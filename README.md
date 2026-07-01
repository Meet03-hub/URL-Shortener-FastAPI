# 🔗 URL Shortener REST API

A production-ready URL Shortener REST API built with **FastAPI**, **JWT Authentication**, **SQLAlchemy**, and **SQLite**. Users can register, log in securely, shorten URLs, track analytics, manage their own links, and delete them with authorization.

---

## 🚀 Features

- ✅ User Registration
- ✅ JWT Authentication (Login)
- ✅ Password Hashing with bcrypt
- ✅ Create Short URLs
- ✅ Redirect to Original URL
- ✅ Track Click Analytics
- ✅ View User's URLs
- ✅ Delete URLs (Owner Only)
- ✅ Swagger API Documentation
- ✅ RESTful API Design

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | REST API Framework |
| SQLAlchemy | ORM |
| SQLite | Database |
| JWT | Authentication |
| bcrypt | Password Hashing |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |

---

## 📂 Project Structure

```
URLShortener/
│
├── models/
│   ├── user.py
│   └── url.py
│
├── routers/
│   ├── auth.py
│   └── url.py
│
├── schemas/
│   ├── user.py
│   └── url.py
│
├── services/
│   ├── auth_service.py
│   └── url_service.py
│
├── database.py
├── dependencies.py
├── security.py
├── main.py
├── requirements.txt
└── README.md
```

---

# 📌 API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive JWT |
| GET | `/me` | Get logged-in user |

---

## URL Management

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/shorten` | Create Short URL |
| GET | `/{short_code}` | Redirect to Original URL |
| GET | `/analytics/{short_code}` | View Click Analytics |
| GET | `/my-urls` | Get Logged-in User URLs |
| DELETE | `/delete/{short_code}` | Delete URL (Owner Only) |

---

# 🔐 Authentication Flow

1. Register a user.
2. Login using email and password.
3. Receive JWT Access Token.
4. Send the token in the Authorization header.

```
Authorization: Bearer <JWT_TOKEN>
```

Protected endpoints:

- `/me`
- `/shorten`
- `/my-urls`
- `/delete/{short_code}`

---

# 📊 Database Schema

## User

| Field | Type |
|-------|------|
| id | Integer |
| username | String |
| email | String |
| password | String (Hashed) |

---

## URL

| Field | Type |
|-------|------|
| id | Integer |
| original_url | String |
| short_code | String |
| clicks | Integer |
| user_id | Foreign Key |

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/URL-Shortener-FastAPI.git
```

Move into the project

```bash
cd URL-Shortener-FastAPI
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
uvicorn main:app --reload
```

---

# 📖 Interactive API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🧪 Example Workflow

### Register

```
POST /register
```

↓

### Login

```
POST /login
```

↓

Receive JWT Token

↓

### Create Short URL

```
POST /shorten
```

↓

### View URLs

```
GET /my-urls
```

↓

### Analytics

```
GET /analytics/{short_code}
```

↓

### Delete URL

```
DELETE /delete/{short_code}
```

---

# 🔮 Future Improvements

- PostgreSQL Support
- Redis Caching
- Custom Short URLs
- URL Expiration
- QR Code Generation
- Docker Deployment
- Rate Limiting
- Admin Dashboard
- Unit Testing
- CI/CD Pipeline

---

# 📸 Screenshots

Add screenshots of:

- Swagger Documentation
- Registration API
- Login API
- URL Shortening
- Analytics Endpoint
- SQLite Database

---

# 👨‍💻 Author

**Meet Bakotra**

- 📧 meet.bakotra.1@gmail.com
- 💼 LinkedIn: https://linkedin.com/in/meet-bakotra-46b9122bb
- 💻 GitHub: https://github.com/Meet03-hub

---

## ⭐ If you found this project useful, consider giving it a star!
