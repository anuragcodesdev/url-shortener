# URL Shortener

A simple URL shortener built with a Python Flask API, PostgreSQL, and Redis. It takes a long URL, generates a short code for it, and redirects users to the original URL when the short link is accessed.

## Tech Stack

- Python
- Flask
- PostgreSQL (Not NoSQL because data is highly structured and permits ACID transactions).
- Redis

## Getting Started

Clone the repository:

```bash
git clone https://github.com/anuragcodesdev/url-shortener.git
cd url-shortener