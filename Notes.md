# Notes

## Setup

- Create a new directory
- Install django in a new virtual env using the command `pipenv install django`
- Activate the virtual env using `pipenv shell`
- Create a new Django project using the command `django-admin startproject {project_name=blog_project} .`
- Create new app called `blog` using the command `python manage.py startapp {app_name=blog}`
- Perform a migration to setup the database using the command `python manage.py migrate`
- Update settings.py to include the blog app

## Database models

ForeignKey allows for many-to-one relationship such that the user can be the author of many different blog posts but not the other way around. Using `ForeignKey` the `on_delete` needs to be defined.

Create a migration record for the database model and migrate the change in the database. This is done using the commands:

> `python manage.py makemigrations blog`

Then,

> `python manage.py migrate blog`

## Admin

- Create an admin using the command `python manage.py createsuperuser`
- Register the new model in admin.py

Upon completing the database model, it's time to create the necessary views, URLs and templates.

## URLs
