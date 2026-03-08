# Social Media API - Deployment Checklist

## Pre-Deployment Checklist

### Development Setup ✓
- [x] Django project created
- [x] Django REST Framework installed
- [x] Custom user model implemented
- [x] Token authentication configured
- [x] User registration endpoint
- [x] User login endpoint
- [x] User profile endpoint
- [x] Follow/unfollow functionality

### Configuration Files ✓
- [x] settings.py configured for production
- [x] requirements.txt with all dependencies
- [x] .env.example created
- [x] .gitignore configured
- [x] Procfile for Heroku
- [x] runtime.txt for Python version
- [x] gunicorn_config.py
- [x] nginx.conf
- [x] Dockerfile
- [x] docker-compose.yml

### Security Settings ✓
- [x] DEBUG=False in production
- [x] SECRET_KEY from environment variable
- [x] ALLOWED_HOSTS configured
- [x] SECURE_BROWSER_XSS_FILTER enabled
- [x] SECURE_CONTENT_TYPE_NOSNIFF enabled
- [x] X_FRAME_OPTIONS set to DENY
- [x] SECURE_SSL_REDIRECT enabled
- [x] SESSION_COOKIE_SECURE enabled
- [x] CSRF_COOKIE_SECURE enabled
- [x] SECURE_HSTS_SECONDS configured

### Documentation ✓
- [x] README.md
- [x] SETUP.md
- [x] API_TESTING.md
- [x] DEPLOYMENT.md
- [x] PROJECT_SUMMARY.md

## Testing Checklist

### Local Testing
- [ ] Run migrations: `python manage.py migrate`
- [ ] Create superuser: `python manage.py createsuperuser`
- [ ] Start server: `python manage.py runserver`
- [ ] Access admin panel: http://127.0.0.1:8000/admin
- [ ] Run automated tests: `python test_api.py`

### API Endpoint Testing

#### Registration
- [ ] POST /api/accounts/register/
  - [ ] With valid data
  - [ ] With duplicate username
  - [ ] With missing required fields
  - [ ] Verify token is created

#### Login
- [ ] POST /api/accounts/login/
  - [ ] With valid credentials
  - [ ] With invalid credentials
  - [ ] Verify token is returned

#### Profile
- [ ] GET /api/accounts/profile/
  - [ ] With valid token
  - [ ] Without token (should fail)
  - [ ] With invalid token (should fail)
- [ ] PUT /api/accounts/profile/
  - [ ] Update bio
  - [ ] Update profile_picture
  - [ ] Verify changes persist

#### Follow/Unfollow
- [ ] POST /api/accounts/follow/<user_id>/
  - [ ] Follow another user
  - [ ] Try to follow self (should fail)
- [ ] POST /api/accounts/unfollow/<user_id>/
  - [ ] Unfollow a user

### Manual Testing with Tools
- [ ] Test with Postman
- [ ] Test with cURL
- [ ] Test with Python requests
- [ ] Test with browser (for GET endpoints)

## Deployment Checklist

### Pre-Deployment
- [ ] All tests passing
- [ ] Code committed to Git
- [ ] .env file NOT committed
- [ ] Database migrations created
- [ ] Static files collected locally

### Environment Variables
- [ ] SECRET_KEY set
- [ ] DEBUG set to False
- [ ] ALLOWED_HOSTS configured
- [ ] DATABASE_URL configured (if using PostgreSQL)
- [ ] AWS credentials (if using S3)

### Heroku Deployment
- [ ] Heroku CLI installed
- [ ] Heroku account created
- [ ] App created: `heroku create app-name`
- [ ] PostgreSQL addon: `heroku addons:create heroku-postgresql:mini`
- [ ] Environment variables set: `heroku config:set KEY=value`
- [ ] Code pushed: `git push heroku main`
- [ ] Migrations run: `heroku run python manage.py migrate`
- [ ] Superuser created: `heroku run python manage.py createsuperuser`
- [ ] Static files collected: `heroku run python manage.py collectstatic`

### AWS Deployment
- [ ] AWS account created
- [ ] EB CLI installed
- [ ] Application initialized: `eb init`
- [ ] Environment created: `eb create`
- [ ] Environment variables set: `eb setenv`
- [ ] Code deployed: `eb deploy`

