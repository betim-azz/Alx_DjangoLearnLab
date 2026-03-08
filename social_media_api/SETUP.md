# Social Media API - Setup and Authentication Guide

## Project Overview
A Django REST API for social media functionality with user authentication, profiles, posts, comments, likes, and notifications.

## Prerequisites
- Python 3.11+
- pip (Python package manager)
- PostgreSQL (for production) or SQLite (for development)

## Installation and Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

Required packages:
- Django 5.2.11
- djangorestframework 3.16.1
- django-filter 25.2
- psycopg2-binary (for PostgreSQL)
- dj-database-url
- gunicorn (for production)
- whitenoise (for static files)

### Step 2: Environment Configuration

Create a `.env` file in the project root (copy from `.env.example`):
```bash
cp .env.example .env
```

For development, use these settings:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
USE_S3=False
```

### Step 3: Database Setup

Run migrations to create database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 5: Start Development Server
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## User Authentication System

### Custom User Model

The API uses a custom user model (`CustomUser`) that extends Django's `AbstractUser` with additional fields:

**Fields:**
- `username` - Unique username (inherited)
- `email` - Email address (inherited)
- `password` - Hashed password (inherited)
- `bio` - User biography (TextField, optional)
- `profile_picture` - Profile picture URL (URLField, optional)
- `following` - ManyToMany relationship to other users (for follow system)

**Model Location:** `accounts/models.py`

### Authentication Endpoints

#### 1. User Registration
**Endpoint:** `POST /api/accounts/register/`

**Request Body:**
```json
{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123",
    "bio": "Software developer",
    "profile_picture": "https://example.com/profile.jpg"
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "bio": "Software developer",
    "profile_picture": "https://example.com/profile.jpg"
}
```

**Notes:**
- A token is automatically created for the user upon registration
- Only `username` and `password` are required
- `email`, `bio`, and `profile_picture` are optional

#### 2. User Login
**Endpoint:** `POST /api/accounts/login/`

**Request Body:**
```json
{
    "username": "johndoe",
    "password": "securepassword123"
}
```

**Response (200 OK):**
```json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

**Notes:**
- Returns an authentication token
- Token must be included in subsequent authenticated requests

#### 3. User Profile
**Endpoint:** `GET /api/accounts/profile/`

**Headers:**
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Response (200 OK):**
```json
{
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "bio": "Software developer",
    "profile_picture": "https://example.com/profile.jpg",
    "followers": []
}
```

**Update Profile:** `PUT /api/accounts/profile/`

**Request Body:**
```json
{
    "bio": "Updated bio",
    "profile_picture": "https://example.com/new-profile.jpg"
}
```

**Notes:**
- Requires authentication token
- Returns current user's profile information
- Can update bio and profile_picture

#### 4. Follow User
**Endpoint:** `POST /api/accounts/follow/<user_id>/`

**Headers:**
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Response (200 OK):**
```json
{
    "message": "Now following username"
}
```

#### 5. Unfollow User
**Endpoint:** `POST /api/accounts/unfollow/<user_id>/`

**Headers:**
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Response (200 OK):**
```json
{
    "message": "Unfollowed username"
}
```

## Testing with Postman

### 1. Register a New User
- Method: POST
- URL: `http://127.0.0.1:8000/api/accounts/register/`
- Body (JSON):
```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123"
}
```

### 2. Login
- Method: POST
- URL: `http://127.0.0.1:8000/api/accounts/login/`
- Body (JSON):
```json
{
    "username": "testuser",
    "password": "testpass123"
}
```
- Copy the token from the response

### 3. Access Profile
- Method: GET
- URL: `http://127.0.0.1:8000/api/accounts/profile/`
- Headers:
  - Key: `Authorization`
  - Value: `Token <your-token-here>`

## Testing with cURL

### Register
```bash
curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"testpass123"}'
```

### Login
```bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

### Get Profile
```bash
curl -X GET http://127.0.0.1:8000/api/accounts/profile/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

## Project Structure

```
social_media_api/
├── accounts/                 # User authentication app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py            # CustomUser model
│   ├── serializers.py       # User serializers
│   ├── views.py             # Authentication views
│   ├── urls.py              # Account URLs
│   └── tests.py
├── posts/                    # Posts app
├── notifications/            # Notifications app
├── social_media_api/         # Project settings
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
├── Procfile                 # Heroku deployment
├── runtime.txt              # Python version
├── DEPLOYMENT.md            # Deployment guide
└── README.md
```

## Security Features

- **Token Authentication:** Secure token-based authentication using Django REST Framework
- **Password Hashing:** Passwords are automatically hashed using Django's built-in password hashers
- **CSRF Protection:** Enabled for all state-changing operations
- **XSS Protection:** Secure browser XSS filter enabled
- **SQL Injection Prevention:** Django ORM prevents SQL injection attacks
- **HTTPS Enforcement:** SSL redirect enabled in production

## REST Framework Configuration

The API uses Django REST Framework with the following settings:

**Authentication:**
- Token Authentication (default)

**Permissions:**
- IsAuthenticatedOrReadOnly (default)
- Specific views may override with IsAuthenticated

**Configuration Location:** `social_media_api/settings.py`

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}
```

## Common Issues and Solutions

### Issue: "No such table: authtoken_token"
**Solution:** Run migrations
```bash
python manage.py migrate
```

### Issue: "Invalid token"
**Solution:** 
- Ensure token is prefixed with "Token " in Authorization header
- Verify token exists in database
- Re-login to get a new token

### Issue: "Authentication credentials were not provided"
**Solution:** 
- Add Authorization header to request
- Format: `Authorization: Token <your-token>`

## Next Steps

After setting up authentication, you can:
1. Create posts using the posts API
2. Add comments and likes to posts
3. Follow/unfollow other users
4. Receive notifications for interactions
5. Deploy to production (see DEPLOYMENT.md)

## API Documentation

Full API documentation is available at:
- Development: `http://127.0.0.1:8000/api/`
- Admin Panel: `http://127.0.0.1:8000/admin/`

## Support

For issues or questions:
- Check the DEPLOYMENT.md for production setup
- Review Django REST Framework documentation: https://www.django-rest-framework.org/
- Review Django documentation: https://docs.djangoproject.com/

## License

MIT License
