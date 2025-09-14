# Learn Django

This guide walks you through setting up a Django project using Python 3.13 in a virtual environment, including creating a starter project and an app named blog.

## Create a New Directory for Python Environment

**Purpose**: Create and navigate into a folder where your Python virtual environment and Django project will live.

**Tip**: Replace `python3.13` with any meaningful folder name if you're using a different Python version.

```shell
mkdir python3.13 && cd python3.13
```

## Set Up a Python Virtual Environment

Create a new virtual environment in a folder named `venv`

Activates the virtual environment (Linux/macOS)

````shell
python -m venv venv && source source venv/bin/activate
````

## Create a Folder for the Django Project

**Purpose**: This folder will contain your Django project structure.

```shell
mkdir starter
```

## Start a New Django Project

Create a new Django project named app inside the starter directory.

```shell
django-admin startproject core starter
```

## Navigate to the Project Directory

**Purpose**: Change into the starter directory to run project-level management commands.

```shell
cd starter
```

## Create a Django App

**Purpose**: Creates a new app named blog, with its own models, views, and admin logic.

You can later register this app in `app/settings.py` under `INSTALLED_APPS`.

```shell
python manage.py startapp blog
```

## Apply Initial Migrations

**Purpose**: Apply built-in Django database migrations (auth, admin, sessions, etc.).

Ensures your database schema is initialized correctly.

```shell
python manage.py migrate
```

## Create a Superuser

**Purpose**: Create an admin account to log in to the Django admin dashboard.

You will be prompted to enter a username, email, and password.

```shell
python manage.py createsuperuser
```

## Run the Development Server

**Purpose**: Start Django's built-in development server at `http://127.0.0.1:8000/`.

Visit `http://127.0.0.1:8000/admin/` to access the Django admin with your superuser credentials.

```shell
python manage.py runserver
```


## Register
If you want to see all the Python packages installed in your current environment along with their versions, you can run: This file can then be used to replicate the environment elsewhere:
```shell
pip freeze > requirements.txt
```