### VPS Deployment
- [ ] Server provisioned
- [ ] SSH access configured
- [ ] Python installed
- [ ] PostgreSQL installed
- [ ] Nginx installed
- [ ] Code cloned from Git
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Database created
- [ ] Migrations run
- [ ] Gunicorn service configured
- [ ] Nginx configured
- [ ] SSL certificate installed
- [ ] Firewall configured

### Docker Deployment
- [ ] Docker installed
- [ ] Docker Compose installed
- [ ] .env file configured
- [ ] Build images: `docker-compose build`
- [ ] Start containers: `docker-compose up -d`
- [ ] Run migrations: `docker-compose exec web python manage.py migrate`
- [ ] Create superuser: `docker-compose exec web python manage.py createsuperuser`

## Post-Deployment Checklist

### Verification
- [ ] Application accessible via URL
- [ ] Admin panel accessible
- [ ] Registration endpoint working
- [ ] Login endpoint working
- [ ] Profile endpoint working (with authentication)
- [ ] Static files loading correctly
- [ ] HTTPS working (SSL certificate valid)
- [ ] Database connections working

### Security Verification
- [ ] DEBUG is False
- [ ] Admin panel requires authentication
- [ ] API endpoints require authentication where appropriate
- [ ] HTTPS redirect working
- [ ] Security headers present
- [ ] No sensitive data in logs

### Performance
- [ ] Response times acceptable
- [ ] Database queries optimized
- [ ] Static files cached
- [ ] Gzip compression enabled

### Monitoring Setup
- [ ] Logging configured
- [ ] Error tracking setup
- [ ] Performance monitoring
- [ ] Uptime monitoring
- [ ] Database backup scheduled

### Documentation
- [ ] Live URL documented
- [ ] API documentation accessible
- [ ] Deployment notes updated
- [ ] Environment variables documented

## Maintenance Checklist

### Regular Tasks
- [ ] Monitor application logs
- [ ] Check error rates
- [ ] Review performance metrics
- [ ] Backup database
- [ ] Update dependencies
- [ ] Apply security patches

### Weekly
- [ ] Review error logs
- [ ] Check disk space
- [ ] Verify backups
- [ ] Test critical endpoints

### Monthly
- [ ] Update dependencies
- [ ] Security audit
- [ ] Performance review
- [ ] Database optimization

### Quarterly
- [ ] Major version updates
- [ ] Infrastructure review
- [ ] Security assessment
- [ ] Disaster recovery test

## Troubleshooting Checklist

### Application Won't Start
- [ ] Check environment variables
- [ ] Verify database connection
- [ ] Check migrations status
- [ ] Review error logs
- [ ] Verify dependencies installed

### Authentication Issues
- [ ] Verify token in Authorization header
- [ ] Check token format: "Token <token>"
- [ ] Verify user exists in database
- [ ] Check token hasn't expired

### Database Issues
- [ ] Verify DATABASE_URL
- [ ] Check database service running
- [ ] Verify migrations applied
- [ ] Check database permissions

### Static Files Not Loading
- [ ] Run collectstatic
- [ ] Verify STATIC_ROOT
- [ ] Check web server configuration
- [ ] Verify file permissions

### 502 Bad Gateway
- [ ] Check Gunicorn service status
- [ ] Verify socket file exists
- [ ] Check Nginx configuration
- [ ] Review application logs

## Success Criteria

### Functionality
- [x] Users can register
- [x] Users can login and receive token
- [x] Users can view/update profile with authentication
- [x] Users can follow/unfollow others
- [x] All endpoints return correct status codes
- [x] Error messages are clear and helpful

### Security
- [x] Passwords are hashed
- [x] Tokens are required for protected endpoints
- [x] HTTPS enforced in production
- [x] Security headers configured
- [x] No sensitive data exposed

### Performance
- [ ] Response time < 500ms for most endpoints
- [ ] Database queries optimized
- [ ] Static files cached
- [ ] Application handles concurrent requests

### Documentation
- [x] Setup instructions clear
- [x] API endpoints documented
- [x] Deployment guide complete
- [x] Testing instructions provided

## Final Sign-Off

- [ ] All development tasks complete
- [ ] All tests passing
- [ ] Documentation complete
- [ ] Deployment successful
- [ ] Post-deployment verification complete
- [ ] Monitoring configured
- [ ] Team trained on maintenance

**Deployment Date:** _________________

**Deployed By:** _________________

**Live URL:** _________________

**Notes:** _________________
