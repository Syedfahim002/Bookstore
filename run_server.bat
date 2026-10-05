@echo off
echo ========================================
echo   Online Bookstore - Django
echo   Starting server at http://127.0.0.1:8000
echo   Admin panel at http://127.0.0.1:8000/admin/
echo ========================================
cd /d "%~dp0"
python manage.py runserver
pause