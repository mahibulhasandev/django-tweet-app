# Django Tweet Project

A simple web application built with Django as part of my journey to learning full-stack web development.

## About the Project

This project is created to practice Django fundamentals, understand project structure, work with URL routing, views, templates, and learn how to build web applications using Python and Django.

## Built With

- **Python** — Programming language
- **Django** — Web framework
- **HTML** — Web page structure
- **SQLite** — Development database
- **Git & GitHub** — Version control

## Project Structure

```text
config/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── tweet/
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
├── manage.py
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mahibulhasandev/first-django-project.git
cd first-django-project
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Linux:

```bash
source .venv/bin/activate
```

### 3. Install Django

```bash
python -m pip install django
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

http://127.0.0.1:8000/

## What I'm Learning

- Django project and app structure
- URL routing and views
- Templates and HTML integration
- Models and database migrations
- Django admin panel
- Git and GitHub workflow

## Future Improvements

- Add more features to the application
- Improve the user interface
- Learn Django forms and authentication
- Explore Django REST Framework

## Author

**Mahibul Hasan**

- GitHub: [@mahibulhasandev](https://github.com/mahibulhasandev)

---

*Learning step by step, building projects, and improving my development skills.*
