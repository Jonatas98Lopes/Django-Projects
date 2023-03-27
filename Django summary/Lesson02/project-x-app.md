# Now, we are going to understand the difference between a Django project and a Django app.

***

As seen before, we create a Django project by using the command: _django-admin startproject PROJECTNAME_. So the question is **what a Django project really is**. To understand it, imagine you are developing an investiment software. We could have different sections.

***

_Example:_

* We could have a section that manages your investiments.
* Another one for finding new ones.
* The part to control signing-in or signing-up of users.

Basically, they are all Django apps separetely, but the Django project is the whole thing. The folder that was generated with that command: (_django-admin startproject PROJECTNAME_). 

When you go into this folder, you have another folder with the same name in it. This folder contains the files for the general settings from the whole project, but to have an app, we need to run another command.
#### Obs: You can create as many apps as you need. All depends on your necessity.

# How to create an app with Django?

1. You need to find the folder of the Django project.

1. Go into it.

1. Open your terminal there.

1. Run the code: _python manage.py startapp APPNAME_. You put the name of **APPNAME** as you wish.

***

After running the command above, you must be able to see another folder in the directory of the project.

## Let's have a look at the files there:

* Open *APPNAME*. You must have the following files:
   
  * **migrations** folder: It deals with the database of the project.
   * **__init__.py** file: It is necessary because call the app folder in others folders, so the principle module is used here.
   * **admin.py** file: ---
   * **apps.py** file: Here, we define which other applications will be related to it.
   * **models.py** file: It will store the code that represents a database table.
   * **tests.py** file: It is used to create unit tests. If you want to carry out multiple tests in your app suddenly, here is the place to do so.
   * **views.py** file: Here, you create functions that represent pages in a website. Each of them represents a different page. Normally, they point to a template made in HTML. We are going to discuss this later.

## First step when you have created a new app:

* Go into the main folder of the project and open _settings.py_.
* Look for the variable *INSTALLED_APPS*.
* In its end, add a comma and write the *APPNAME* here. It is important so that Django indetifies each new app in the project.

### Optional: In case you are in Brazil and want the website to run in Portuguese, you can do this:

* Go to the end of the file _settings.py_.
* Look for the variable: *LANGUAGE_CODE*.
* As standard, it comes with the value _en-us_, but you can put _pt-br_.
* Look for the variable: *TIME_ZONE*.
* As standard, it comes with the value _UTC_, but you can change it to *America/Sao_Paulo* if you are in São Paulo.