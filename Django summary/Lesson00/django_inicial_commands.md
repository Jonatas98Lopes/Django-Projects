# Starting with Django? Here, it's a summary for you

### Obs: Make sure that Python is already installed and added to path.

***

## How to Install Django?

* **On Windows?**

1. Go to your terminal.

2. Type: **_pip install django_**.

* **On MAC or Linux?**

1. Go to your terminal.

2. Type: **_pip3 install django_**.

### You can make sure Django is installed by typing _Python_ in your terminal, click _Enter_. 

### Now, you have started Python in terminal. Type _import django_ in the first line and click _Enter_. The last command: *django.get_version()*.

### If it returns a number, it is working. Example: **'3.1.2'**

***

## Main Django commands:

### Make sure you're in your terminal.

***

* **django-admin** => To see all Django commands

***

* **django-admin startproject _projectname_** => To start a new Django project.

***

* **python manage.py runserver** => To see the alterations done in a local server. Copy the link and paste it in your browser.

***
* **python manage.py runserver _5000_** => In case you have problems regarding an used gate, switch it like this.

***

## How to start a Django project?

1. Create a folder.

2. You have two options here:

   * You can copy the path of your folder, open your terminal, and use the command: **_cd (path-copied)_**. - **"cd ONLY on Windows"** - **"ls on Linux or MAC"**.

   * Being in the created folder, you can click, with the **right button** of your mouse, and look for the option to open your terminal there.

3. Run the command: **_django-admin startproject projectname_.** - Name **projectname** with name you want. Just make sure to not leave spaces.

* After all of this, you must have another folder in that initial folder created with the name like this: **_projectname_**. In other words, the name you put on that command will be the name of the your project folder.

***

## How to see the alteration I'm doing on my website?

1. Go into the folder of the project. _-The folder created by this command: **django-admin startproject projectname.**_

1. Run the command: _**python manage.py runserver.**_
   
      * If this command presents any problem, it must be because an used gate. Run: _**python manage.py runserver 5000.**_ Choose any gate you want. It doesn't have to be _5000_.
   
1. Copy the _**http://...**_ link that has been generated.
   
1. Paste it on your browser. Here, you'll see every new alteration you do.
   
1. Close the link. Just type: **_ctrl + z_** - on Windows - to finalize it.

### Obs: Upon you do it, you will find, in your project folder, file called _"db.sqlite3"_. This file will be useful for us to save our data later.