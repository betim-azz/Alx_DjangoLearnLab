# API Testing Quick Reference

## Base URL
Development: `http://127.0.0.1:8000`

## Authentication Endpoints

### 1. Register New User
```http
POST /api/accounts/register/
Content-Type: application/json

{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepass123",
    "bio": "Developer",
    "profile_picture": "https://example.com/pic.jpg"
}
```

**Response:**
```json
{
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "bio": "Developer",
    "profile_picture": "https://example.com/pic.jpg"
}
```

### 2. Login
```http
POST /api/accounts/login/
Content-Type: application/json

{
    "username": "johndoe",
    "password": "securepass123"
}
```

**Response:**
```json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### 3. Get Profile (Authenticated)
```http
GET /api/accounts/profile/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Response:**
```json
{
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com",
    "bio": "Developer",
    "profile_picture": "https://example.com/pic.jpg",
    "followers": []
}
```

### 4. Update Profile (Authenticated)
```http
PUT /api/accounts/profile/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
Content-Type: application/json

{
    "bio": "Updated bio",
    "profile_picture": "https://example.com/new-pic.jpg"
}
```

### 5. Follow User (Authenticated)
```http
POST /api/accounts/follow/2/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

### 6. Unfollow User (Authenticated)
```http
POST /api/accounts/unfollow/2/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

## Postman Collection

Import this JSON into Postman:

```json
{
    "info": {
        "name": "Social Media API",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": [
        {
            "name": "Register",
            "request": {
                "method": "POST",
                "header": [{"key": "Content-Type", "value": "application/json"}],
                "body": {
                    "mode": "raw",
                    "raw": "{\"username\":\"testuser\",\"email\":\"test@example.com\",\"password\":\"testpass123\"}"
                },
                "url": "http://127.0.0.1:8000/api/accounts/register/"
            }
        },
        {
            "name": "Login",
            "request": {
                "method": "POST",
                "header": [{"key": "Content-Type", "value": "application/json"}],
                "body": {
                    "mode": "raw",
                    "raw": "{\"username\":\"testuser\",\"password\":\"testpass123\"}"
                },
                "url": "http://127.0.0.1:8000/api/accounts/login/"
            }
        },
        {
            "name": "Get Profile",
            "request": {
                "method": "GET",
                "header": [{"key": "Authorization", "value": "Token {{token}}"}],
                "url": "http://127.0.0.1:8000/api/accounts/profile/"
            }
        }
    ]
}
```

## cURL Commands

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

### Update Profile
```bash
curl -X PUT http://127.0.0.1:8000/api/accounts/profile/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"bio":"Updated bio"}'
```

## Python Requests

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# Register
response = requests.post(f"{BASE_URL}/api/accounts/register/", json={
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123"
})
print(response.json())

# Login
response = requests.post(f"{BASE_URL}/api/accounts/login/", json={
    "username": "testuser",
    "password": "testpass123"
})
token = response.json()["token"]

# Get Profile
headers = {"Authorization": f"Token {token}"}
response = requests.get(f"{BASE_URL}/api/accounts/profile/", headers=headers)
print(response.json())
```

## Status Codes

- `200 OK` - Request successful
- `201 Created` - Resource created successfully
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Authentication required or invalid token
- `403 Forbidden` - Permission denied
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## Common Headers

**For all requests:**
```
Content-Type: application/json
```

**For authenticated requests:**
```
Authorization: Token <your-token-here>
```

## Testing Workflow

1. **Register** a new user → Get user data
2. **Login** with credentials → Get token
3. **Get Profile** with token → Verify authentication
4. **Update Profile** with token → Test updates
5. **Follow/Unfollow** users → Test social features
