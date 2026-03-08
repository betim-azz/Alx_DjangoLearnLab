@echo off
REM Social Media API - Quick Setup Script for Windows

echo ================================================
echo Social Media API - Quick Setup
echo ================================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
echo.

REM Check if .env exists
if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env
    echo.
    echo IMPORTANT: Please edit .env file with your settings
    echo Press any key to continue after editing .env...
    pause
)

REM Run migrations
echo Running database migrations...
python manage.py makemigrations
python manage.py migrate
echo.

REM Ask about superuser
set /p create_super="Do you want to create a superuser? (y/n): "
if /i "%create_super%"=="y" (
    python manage.py createsuperuser
    echo.
)

REM Collect static files
echo Collecting static files...
python manage.py collectstatic --noinput
echo.

echo ================================================
echo Setup complete!
echo ================================================
echo.
echo To start the development server, run:
echo   python manage.py runserver
echo.
echo API will be available at: http://127.0.0.1:8000
echo Admin panel: http://127.0.0.1:8000/admin
echo.
echo To test the API, run:
echo   python test_api.py
echo.
pause
