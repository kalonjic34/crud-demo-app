# Django CRUD Demo Application

This is a basic CRUD (Create, Read, Update, Delete) demo application built with Django. The project demonstrates how to manage simple tasks and user authentication using Django's built-in features.

## Features

- **Task Management**
  - Create new tasks
  - View a list of all tasks
  - Update existing tasks
  - Delete tasks

- **User Authentication**
  - User registration
  - User login
  - Dashboard for logged-in users

- **Simple UI**
  - HTML templates for all major views
  - Basic navigation and layout

## Project Structure

```
demo/
├── crm/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── crm/
│           ├── base.html
│           ├── create-task.html
│           ├── dashboard.html
│           ├── delete-task.html
│           ├── index.html
│           ├── my-login.html
│           ├── register.html
│           ├── update-task.html
│           └── view-tasks.html
├── demo/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   ├── css/
│   ├── images/
│   └── js/
└── manage.py
```

## How It Works

- **Models:**  
  - `Task`: Represents a task with a title, description, and creation date.
  - `Review`: (Optional) Linked to tasks for future extension.

- **Forms:**  
  - `TaskForm`: For creating and updating tasks.
  - `CreateUserForm`: For user registration.
  - `LoginForm`: For user login.

- **Views:**  
  - CRUD operations for tasks (`create_task`, `tasks`, `update_task`, `delete_task`)
  - User registration and login (`register`, `my_login`)
  - Dashboard and homepage

- **Templates:**  
  - Each view has a corresponding HTML template for rendering forms and data.

## Setup Instructions

1. **Clone the repository**

2. **Install dependencies**
   ```sh
   pip install django
   ```

3. **Apply migrations**
   ```sh
   python manage.py migrate
   ```

4. **Run the development server**
   ```sh
   python manage.py runserver
   ```

5. **Access the app**
   - Open [http://localhost:8000/](http://localhost:8000/) in your browser.

## Notes

- Static files (CSS, JS, images) are located in the `static/` directory.
- The app uses SQLite by default.
- This project is for learning/demo purposes and is not production-ready.

---

