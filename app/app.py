"""
Plan:

1. Get a long URL from the user
2. Save the long URL in the database
3. Get the unique ID created by the database
    3.1 We know that in base10 we have 6 places of value, however, 
        base 64 can be represented the same but in 3 values instead 
        making it smaller.
4. Turn that ID into a short code
5. Cache the short code and long URL in Redis
6. Return the short URL to the user

When someone uses the short URL:

1. Check Redis for the short code
2. If it is there, get the long URL from the cache
3. If it is not there, get it from the database and cache it
4. Redirect the user to the long URL
"""


import os
import string

from flask import Flask, request, redirect, jsonify
import redis
import psycopg2

app = Flask(__name__)

ALPHABET = string.digits + string.ascii_lowercase + string.ascii_uppercase

# Connect to Redis for fast lookups
cache = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    decode_responses=True,
)

def get_db():
    """Connect to PostgreSQL for permanent storage."""
    return psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST", "db"),
        database=os.environ.get("POSTGRES_DB", "urlshortener"),
        user=os.environ.get("POSTGRES_USER", "postgres"),
        password=os.environ.get("POSTGRES_PASSWORD", "postgres"),
    )

@app.route("/shorten", methods=["POST"])
def shorten():
    pass