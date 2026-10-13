# Django Fast Track — Learning Project

A hands-on Django project built while learning Python web development. The goal is to understand Django concepts by implementing and testing real features.

## Tech Stack
- Python
- Django
- SQLite
- HTML
- Git and GitHub

## Learning Progress

### Lesson 1: Project Setup
- Created a Django project and `tasks` app.
- Configured settings and URLs.
- Set up the virtual environment.

### Lesson 2: Models and Database
- Created the `Task` model.
- Learned model fields and database migrations.
- Registered the model in Django Admin.

### Lesson 3: Views, URLs and Templates
- Connected URLs to views.
- Rendered HTML templates.
- Retrieved tasks from the database and displayed them.

### Lesson 4: Create and Delete Tasks
- Created tasks using an HTML form.
- Deleted tasks using POST requests.
- Used redirects after form submissions.

### Lesson 5: ModelForm and Edit Tasks
- Created a Django `ModelForm`.
- Displayed existing task values in a form.
- Validated and saved updates to an existing task.

### Lesson 6: Mark Tasks as Complete
- Added a view and URL for completing tasks.
- Updated the task's completion status.
- Added a completion button to the homepage.

## Current Project Features
- View tasks
- Create tasks
- Edit tasks
- Delete tasks
- Mark tasks as complete
- Manage tasks through Django Admin

## How to Run Locally
1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install Django.
4. Run migrations.
5. Start the development server.

Commands:

```bash
python -m pip install django
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Next Learning Goals
- User authentication
- Django ORM relationships
- Django REST Framework
- Automated testing
- Deployment

## Note
This is a learning project. Features are added and tested incrementally as part of my Django learning journey.