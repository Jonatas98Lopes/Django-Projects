# Do you understand the functions of each file in a folder of a Django project?

## If your answer is no, do not worry because today we are going to teach you that once for all. 

***

### Before all, open your project folder with Django. In it, you will see three icons. They are:

1. A folder with the same name of the folder you are currently are in.

1. A database file called **db.sqlite3**.

1. And a Python file **manage.py**.

***

### Let us look through all of them.

* The file **manage.py** sets how the application will behave. Normally, we do not edit anything in it. If you really need to change something here, make sure you know exactly you are doing. Otherwise, the software will not work.

Obs: This file we use to see the application work on our browse. The commands is: **_python manager.py runserver_**.
***

* The file **db.sqlite3** is a database file, as already mentioned. So, it will be crucial when we need to store data on our applications.
***

### Now, open the folder above them. You'll see some files in it too.

* **_py_cache_** fie: This file stores temporary files that are generated when we run our application. No need to modify anything.

* **__init__.py** file: Since we are working with module, the same rules to mudules apply here. In order that these current folder can be used in other places, we need this file.

* **asgi.py** file can be used to set the deployment.
##### Deployment is the process to host the project online.

* **wsgi.py** file can be used to set the deployment.

* **settings.py** used to set the language of the application, other functions and so on.

