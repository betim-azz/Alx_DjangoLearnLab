# Django Blog Authentication System

## Overview

This project includes a fully functional user authentication system utilizing Django's built-in `auth` views and custom forms.

## Features

- **Registration:** Users can create an account at `/register/`. The form requires a username, email, and password. It securely hashes passwords.
- **Login/Logout:** Handled at `/login/` and `/logout/` via Django's `LoginView` and `LogoutView`.
- **Profile Management:** Authenticated users can navigate to `/profile/` to update their username, email, bio, and upload a profile picture.

## Security

- **CSRF Protection:** All forms include `{% csrf_token %}` to prevent Cross-Site Request Forgery.
- **Password Hashing:** Django's default PBKDF2 algorithm handles all password security.
- **Access Control:** The `@login_required` decorator restricts unauthorized users from accessing the `/profile/` endpoint.

## How to Test

1. Run the server: `python manage.py runserver`
2. Navigate to `http://127.0.0.1:8000/register/` and create an account.
3. Upon success, log in at `http://127.0.0.1:8000/login/`.
4. Navigate to `http://127.0.0.1:8000/profile/` to test updating information.
