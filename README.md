# 📚 Online Bookstore (Django)

A complete CRUD web application built with **Python + Django + Django REST Framework**.
This is a self-built demo project for showing skills to recruiters/companies.

## ✨ Features

- ✅ **Create / Read / Update / Delete** books (full CRUD)
- ✅ **Category** relation (ForeignKey) with filter by category
- ✅ **Search** by title / author
- ✅ **Cover image** upload (Pillow)
- ✅ **Admin panel** to manage everything
- ✅ **REST API** (`/api/books/`) ready to connect with a Flutter app later

## 📁 Project structure

```
config/              # project settings & URLs
bookstore/           # main app
├── models.py        # Category, Book
├── views.py         # CRUD + filter + search
├── forms.py
├── serializers.py   # REST API
├── api.py           # DRF viewset
└── templates/bookstore/  # HTML templates
seed.py              # adds demo books/categories
manage.py
```

## 🚀 How to run

```bash
pip install django djangorestframework django-cors-headers pillow
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Or just double-click **`run_server.bat`**.

Then open:
- Website: http://127.0.0.1:8000
- Admin: http://127.0.0.1:8000/admin
- API: http://127.0.0.1:8000/api/books/
- REST browseable: http://127.0.0.1:8000/api/books/1/

## 🌱 Seed demo data (optional)

```bash
python manage.py shell -c "exec(open('seed.py', encoding='utf-8').read())"
```

## 🔑 Admin login (created for demo)

- **Username:** admin
- **Password:** admin12345

*Change it before showing anywhere public!*

## 🧪 Running the check

```bash
python manage.py check
```

## 🎯 Next step (Flutter)

The `/api/books/` endpoint is CORS-enabled and ready. Build a Flutter app that
fetches books from this API and you'll have a full-stack (Django + Flutter) project!