# 🔗 FastAPI URL Shortener

A secure URL Shortener REST API built with FastAPI and SQLAlchemy featuring JWT authentication, user-specific URL management, click analytics, and modular backend architecture.

---

## Features

- User Registration
- User Login (JWT Authentication)
- Protected Routes
- Create Short URLs
- URL Redirection
- Click Analytics
- My URLs Endpoint
- Delete URLs
- SQLite Database
- SQLAlchemy ORM
- RESTful API Design

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Pydantic
- Uvicorn

---

## Project Structure

URLShortener/
│
├── models/
├── routers/
├── schemas/
├── services/
├── database.py
├── dependencies.py
├── security.py
├── main.py
├── requirements.txt
└── README.md

---

## Installation

git clone https://github.com/YOUR_USERNAME/fastapi-url-shortener.git

cd fastapi-url-shortener

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload

---

## API Endpoints

POST    /register

POST    /login

GET     /me

POST    /shorten

GET     /{short_code}

GET     /analytics/{short_code}

GET     /my-urls

DELETE  /delete/{short_code}

---

## Authentication

This project uses JWT Authentication.

Include the token in every protected request:

Authorization: Bearer <your_token>

---

## Example Response

{
    "original_url": "https://google.com",
    "short_code": "zwIRqL"
}

---

## Future Improvements

- PostgreSQL
- Docker
- Custom Aliases
- QR Codes
- URL Expiration
- Rate Limiting

---

## Author

Meet Bakotra

LinkedIn:
https://linkedin.com/in/meet-bakotra-46b9122bb

GitHub:
https://github.com/Meet03-hub