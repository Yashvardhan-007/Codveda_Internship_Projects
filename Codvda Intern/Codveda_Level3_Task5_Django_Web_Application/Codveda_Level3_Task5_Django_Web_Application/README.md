# Codveda Level 3 - Task 5: Django Web Application

A security-conscious Django web application demonstrating user registration,
authentication, logout, password validation, password reset, protected
dashboard access, and staff-aware navigation.

## Internship Requirement

The Codveda Level 3 Django task requires a web application with features
including user registration, login/logout, password security, password reset,
and role-based permissions.

This project implements those requirements using Django's built-in
authentication framework.

## Features

- User registration
- Login/logout
- Django password hashing and validators
- Login-protected dashboard
- Staff/admin-aware navigation
- Password reset workflow
- CSRF protection
- Session-based authentication
- SQLite database
- Responsive UI
- Django admin
- Automated Django tests

## Technology Stack

- Python 3
- Django 5.x
- SQLite
- HTML/CSS
- Django Authentication Framework

## Project Structure

```text
Codveda_Level3_Task5_Django_Web_Application/
├── manage.py
├── requirements.txt
├── secure_portal/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── forms.py
│   ├── models.py
│   ├── admin.py
│   ├── apps.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── migrations/
├── templates/
│   ├── base.html
│   ├── portal/
│   └── registration/
├── static/css/style.css
└── README.md
```

## Installation - Windows / VS Code

Open the project folder in VS Code.

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run Python directly from the
environment or use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

Install Django:

```powershell
pip install -r requirements.txt
```

## Initialize Database

Run:

```powershell
python manage.py migrate
```

Create an administrator:

```powershell
python manage.py createsuperuser
```

Follow the prompts.

## Start the Server

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin:

```text
http://127.0.0.1:8000/admin/
```

## Test the Application

### Registration

Open:

```text
/accounts/signup/
```

Create a user account.

### Login

Open:

```text
/accounts/login/
```

### Protected Dashboard

Open:

```text
/dashboard/
```

Unauthenticated users are redirected to the login page.

### Password Reset

Open:

```text
/accounts/password_reset/
```

For local development, Django's default email backend can be configured
to print reset messages to the terminal if needed.

## Security Concepts Demonstrated

- Password hashing through Django's authentication framework
- Password validation
- CSRF protection
- Session authentication
- Login-required authorization
- Staff/admin role distinction
- Secure form handling
- No plaintext password storage

## Important Development Note

The included `SECRET_KEY` is a development placeholder. For production,
move secrets into environment variables and set `DEBUG = False`.

This project is intended for learning and portfolio development, not direct
production deployment without additional hardening.

## Learning Outcomes

This project develops:

- Django project structure
- URL routing
- Views
- Templates
- Forms
- Authentication
- Authorization
- Password security
- Sessions
- Database migrations
- Admin interface
- Static files
- Web application security fundamentals

## Future Enhancements

- Custom user profile model
- Role/permission management UI
- Email verification
- PostgreSQL
- REST API using Django REST Framework
- Audit logging
- Rate limiting
- Two-factor authentication
- Security event dashboard
- Docker deployment
- Automated CI/CD

## Author

**Yashvardhan Singh**

Python Development Intern
Codveda Technologies
