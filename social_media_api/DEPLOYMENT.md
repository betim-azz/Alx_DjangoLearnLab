# Social Media API - Deployment Guide

## Overview
This guide provides step-by-step instructions for deploying the Social Media API to production environments.

## Prerequisites
- Python 3.11+
- PostgreSQL database
- Git
- Hosting service account (Heroku, AWS, DigitalOcean, etc.)

## Deployment Options

### Option 1: Heroku Deployment

#### Step 1: Install Heroku CLI
```bash
# Download and install from https://devcenter.heroku.com/articles/heroku-cli
```

#### Step 2: Login and Create App
```bash
heroku login
heroku create your-app-name
```

#### Step 3: Add PostgreSQL Database
```bash
heroku addons:create heroku-postgresql:mini
```

#### Step 4: Set Environment Variables
```bash
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"
heroku config:set USE_S3=False
```

#### Step 5: Deploy
```bash
git add .
git commit -m "Prepare for deployment"
git push heroku main
```

#### Step 6: Run Migrations
```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku run python manage.py collectstatic --noinput
```

#### Step 7: Open Application
```bash
heroku open
```

### Option 2: AWS Elastic Beanstalk

#### Step 1: Install EB CLI
```bash
pip install awsebcli
```

#### Step 2: Initialize EB Application
```bash
eb init -p python-3.11 social-media-api
```

#### Step 3: Create Environment
```bash
eb create social-media-api-env
```

#### Step 4: Set Environment Variables
```bash
eb setenv SECRET_KEY="your-secret-key" DEBUG=False ALLOWED_HOSTS="your-domain.com"
```

#### Step 5: Deploy
```bash
eb deploy
```

### Option 3: DigitalOcean/VPS Deployment

#### Step 1: Server Setup
```bash
# SSH into your server
ssh root@your-server-ip

# Update system
apt update && apt upgrade -y

# Install dependencies
apt install python3-pip python3-venv postgresql nginx -y
```

#### Step 2: Clone Repository
```bash
cd /var/www
git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
```

#### Step 3: Setup Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Step 4: Configure Environment Variables
```bash
cp .env.example .env
nano .env
# Edit with your production values
```

#### Step 5: Setup PostgreSQL
```bash
sudo -u postgres psql
CREATE DATABASE social_media_db;
CREATE USER dbuser WITH PASSWORD 'your-password';
GRANT ALL PRIVILEGES ON DATABASE social_media_db TO dbuser;
\q
```

#### Step 6: Run Migrations
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

#### Step 7: Configure Gunicorn Service
```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Add:
```ini
[Unit]
Description=gunicorn daemon for social_media_api
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/Alx_DjangoLearnLab/social_media_api
EnvironmentFile=/var/www/Alx_DjangoLearnLab/social_media_api/.env
ExecStart=/var/www/Alx_DjangoLearnLab/social_media_api/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/var/www/Alx_DjangoLearnLab/social_media_api/gunicorn.sock \
          social_media_api.wsgi:application

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

#### Step 8: Configure Nginx
```bash
sudo cp nginx.conf /etc/nginx/sites-available/social_media_api
sudo ln -s /etc/nginx/sites-available/social_media_api /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 9: Setup SSL with Let's Encrypt
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| SECRET_KEY | Django secret key | `django-insecure-...` |
| DEBUG | Debug mode (False in production) | `False` |
| ALLOWED_HOSTS | Comma-separated allowed hosts | `yourdomain.com,www.yourdomain.com` |
| DATABASE_URL | PostgreSQL connection string | `postgresql://user:pass@host:5432/db` |
| USE_S3 | Enable AWS S3 for media files | `True` or `False` |
| AWS_ACCESS_KEY_ID | AWS access key | `AKIAIOSFODNN7EXAMPLE` |
| AWS_SECRET_ACCESS_KEY | AWS secret key | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| AWS_STORAGE_BUCKET_NAME | S3 bucket name | `my-media-bucket` |

## Post-Deployment Checklist

- [ ] Verify DEBUG=False in production
- [ ] Confirm ALLOWED_HOSTS is properly configured
- [ ] Test all API endpoints
- [ ] Verify database migrations are applied
- [ ] Check static files are served correctly
- [ ] Test media file uploads (if applicable)
- [ ] Verify SSL certificate is active
- [ ] Setup monitoring and logging
- [ ] Configure automated backups
- [ ] Test authentication flows
- [ ] Review security headers

## Monitoring and Maintenance

### Logging
Application logs are configured to output to console. For production:
- Heroku: `heroku logs --tail`
- AWS: CloudWatch Logs
- VPS: `/var/log/gunicorn/` and `/var/log/nginx/`

### Database Backups
```bash
# Heroku
heroku pg:backups:capture
heroku pg:backups:download

# PostgreSQL (VPS)
pg_dump -U dbuser social_media_db > backup_$(date +%Y%m%d).sql
```

### Updates
```bash
# Pull latest changes
git pull origin main

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart services
sudo systemctl restart gunicorn
```

## Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
# Check STATIC_ROOT and STATIC_URL settings
```

### Database Connection Issues
- Verify DATABASE_URL or individual DB credentials
- Check PostgreSQL service is running
- Confirm firewall rules allow database connections

### 502 Bad Gateway
- Check gunicorn service status: `sudo systemctl status gunicorn`
- Review gunicorn logs: `sudo journalctl -u gunicorn`
- Verify socket file permissions

## Security Best Practices

1. Never commit `.env` file to version control
2. Use strong SECRET_KEY (generate with `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`)
3. Keep DEBUG=False in production
4. Use HTTPS/SSL certificates
5. Regularly update dependencies
6. Implement rate limiting
7. Setup CORS properly if needed
8. Use environment variables for all secrets

## Support and Resources

- Django Deployment Checklist: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
- Heroku Django Guide: https://devcenter.heroku.com/articles/django-app-configuration
- AWS Elastic Beanstalk: https://docs.aws.amazon.com/elasticbeanstalk/
- DigitalOcean Tutorials: https://www.digitalocean.com/community/tutorials

## Live Application

**URL**: [To be added after deployment]

**API Documentation**: [Your-Domain]/api/

**Admin Panel**: [Your-Domain]/admin/
