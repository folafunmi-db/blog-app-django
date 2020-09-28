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

Upon completing the database model, it's time to create the necessary **views**, **URLs** and **templates**.

## URLs

In order to display the blog posts on the homepage, we first configure project-level URLConfs and then then app-level URLConfs.

- Create urls.py in the blog folder

  > Adding a named URL is optional, however, it is a best practice that should be adopted as it helps keep things organized as the number of URL grows.

- Update the project-level urls.py so that it forwards requests directly to the `blog` app

## Views

Class-based views or Function-based views

## Templates

Templates can be inherited from other templates. Start off with a base.html file and home.html file will inherit from it.

Later when we add templates for creating and editing blog posts, they too can inherit from base.html.

- Create a project-level `templates` directory with two template files: `base.html` & `home.html`
- Update settings.py to include the templates by including `str(BASE_DIR.joinpath('templates'))` in the value list of the 'DIRS' key of the TEMPLATES list.

> Note: object_list comes from ListView and contains all the objects in the view.

## Static files

In a production-ready django project you'd typically store this on a CDN for better performance, but for our purposes local storage will do.

- Create a project-level static folder
- Update settings.py to include the static by including `str(BASE_DIR.joinpath('static'))` in the value list of the 'DIRS' key of the STATICFILES_DIRS list
- Create a CSS dir in the static folder and create a base.css in it
- Add `{% load static %}` to the top of base.html and link base.css as stylesheet

## Individual Blog Pages

Functionality can be added for individual blog pages, how? Create a new **view**, **url** and **template**.

By default, DetailView will provide a context object we can use in our template called either `object` or the lowercased name of our model `post`

> DetailView expects either a primary key or a slug passed to it as the identifier

However, the context object name can be specified in the DetailView class by assigning the `context_object_name` to a string.

The url path is included as `post/<int:pk>/` such that all blog post entries would start with post/ and the primary key for our post entry which will be represented as an integer `<int:pk>`

> Django automatically adds an auto-incrementing primary key to our database models. So, while the only declared fields are `title`, `author` and `body` on the Post model, django has also added another field called `id` which is the primary key(pk). This can either be accessed as 'id' or 'pk'.

Adding a URLConf reference to the a tag is done using the code `{% url ... %}`. The URL is specified to be post_detail which is the name assigned in BlogDetailView in the app-level urls.py.

The post_detail url expects to be passed an argument `pk` representing the primary key for the blog post. Django already provides this as an `pk` or `id` and this is passed into the URLConf as `post.pk`.

## Test

Tests are added to ensure that the Post model works as expected including its representation. And also to test ListView and DetailView.

At the top we import `get_user_model` to reference our active User.
We import TestCase and Client which is used as a dummy web browser for simulating GET AND POST requests on a URL.

>When testing views use `Client()`

In the setUp method, we add a sample blog post to test and confirm its string representation and content are correct.

Then we use `test_post_list_view` to confirm that our homepage returns a 200 STATUS CODE, contains our body text and uses the correct home.html template.

Finally, test_post_detail_view tests that our detail page works as expected and that an incorrect page returns a 404.

>It's always good to test that something does exist and that something incorrect doesn't exist in your test

## Forms

With any user input there are security concerns (XSS), proper error handling is therefore required and there are UI considerations.

Django's built-in Forms abstracts away much of the difficulty and provides a rich set of tools to handle common use cases working with forms.
