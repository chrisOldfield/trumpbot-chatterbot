# Install packages


Install with pip

 `pip install django chatterbot`

For more details on installing Django, see the `Django documentation`

# Installed Apps


Add `chatterbot.ext.django_chatterbot` to your `INSTALLED_APPS`

```python

   INSTALLED_APPS = (
       # ...
       'chatterbot.ext.django_chatterbot',
   )
```

# API view


If you need a ChatterBot API endpoint you will want to add the following to your urls.py

```python

   urlpatterns = patterns(
       ...
       url(r'^chatterbot/', include('chatterbot.ext.django_chatterbot.urls', namespace='chatterbot')),
   )
```

# Migrations


   `python manage.py migrate django_chatterbot`



Looking for a working example? Check our the example Django app using
ChatterBot on GitHub: [Django Example](https://github.com/gunthercox/ChatterBot/tree/master/examples/django_app)

# MongoDB and Django


ChatterBot has a storage adapter for MongoDB but it does not work with Django.
If you want to use MongoDB as your database for Django and your chat bot then
you will need to install a **Django storage backend** such as `Django MongoDB Engine`

The reason this is required is because Django's storage backends are different
and completely separate from ChatterBot's storage adapters.

[Django documentation](https://docs.djangoproject.com/en/dev/intro/install/)
[Django MongoDB Engine](https://django-mongodb-engine.readthedocs.io/)