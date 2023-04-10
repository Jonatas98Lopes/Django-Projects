# Today,  we are going to host our project online and create a database online.

***

We are going to the hostage place from Railway.

***
* [Access the website here!](https://railway.app)

* Create an account

We are going to the user the trial version. We can use the Usage one and it will keep being for free unless you use more than 5GB from the server storage.  

* Having the project on GitHub and logged in with the Stater plan. Let move on.

* Being in  the initial page -[Click!](https://railway.app/dashboard).

* Create Provision PostgreSQL.

* Click on it.

* We are going to user the requirement.txt file informed in the lesson

* Open the requirements file.

* Replace the line: _psycopg2==2.9.1_ with _psycopg2-binary_.

***
We are going to change some things  in _settings.py_ now.

* Go into it.

* Look for _databases_. We need to fill it with information we have in our online database. How?

* Be logged in. Access the folder of your online database.

* Find it in your current project.

* Click on it and go to VARIABLES.

* There, you will see the following pieces of information: *DATABASE_URL*, *PGDATABASE*, *PGHOST*, *PGPASSWORD*, *PGPORT*, AND *PGUSER*.

    * Your variable is like that:
```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```
    * You replace the information in ENGINE with: django.db.backends.postgresql_psycopg2
    * You replace the information in NAME with the  PGDATABASE.
    * Add PGHOST like: 'HOST': 'PGHOSTINFORMATION HERE'
    * Add PGPASSWORD like: 'PASSWORD': 'PGPASSWORDINFORMATION HERE'
    * Add PGPORT like: 'PORT': 'PGPORTINFORMATION HERE'
    * Add PGUSER like: 'USER': 'PGUSERINFORMATION HERE'

***

* After doing this run the command: _python manage.py migrate_ to send the information to our online database.

* Being in usuarios folder. Create a fila called _Procfile_ and in it, add: web: gunicorn projeto_invista_me.wsgi 

Obs: Remember that projeto_invista_me is name of our Django project. After it, we are using a dot and a wsgi. It means that we are using the _wsgi.py_ file.

***

* Go back into _settings.py_ and look for: *static_root*.

* Erase it. 

* In its place, add this to line:

```
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

* Run the command: _python manage.py collectstatic_. This will be useful for running static files.

***

* Look for: *allowed_hosts*. Replace the information in this variable with '*'.
***
With all this done. We will use the _requirements.txt_ file now. This file contains all the Python libraries demanded for our project.

Okay? But why do we need it? Simply, because we are going to create virtual environment to install all this library separatedly. This is a good practice. By doing this, we reduce the size of the project to host online.

*** 

* Create a virtual environment and activate it now.

* With it installed and activated, run: pip install -r .\requirements.txt. All libraries will be installed.

* We are going to include the name of our virtual environment in the _.gitignore_ file. 
    * Open it.
    Add: .nameofenvironment/ \n nameofenvironment/

* Update GitHub with the alteration we have done.

* Get name of the repository.

* Being in the folder of your project. Click on new.

* CLick on GitHub Repo

* Choose your repository. Make sure you are logged in with a GitHub account.

* Go into settings. Settings from your GitHub project.

* Click on generate Domain

* It is possible that the deployment takes around 10 mins. So wait it up.


* The last thing. Go into _settings.py_ from your Django project.

* Look for the variable: *ALLOWED_HOSTS*.

* In it, add the domain generated to make it safer.