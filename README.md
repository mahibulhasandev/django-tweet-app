# Django Tweet App

A simple Tweet application built with Django and Bootstrap. Users can create tweets with text and images, view tweets in a responsive card layout, and manage their accounts through authentication.

## Features

- User registration and login
- User logout
- Create tweets with text and photos
- Display tweets in a responsive grid layout
- Four tweet cards per row on large screens
- Edit and delete tweets
- Bootstrap 5 responsive navigation bar
- Django template inheritance
- CSRF protection for form submissions

## Technologies Used

- Python
- Django
- HTML5
- Bootstrap 5
- SQLite
- Django Template Language

## Project Structure

```text
config/
├── config/
│   ├── settings.py
│   └── urls.py
├── tweet/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── media/
├── templates/
│   ├── layout.html
│   └── registration/
├── manage.py
└── README.md
```

*The structure may vary depending on your project configuration.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-project-directory>
```

### 2. Create a Virtual Environment

Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Django

```bash
pip install django
```

If your project uses additional packages, install them as well.

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/tweet/
```

## Learning Goals

This project helps me practice:

- Django models, views, and URL routing
- ModelForm and form validation
- User authentication and registration
- File uploads and media handling
- Django template inheritance
- Bootstrap layout and responsive design
- CRUD operations

## Future Improvements

- Add tweet search functionality
- Add pagination
- Display usernames on tweets
- Add likes and comments
- Improve the user profile system
- Deploy the application online

## Author

**Mahibul Hasan**

CST Diploma Student | Learning Full-Stack Web Development

---

This project is built for learning and practicing Django web development.
