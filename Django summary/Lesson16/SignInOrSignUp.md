# Now, we are going to teach you how to block or allow users access some pages from your app:

***

To do this, we are going to split the app of the website from the one of login from users.

***

* Go to the main folder of the project.

* Run the command: _python manage.py startapp APPNAME_. In our case, the app name will be 'usuarios'.

You will see that a new Django app has been created.

***

Always when we create a new Django app in our project, we need to add to _settings.py_. File in the main folder of the project.

* Go into _settings.py_.

* Look for the *INSTALLED_APPS*.

* Add the app name at the end of the variable. In our case, _'usuarios'_.

***
We have added the app to our project. What about now?

First we need to think... If we want to control the access to some pages of our project through a signing-in from users, we need to have a page to it.

And if we want to have a page, we need to have a template, a function to render it, and a new path. Let us do all of this. Starting with the template.

* Go into _usuarios_ folder.

* Create a folder called _templates_ and in it, another called _usuarios_.