# Django Student Management System

## Project Description

This is a Django-based web application for managing students and departments within an educational institution. The system allows for CRUD (Create, Read, Update, Delete) operations on students and departments.

## Features

- Add, view, edit, and delete students.
- Add, view, edit, and delete departments.
- List students with their associated departments.
- Admin interface for managing students and departments.

## Technologies Used

- Django 5.0.6
- PostgreSQL
- HTML/CSS (for templates)

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Virtualenv (optional but recommended)
- PostgreSQL ( or any database)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AbdullahAbaza/django-student-management-system.git
   cd django-student-management-system
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   Database Configuration first
   The database settings are located in `django_project/settings.py`:

   ```python
       DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.postgresql",
           "NAME": "student_managment_system_db",
           "USER": "postgres",
           "PASSWORD": "YourPassword",
           "HOST": "127.0.0.1",
           "PORT": "5432",
       }
   }

   ```

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   if you incounter any problem regarding the port try another port

   ```bash
   python manage.py runserver 8080
   ```

7. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Admin:**
  - Log in to the admin panel at `http://127.0.0.1:8000/admin/`.
  - Manage students, courses, and grades.
- **Student:**
  - Log in to the student dashboard.
  - View personal academic information and grades.

## Project Structure

- django_project/: Contains the main project settings and configurations.
- students/: Contains the student management app with models, views, forms, and templates.
- templates/: Contains HTML templates for rendering the web pages.

## Static Files

Static files (CSS, JavaScript, Images) are served from the `static/` directory. The URL for static files is configured in `django_project/settings.py`:

```python
STATIC_URL = "static/"

```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Django Documentation
- Bootstrap Documentation

## Contact

For any inquiries or feedback, please contact [your-email@example.com](mailto:your-email@example.com).
