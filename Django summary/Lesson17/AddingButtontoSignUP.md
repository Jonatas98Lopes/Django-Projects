# Now, we are going to edit a button to sign in in the initial page.

***

We are going to create  buttons to logIn and logout. How?

* Go into *base.html*. It is in *invista_me* folder.

* Below _a_ tag, add the following code:
```
<nav>
<ul style="list-style: none;">
    <li style="float: left">
        <a href="#" class="nav-item nav-link">LogIn</a>
    </li>
    <li style="float: left"></li>
        <a href="{% url 'novo_usuario' %}" class="nav-item nav-link">Fazer Cadastro</a>
    </li>
</ul>
</nav>
```

The second _li_ tag carries the link to the page of signing up;

***

Now, we are going to make the _LogIn_ button be dynamic.

* Go into _urls.py_ file.

* Being there, import:
```
django.contrib.auth import views as auth_views
```
This command will provide us an already created method to make users sign in.

***

We need to use two functions made by Django that is in *auth_views*, like:

```
path('login/', auth_views.LoginView.as_views(), name="login"),
path('logout/', auth_views.LogoutView.as_views(), name="logout"),
```

This will be necessary to validate the user's data. It wil not render the HTML template we want. It will get in _registration/login.html_.

But we do want to choose the template. That is why we used *.as_views()*. Here we can define the template we want. Like: **.as_views(template_name='usuarios/login.html')**, and for logout, **.as_views(template_name='usuarios/logout.html')**

***

But we do not have these templates what about now?

So, let us create them.

* Go into the templates folder from usuarios folder, and in the folder in it.

* Create both *login.html* and *logout.html*.

* Copy the content from *registrar.html* and paste into them both,like:
```
{% extends 'invista_me/base.html' %}
{% load crispy_forms_tags %}
{% block conteudo %}
<div class="container">
    <form method='POST'>
        {% csrf_token %}
        {% formulario | crispy %}
        <button class="btn btn-primary" type="submit">Criar novo usuário</button>
        <a href="#">Já possui uma conta? Entre aqui</a>
    </form>
</div>
{% endblock %}
```
***
Let us do some things:

```
{% extends 'invista_me/base.html' %}
{% load crispy_forms_tags %}
{% block conteudo %}
<div class="container" style="padding: 30px;">
    <h1>LogIn</h1>
    <form method='POST'>
        {% csrf_token %}
        {% form | crispy %}
        <button class="btn btn-primary" type="submit">Fazer login</button>
        <a href="{% url 'novo_usuario' %}">Ainda não possui uma conta? Cadastre-se aqui</a>
    </form>
</div>
{% endblock %}
```

The form is a ready map in the function LoginView. We do not to create views functon in this case.

We redirect the user to sign up, in case they do not have an account.

***

We also need to alterate the pattern of the functin Loginview. When it receives the user's request, it redirects him to profile page as standard. But we do not have it.

Go into _settings.py_ and add:

```
LOGIN_REDIRECT_URL = 'investimentos'
```

***

Edit as well the page _registrar.html_, like:

```
{% extends 'invista_me/base.html' %}
{% load crispy_forms_tags %}
{% block conteudo %}
<div class="container">
    <form method='POST'>
        {% csrf_token %}
        {% formulario | crispy %}
        <button class="btn btn-primary" type="submit">Criar novo usuário</button>
        <a href="{% url 'login' %}">Já possui uma conta? Entre aqui</a>
    </form>
</div>
{% endblock %}
```

We added the link to _login.html_.

The same we do in _base.html_

```
{% url 'login' %}
```
The same for signing up.

```
{% url 'novo_usuario' %}
```

ADD a title in signing up.

*** 

Let us edit the **logout** page.

Copy the code from _login.html_ and paste it into it.

Edit like:
```
{% extends 'invista_me/base.html' %}
{% load crispy_forms_tags %}
{% block conteudo %}
<div class="container">
    <h1>Você saiu da página!</h1>
    <form method='POST'>
        {% csrf_token %}    
        <a href="{% url 'login' %}">Fazer login novamente</a>
    </form>
</div>
{% endblock %}
```

When someone signs up, they should be redirected to signing in page. Let us do it:

* Go into *usuario_views* file. 
 
* Instead of redirecting the user to initial page, we redirect them to sign in.

```
return render('login')

```

***

We are going to change the button on the right. Even if you are already logged in, it shows the button to sign in or sign up. Let us alterate this.

How?

There is a property in Django to use if the user is logged in. It is: **user.is_authenticated**

Add in _base.html_, like: Add it below _ul_ tag.

```
<ul>
{% if user.is_authenticated%}
    <li style="float: left">
        <a class="nav-item nav-link" href="{% url 'logout'%}">Sair</a>
    </li>
{% else %}
    <li style="float: left">
        <a class="nav-item nav-link" href="{% url 'login'%}">Login</a>
    </li>
    <li style="float: left">
        <a class="nav-item nav-link" href="{% url 'novo_usuario'%}">Fazer Cadastro</a>
    </li>
{% endif%}
</ul>
```
Add new line to display the name of the user. Add the following code right after the if condition, code is:

```
<li>
    <strong class="nav-item nav-link">Bem-vindo {{user.get_username}}</strong>
</li>
```