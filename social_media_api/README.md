# Social Media API

Setup:

1. `pip install django djangorestframework pillow`
2. `python manage.py migrate`
3. `python manage.py runserver`

Auth Endpoints:

- `POST /api/accounts/register/`
- `POST /api/accounts/login/`
- `GET /api/accounts/profile/` (Requires Authorization header: `Token <your_token>`)
