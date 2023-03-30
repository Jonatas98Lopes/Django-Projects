# How to add, exclude and edit data in our database?

In the last lesson, we created our database structure. Now, we need to add new data. To do this, we will use a system called **Django admin**

***

Before everything, verify if this line is still in your _urls.py_.
```
path('admin/',admin.site.urls),
```
This line comes with the creation of the project as standard, but if you have deleted it, create it now.

***

Let us start:

1. Run your application. Use the command: _python manage.py runserver_

1. Access the link.

1. You can add to end of the url _admin/_ to be redirected to the admin's section.

***

In this url, you will be asked to sign in with your user's account, but you do not have one yet. Let us create it.
   * Make sure you are the main folder of the project.
   * Run: _python manage.py createsuperuser_.
   * You will receive a line to inform your intended user' name and click enter.
   * Inform your email address and click enter.
   * Afterward, insert your intended password and click enter. The user has been created.
   * Run the application again.

***

1. Access the admin's link and access your account with the user who has just been created.

1. You have two options: **Users** and **Groups**. Users are those who can have an account like yours. You can modify them here. Groups will discuss later.

### Okay, so how do I insert new data here?

1. You need to go into the _admin.py_ file. A file in your Django app folder.

1. You will import all the tables you want to apper in our admin's page.
In the example, our table is called **Investimentos** so do it like this.
```
from  django.contrib import admin
from .models import Investimentos

admin.site.register(Investimento)
```
1. Reload the page and it will apper in our admin's page.

1. You will see the name of the tables(s).

1. You have an option _add_. Click it and you can insert new information directly here.

As examples, insert the information below:

1. Example_1:
   * Investimento bar. Insert **Livro**.
   * Valor bar Insert **89**.
   * Pago checkbox bar: Selected
   * DATA bar: Automatically filled.
1. Example_2:
   * Investimento bar. Insert **Carro**.
   * Valor bar Insert **25000**.
   * Pago checkbox bar: Selected
   * DATA bar: Automatically filled.

All done.