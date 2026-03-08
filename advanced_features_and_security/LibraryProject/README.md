# Django Security and Permissions Implementation

## Task 1: Permissions and Groups

### Custom Permissions
The `Book` model includes four custom permissions:
- `can_view`: Permission to view books
- `can_create`: Permission to create new books
- `can_edit`: Permission to edit existing books
- `can_delete`: Permission to delete books

### Groups Setup
Create the following groups in Django Admin and assign permissions:

1. **Viewers Group**
   - Permissions: `can_view`

2. **Editors Group**
   - Permissions: `can_view`, `can_create`, `can_edit`

3. **Admins Group**
   - Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`

### Setting Up Groups (via Django Admin or Shell)
```python
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

# Get content type for Book model
content_type = ContentType.objects.get_for_model(Book)

# Get permissions
can_view = Permission.objects.get(codename='can_view', content_type=content_type)
can_create = Permission.objects.get(codename='can_create', content_type=content_type)
can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

# Create groups
viewers = Group.objects.create(name='Viewers')
viewers.permissions.add(can_view)

editors = Group.objects.create(name='Editors')
editors.permissions.add(can_view, can_create, can_edit)

admins = Group.objects.create(name='Admins')
admins.permissions.add(can_view, can_create, can_edit, can_delete)
```

### Testing Permissions
1. Create test users in Django Admin
2. Assign users to different groups
3. Log in as each user and test access to:
   - `/books/` (requires can_view)
   - `/books/create/` (requires can_create)
   - `/books/<id>/edit/` (requires can_edit)
   - `/books/<id>/delete/` (requires can_delete)

## Task 2: Security Best Practices

### Security Settings Implemented
1. **DEBUG = False**: Disabled in production to prevent sensitive information exposure
2. **SECURE_BROWSER_XSS_FILTER = True**: Enables browser XSS filtering
3. **X_FRAME_OPTIONS = 'DENY'**: Prevents clickjacking attacks
4. **SECURE_CONTENT_TYPE_NOSNIFF = True**: Prevents MIME-sniffing
5. **CSRF_COOKIE_SECURE = True**: CSRF cookies only sent over HTTPS
6. **SESSION_COOKIE_SECURE = True**: Session cookies only sent over HTTPS

### CSRF Protection
All forms include `{% csrf_token %}` to protect against CSRF attacks.

### SQL Injection Prevention
- All database queries use Django ORM with parameterized queries
- User inputs are validated using Django Forms
- Example: `Book.objects.filter(title__icontains=query)` instead of raw SQL

### Input Validation
- All user inputs are validated through Django Forms
- Forms provide automatic sanitization and validation

## Task 3: HTTPS and Secure Redirects

### HTTPS Configuration
1. **SECURE_SSL_REDIRECT = True**: Redirects all HTTP requests to HTTPS
2. **SECURE_HSTS_SECONDS = 31536000**: Enforces HTTPS for 1 year
3. **SECURE_HSTS_INCLUDE_SUBDOMAINS = True**: Applies HSTS to all subdomains
4. **SECURE_HSTS_PRELOAD = True**: Allows HSTS preloading in browsers

### Deployment Configuration
For production deployment with HTTPS, configure your web server:

#### Nginx Example
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com;
    
    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;
    
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

#### Apache Example
```apache
<VirtualHost *:80>
    ServerName yourdomain.com
    Redirect permanent / https://yourdomain.com/
</VirtualHost>

<VirtualHost *:443>
    ServerName yourdomain.com
    
    SSLEngine on
    SSLCertificateFile /path/to/certificate.crt
    SSLCertificateKeyFile /path/to/private.key
    
    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/
</VirtualHost>
```

### Security Review
- All HTTP traffic is redirected to HTTPS
- Cookies are only transmitted over secure connections
- HSTS policy ensures browsers always use HTTPS
- XSS and clickjacking protections are enabled
- CSRF protection is enforced on all forms
- SQL injection is prevented through ORM usage
- User inputs are validated and sanitized

### Areas for Improvement
- Implement Content Security Policy (CSP) headers
- Add rate limiting for API endpoints
- Implement two-factor authentication
- Regular security audits and dependency updates
- Use environment variables for sensitive settings
