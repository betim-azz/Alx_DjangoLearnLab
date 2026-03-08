# Quick Reference Card

## Setup Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver

# Run tests
python test_api.py
```

## API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | /api/accounts/register/ | No | Register new user |
| POST | /api/accounts/login/ | No | Login and get token |
| GET | /api/accounts/profile/ | Yes | Get user profile |
| PUT | /api/accounts/profile/ | Yes | Update profile |
| POST | /api/accounts/follow/<id>/ | Yes | Follow user |
| POST | /api/accounts/unfollow/<id>/ | Yes | Unfollow user |

## Quick Test

```bash
# Register
curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"test123"}'

# Login
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test","password":"test123"}'

# Get Profile (replace TOKEN)
curl -X GET http://127.0.0.1:8000/api/accounts/profile/ \
  -H "Authorization: Token TOKEN"
```

## Deployment

### Heroku
```bash
heroku create app-name
heroku addons:create heroku-postgresql:mini
heroku config:set SECRET_KEY="key" DEBUG=False
git push heroku main
heroku run python manage.py migrate
```

### Docker
```bash
docker-compose up --build
```

## Environment Variables

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://user:pass@host:5432/db
USE_S3=False
```

## Common Issues

**Token not working?**
- Format: `Authorization: Token <token>`
- Include "Token " prefix

**Database error?**
- Run: `python manage.py migrate`

**Static files missing?**
- Run: `python manage.py collectstatic`

## Documentation

- **SETUP.md** - Complete setup guide
- **API_TESTING.md** - API testing reference
- **DEPLOYMENT.md** - Deployment guide
- **CHECKLIST.md** - Deployment checklist

## Support

- Django Docs: https://docs.djangoproject.com/
- DRF Docs: https://www.django-rest-framework.org/
