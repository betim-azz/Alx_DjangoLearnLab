# Social Media API

A production-ready Django REST API for social media functionality including user authentication, posts, comments, likes, and notifications.

## Features

- User registration and authentication with token-based auth
- User profiles and following system
- Post creation, editing, and deletion
- Comments and likes on posts
- Real-time notifications
- RESTful API design
- Production-ready deployment configuration

## Documentation

- **[SETUP.md](SETUP.md)** - Complete setup and authentication guide
- **[API_TESTING.md](API_TESTING.md)** - API testing quick reference
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Production deployment guide

## Quick Start (Development)

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

### Authentication Endpoints

- `POST /api/accounts/register/` - Register new user
- `POST /api/accounts/login/` - Login and get token
- `GET /api/accounts/profile/` - Get user profile (requires token)
- `PUT /api/accounts/profile/` - Update user profile (requires token)
- `POST /api/accounts/follow/<user_id>/` - Follow user (requires token)
- `POST /api/accounts/unfollow/<user_id>/` - Unfollow user (requires token)

### Example: Register and Login

**Register:**
```bash
curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"testpass123"}'
```

**Login:**
```bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

**Get Profile:**
```bash
curl -X GET http://127.0.0.1:8000/api/accounts/profile/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

## Production Deployment

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

### Quick Deploy to Heroku

```bash
# Install Heroku CLI and login
heroku login

# Create app
heroku create your-app-name

# Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# Set environment variables
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Environment Variables

Copy `.env.example` to `.env` and configure:

- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to False in production
- `ALLOWED_HOSTS` - Your domain(s)
- `DATABASE_URL` - PostgreSQL connection string
- `USE_S3` - Enable AWS S3 for media files (optional)

## API Documentation

Full API documentation available at `/api/` when running the server.

## Technology Stack

- Django 5.2.11
- Django REST Framework 3.16.1
- PostgreSQL
- Gunicorn (WSGI server)
- WhiteNoise (Static files)
- AWS S3 (Optional media storage)

## Security Features

- Token-based authentication
- HTTPS enforcement in production
- XSS protection
- CSRF protection
- Secure cookie settings
- SQL injection prevention

## License

MIT License
