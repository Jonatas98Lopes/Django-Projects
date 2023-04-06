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

First we need to think... If we want to control the access to some pages of our project through a signing-in(up) from users, we need to have a page to it. Let us start with the signing-up.

And if we want to have a page, we need to have a template, a function to render it, and a new path. Let us do all of this. Starting with the template.

* Go into _usuarios_ folder.

* Create a folder called _templates_ and in it, another called _usuarios_.

* Create a new HTML file in it called _registrar.html_.

* Add the code: 

```
{% extends 'invista_me/base.html' %}
{% block conteudo %}
<div class="container">
    <form method="POST">
        {% csrf_token %}
        {{formulario.as_p}}
        <button class='btn btn-primary' type='submit'>Criar novo usuário</button>
        <a href="">Já possui uma conta? Entre aqui</a>
    </form>
</div>
{% endblock %}

```
We are taking advantage of other template styles. That is why we use extends.
We are receiving information from the user, that is why a form tag
We use a security token since we are getting information.
We have a button to send the information,  and the link in case the user already has an account.
***
Now we need to create a new function to render the template.

Go into the _views.py_ file from _usuarios_ app, add the following code:
```
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def novo_usuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(request,f'O usuário {usuario} foi criado com sucesso!')
            return redirect('investimentos')
    formulario = UserCreationForm()
    return render(request, 'usuarios/registrar.html', {'formulario': formulario})

```
To avoid having to validate the user's signing-in data, we use the _UserCreationForm_ to do it.
***

But if we want to send the message to the user in another page. That is the most common since we redirect them to another page. How do we do it?

Go into *base.html* file.

Above the line: **{% block conteudo %}**, add: 
```
{% if messages%}
    {% for message in messages %}
        <div class='alert alert-{{ message.tags }}'>{{ message }}</div>        
    {% endfor%}
{% endif%}
``` 
***

Before we create the new path to it, we need to import the _views.py_ file from our new Django app since all apps have one.

In the first lines of _urls.py_, add:
```
from usuarios import views as usuario_views
```
We assigned to this views file a nickname. This is necessary to avoid confusion between function since we already had a views function imported from *invista_me*.

*** 
Add the new path like this:
```
path('conta/',usuario_views.novo_usuario, name="novo_usuario"),
```
***

But if we want to show more fields to the user fill them?
Easy!

***
* First go to the *usuarios* folder.

* Create a new file there called _forms.py_.

* Add the code:
```
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
```

Now, we are going to create class with the adjusts we need. Always inheriting from UserCreationForm.
```
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField
    class Meta:
        model = User
        fields = ['email','username', 'password1', '    password2'] 
```

***
Edit the form in _views.py_

From UserCreationForm to UserRegisterForm and imported.
```
from .forms import UserRegisterForm
```
***

To finish it, we will just style it.

Change _registrar.html_, like:

```
{% extends 'invista_me/base.html' %}
{% load crispy_forms_tags %}
{% block conteudo %}
<div class="container">
    <form method="POST">
        {% csrf_token %}
        {{formulario | crispy}}
        <button class='btn btn-primary' type='submit'>Criar novo usuário</button>
        <a href="">Já possui uma conta? Entre aqui</a>
    </form>
</div>
{% endblock %}
```