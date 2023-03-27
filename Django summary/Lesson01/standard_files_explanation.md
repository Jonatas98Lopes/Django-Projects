# Do you understand the functions of each file in a folder of a Django project?

## If your answer is no, do not worry because today I am going to teach you that once for all. 

***

### Before all, open your Django project folder. In it, you will see three icons. They are:

1. A folder with the same name of the folder you are currently are in.

1. A database file called **db.sqlite3**.
**Important:** You will ONLY see this file after running the application for the first with the command:  **_python manager.py runserver_**.

1. And a Python file **manage.py**.

***

### Let us look through all of them.

* The file **manage.py** sets how the application will behave. Normally, we do not edit anything in it. If you really need to change something here, make sure you know exactly what you are doing. Otherwise, the software will not work.

Obs: We use this file to see the application work on our browse. The commands is: **_python manager.py runserver_**.

***

* The file **db.sqlite3** is a database file, as already mentioned. So, it will be crucial when we need to store data on our applications. 

***

### Now, open the folder above them. You'll see some files in it too.

* **_py_cache_** file: This file stores temporary files that are generated when we run our application. No need to modify anything here.

* **__init__.py** file: Since we are working with module, the same rules to mudules apply here. In order that this current folder can be used in other places, we need this file.

* **urls.py** file: It stores the paths for all the pages of a website.

* **asgi.py** file can be used to set the deployment.
##### Deployment is the process to host the project online.

* **wsgi.py** file can be used to set the deployment.

* **settings.py** file is used to set the language of the application, and other functions.

