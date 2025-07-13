
#  Django-Powered Paragraph Upload and Search Tool 🔍

## 🧩 Project Architecture

```
textapi/
├── core/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/core/
│   │   ├── base.html
│   │   ├── login.html         
│   │   ├── register.html
│   │   ├── upload.html
│   │   └── search.html
│   └── static/core/
│       └── style.css
├── textapi/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── docker-compose.yml
├── Dockerfile
├── .env
└── README.md
```

## 🛠️ Key Features

- ✅ Register & Login APIs (token auth)
- ✅ Upload and index paragraphs
- ✅ Search for word-matched paragraphs
- ✅ Swagger API docs
- ✅ PostgreSQL backend
- ✅ Dockerized setup

##  How It Works

1. User registers and logs in
2. Upload paragraphs (split by `\n\n`)
3. System indexes words for fast search
4. Authenticated API access

## 🚀 How to Run the Project

###  Prerequisites
- Install Docker Desktop

- Ensure Docker is running

- Docker Desktop installed and running

###  Setup and Run

Now run:   docker-compose up --build

```bash
cd C:\Users\name\Django-Project\textapi
docker-compose up --build
```
-Starting development server at http://0.0.0.0:8000/

### ✅ Run Migrations

Open a new terminal:

-for any model changes
```bash
cd C:\Users\user\Django-Project\textapi
docker-compose exec web python manage.py migrate
```

### ✅ Access in Browser

- App: `http://localhost:8000/`
- Swagger Docs: `http://localhost:8000/swagger/`

## 📄 Technologies Used

| Tech                      Description                        
|--------------------------------------------------
| Django                   Web framework                      
| DRF                         REST API handling                  
| PostgreSQL            Relational DB                      
| Docker                   Containerize environment           
| HTML/CSS              Frontend UI                        
| Swagger                 API documentation                  
| Token Auth            Secure user sessions               

## 📘 API Endpoints Summary

| Endpoint        | Method | Description               
|-----------------|---------|---------------------------
| /api/register/  | POST   | Register user             
| /api/login/      | POST   | Login and get token       
| /api/upload/   | POST   | Upload paragraphs         
| /api/search/    | GET     | Search paragraphs by word 
| /swagger/       | GET     | API docs (Swagger UI)     

## ✅ Extras

- `.env used to store secrets like SECRET_KEY, DB credentials
