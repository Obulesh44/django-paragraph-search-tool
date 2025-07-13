# 🧠 Django-Powered Paragraph Upload and Search Tool

A Django-powered REST API project for uploading, indexing, and searching text paragraphs using token-based authentication. Fully containerized using Docker.

---

## 🚀 Features

- ✅ User registration & login via token-based auth
- ✅ Upload multiple paragraphs at once
- ✅ Indexes each word for fast search
- ✅ Word-based paragraph search endpoint
- ✅ PostgreSQL as the relational database
- ✅ Secure token-based access to protected routes
- ✅ Swagger API documentation available
- ✅ Responsive web UI for manual upload/search

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: TokenAuthentication (DRF)
- **Containerization**: Docker, docker-compose
- **API Docs**: Swagger (drf-yasg)
- **Frontend**: HTML, CSS, Django Templates

---

## 📁 Project Structure

```
textapi/
│
├── core/                     # HTML templates & static CSS
│   ├── templates/
│   └── static/
│
├── api/                      # API logic
│   ├── views.py              # Auth, Upload, Search
│   ├── serializers.py        # User serializer
│   ├── models.py             # User, Paragraph, WordIndex models
│
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env
```

---

## ⚙️ Setup Instructions

### 📍 Local (Manual)

```bash
# 1. Clone the repo
git clone https://github.com/your-username/textapi.git
cd textapi

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate       # On Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure .env file
cp .env.example .env

# 5. Run migrations
python manage.py migrate

# 6. Start the server
python manage.py runserver
```

### 🐳 Docker Setup

```bash
# 1. Create .env from template
cp .env.example .env

# 2. Build containers
docker-compose build

# 3. Run the stack
docker-compose up

# 4. Apply DB migrations inside container
docker-compose exec web python manage.py migrate

# 5. Visit:
http://localhost:8000/
http://localhost:8000/swagger/  # API docs
```

---

## 🔐 API Authentication Flow

1. **Register** (`/api/register/`) — Get a token
2. **Login** (`/api/login/`) — Get token + user info
3. **Upload/Search** — Send `Authorization: Token <token>` in headers

---

## 🔎 API Endpoints

| Method | Endpoint        | Description                  |
|--------|-----------------|------------------------------|
| POST   | `/api/register/` | Register new user (get token)|
| POST   | `/api/login/`    | Login with email/password    |
| POST   | `/api/upload/`   | Upload paragraph(s)          |
| GET    | `/api/search/`   | Search word in paragraphs    |

All except `/register` & `/login` require **token authentication**.

---

## 📖 Example JSON for Upload

```json
{
  "text": "Python is a powerful language.

It is used for web development."
}
```

---

## 📘 Swagger UI

Available at: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

Use it to explore and test all endpoints.

---

## 🧠 Best Practices Followed

- [x] Google Python style guide followed
- [x] Clear comments & docstrings
- [x] RESTful conventions respected
- [x] Environment-specific secrets stored in `.env`
- [x] Dockerized setup with `docker-compose`

---

## ✅ Commit Message Guidelines

- `feat: upload API endpoint`
- `fix: token auth bug`
- `docs: add README`
- `style: navbar alignment`
- `refactor: search query optimization`

---

## 👏 Acknowledgments

This project was developed as part of a full-stack Django + REST + PostgreSQL learning journey with modern tooling like Docker.

---

> Feel free to fork, extend, or contribute! ⭐