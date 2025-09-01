# Auth_Service_Sample
Django Authentication Service

A simple user authentication system built with Django, PostgreSQL, and Redis, and then deployed on Railway.
This project is part of an assesment task at Bill Station. It provides APIs for registration, login, logout, and password reset.

Features
• User registration & login with JWT authentication
• Password reset (via django-rest-passwordreset)
• Session & token management with Redis
• PostgreSQL as the database
• Static files served using Whitenoise in production
• Deployed on Railway

Setup
1. Clone the repo
    git clone https://github.com/your-username/django-auth-service.git
    cd django-auth-service

2. Create and activate a virtual environment
    python -m venv env_name
    source env_name/bin/activate or env_name\Scripts\activate depending on your Operating System

3. Install dependencies
    pip install -r requirements.txt

4. Environment variables
Create a .env file in the project root. Include the following:
    DEBUG=True
    SECRET_KEY=your-secret-key
    DATABASE_URL= your_Postgres_url
    REDIS_URL= your_Redis_url

5. Run migrations with:
    python manage.py migrate

6. Create a superuser with:
    python manage.py createsuperuser

7. Run locally
    python manage.py runserver

🌐 Deployment on Railway
    Railway automatically builds from your repo using the requirements.txt and Procfile.
    Whitenoise serves static files.
    App listens on 0.0.0.0:$PORT (Railway maps this to your live URL).

📡 API Documentation
Auth Endpoints
    1. Register User

    POST /auth/register/

    {
    "username": "john",
    "email": "john@example.com",
    "password": "securepassword123"
    }

    2. Login

    POST /auth/login/

    {
    "username": "john",
    "password": "securepassword123"
    }

    Response includes JWT access & refresh tokens.

    3. Logout

    POST /auth/logout/ (requires Authorization header with token)

    4. Password Reset Request

    POST /auth/password_reset/

    { "email": "john@example.com" }

    5. Password Reset Confirm

    POST /auth/password_reset/confirm/

    {
    "token": "reset-token",
    "password": "newsecurepassword"
    }

🛠️ Tech Stack
    Backend: Django, Django REST Framework
    Database: PostgreSQL (via Railway/Supabase)
    Cache/Session: Redis
    Deployment: Railway
    Static files: Whitenoise

✅ Usage
    Visit /admin/ → Django admin panel
    Visit /auth/register/ → Register new users
    Use /auth/login/ → Authenticate & receive JWT tokens
    Include Authorization: Bearer <token> in requests to access protected routes