# Today, we are going to creata a database table using "Migrations".

### Introduction

***

As it was mentioned before, the _models.py_ file only creates the model of the table, but to create the database, we need to use the _migrations_ folder.

***

In this lesson, we are going to use the _db.sqlite3_ file and it will be necessary to see tha data in it too. However, we can't open this file without an apropriate software. To resolve this, you can download _DB Browser(SQLite)_ in your computer and open this file with it. Identify your operating system version, and download it. Link below:
[Download the software here!](https://sqlitebrowser.org/dl/)

***

You can open the software now, find the _db.sqlite3_ file through it. Open it and you will see there is nothing in this database file.

***

### How to transfer the model created in _models.py_ to the _db.sqlite3_?

1. Close your application if it is opened. You can type _ctrl + c_, on Windows, in your terminal.

1. Make sure you are the main folder of the project. The folder that contains the _manage.py_ file.

1. Run: _python manage.py makemigrations_. This will prepare the migrations to be transfered.

***

You can make sure the operation has been done succesfully by open the _migrations_ folder in your Django app folder and you will see an initial file called: *0001_initial.py*.

If you open the file, you will see a code that transfers the data to our _db.sqlite3_ automatically. Usually, we do not alterate anything here. **NEVER EXCLUDE A _MIGRATIONS_ FILE**

***

### Possible problems:

* If the _python manage.py makemigrations_ command does not work, it is possible you have not added the app to the project. **HAVE A LOOK AT _LESSON02_**

* In case you have more than one app, you will not be enough to run _python manage.py makemigrations_ since Django can get confused among the apps you have. In this case run:  _python manage.py makemigrations APPNAME_. Specify the name of the app and run it.

1. To transfer all that we have done to the database file, run: _python manage.py migrate_. **MAKE SURE YOU ARE IN THE MAIN FOLDER OF THE PROJECT.**

***

After this, all migrations will be applied. You can open _DB Browser(SQLite)_, open _db.sqlite3_ in it to see if everything has been created properly. If you see many tables upon opening _db.sqlite3_, in the _Database structure_ bar, it means everything has gone well. The table we have created through **MIGRATIONS** commands is the one with the following structure: **APPNAME_TABLENAME**. The app name is the name of the app we have created. The table name is the of the class defined in _models.py_.

*** 
Always when you update something in models, do this again.

**TO SEE ALL THE SQL COMMANDS, RUN: _python manage.py sqlmigrate APPNAME MIGRATIONNAME_. YOU WILL SEE THE COMMANDS IN YOUR TERMINAL.**