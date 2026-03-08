#!/usr/bin/env python
"""
Management script for deployment tasks
"""
import os
import sys
import subprocess

def run_command(command):
    """Execute shell command"""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def collect_static():
    """Collect static files"""
    print("Collecting static files...")
    run_command("python manage.py collectstatic --noinput")

def migrate():
    """Run database migrations"""
    print("Running migrations...")
    run_command("python manage.py migrate")

def create_superuser():
    """Create superuser"""
    print("Creating superuser...")
    run_command("python manage.py createsuperuser")

def check_deployment():
    """Run deployment checks"""
    print("Running deployment checks...")
    run_command("python manage.py check --deploy")

def backup_db():
    """Backup database"""
    print("Backing up database...")
    db_name = os.getenv('DB_NAME', 'social_media_db')
    backup_file = f"backup_{db_name}.sql"
    run_command(f"pg_dump {db_name} > {backup_file}")
    print(f"Database backed up to {backup_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python manage_deployment.py [collect_static|migrate|create_superuser|check|backup]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    commands = {
        'collect_static': collect_static,
        'migrate': migrate,
        'create_superuser': create_superuser,
        'check': check_deployment,
        'backup': backup_db,
    }
    
    if command in commands:
        commands[command]()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()
