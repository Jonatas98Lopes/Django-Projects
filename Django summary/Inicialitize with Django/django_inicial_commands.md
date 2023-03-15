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
* **python manage.py runserver _(5000)_** => In case you have problems regarding an used gate, switch it like this.

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

2. Being there, you have two options:

   * Run the command: _**python manage.py runserver.**_
   
      * If this command presents any problem, it must be because an used gate. Run: _**python manage.py runserver (5000).**_ Choose any gate you want. It doesn't have to be _5000_.
   
   * Copy the _**http://...**_ link that has been generated.
   
   * Paste it on your browser. Here, you'll see every new alteration you do.
   
4. Close the link. Just type: **_ctrl + z_** - on Windows - to finalize it.