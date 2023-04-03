# Today, we are going to edit the view of your page through _Bootstrap_.

### What is it? Bootstrap is a set of ready-to-use classes from CSS to add style to your application.

***

* Firstly, we need to access a website to get it. [Click here!](https://getbootstrap.com/)

* We need to choose an option. We are going to the version **v4.6.x** that is a bit more stable.

* Go into templates and in the folder in it.

* Create a HTML file called _base.html_.

* Access [this page](https://getbootstrap.com/docs/4.5/getting-started/introduction/), you will look for the template entitled **Starter template**. The code is like:
```
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

    <!-- Option 2: jQuery, Popper.js, and Bootstrap JS
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>
    -->
  </body>
</html>
```

* Copy it. 

* Paste it on your _base.html_ file.

* We are going to edit the _title_ tag from **Hello, word!** to **Invista-Me!**. 

* We are going to edit a _navbar_. Click [here](https://getbootstrap.com/docs/4.5/components/navbar/) to access the page to copy it. Get the first half of the code entitled _Brand_.
The code is like:
```
<!-- As a link -->
<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
</nav>
```

* Erase the _h1_ tag from your _base.html_ file. Paste this code on its place.

* Change the _a_ tag. It contains the sentence: *Navbar*. Change it to *Invista-Me!*

```
* Add to the _href_ attribute: 
href="{% url 'investimentos' %}"
```
When the user clicks on it, they will be redirected to the initial page.

***

* The last thing to do is to differ the base code to the exclusive code from every page. This is necessary because this page will be ONLY a standard page. The other pages will get his style.

* Below our _nav_ tag, insert the following code:
```
{% block conteudo %}

{% endblock %}
```
The codes from all the other pages will be inserted in the middle of this command.

***

Now, we are going to extend this standard to all the pages we want. Let us start with _investimento.html_. Open this file and put all its code between the following command:
```
{% extends 'invista_me/base.html' %}
{% block conteudo %}

{% endblock %}
```
This must be enough to alteration in its style. Let us make some more modifications.

* Being in this file yet, add the _'table table-striped table-bordered'_ class to our _table_ tag.

***
* On our _Detalhe_ button add the _'btn btn-info'_ class.
* Being in this button, go to _a_ tag, and added the following command:
```
style="color: white;"
```

***
* On our _Editar_ button add the _'btn btn-warning'_ class.
* Being in this button, go to _a_ tag, and added the following command:
```
style="color: white;"
```

***
* On our _Excluir_ button add the _'btn btn-danger'_ class.
* Being in this button, go to _a_ tag, and added the following command:
```
style="color: white;"
```
***

We can centralize our table by putting it in a _div_ tag with the _container_ class. Like:
```
<div class="container">

</div>
```
***

We can align our title by adding the command below in our _h1_ tag, like:

```
style="text-align: center;"
```

***

* Move the _Novo investimento_ button into our div.

* Add _'btn btn-success'_ class into the button.

***

* We can change the color of our *Novo investimento* text color, by accessing the _a_ tag in it, and add the code below: 
```
style="color: white;"
```

***
We can leave gap between the *Novo investimento* button and our table. Like:
```
style="margin-bottom: 30px;"
```

***

Now, we are going to extend the standard of style to _detalhe.html_ file:

* The beginning is the same. Add the following code in this HTML file. This first command on the first line,the second one on the second line, and the third one on the last line:

```
{% extends 'invista_me/base.html' %}
{`% block conteudo %}

{% endblock %}

```
***
* Align the title to the center by the command:
```
style="text-align: center;"
```
***
* Put your table in our _div_ tag to centralize it. Like:

```
<div class="container">

</div>
```

***
We can add a diferent style to our table here too, like:
```
<table class='table table-hover table-bordered'></table>
```

***

Let us edit the page _editar_ now.

* Open the HTMl file called *novo_investimento.html*

***

Here,  we are going to do a bit different. We are going to use Python library to style our HTML file called **crispy-forms**.

* Open your terminal and run the command:
```
pip install crispy-bootstrap5

```
***

* Go into the _settings.py_ file. 

* In the variable _INSTALLED APPS_, add: *'crispy_forms',* and *crispy_bootstrap5*.

* In the same file, look for the variable *STATIC_URL* and bellow, add:
```
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
```
***
* Go again to *novo_investimento.html*.

* Add the following commands:

```
{% extends 'invista_me/base.html' %}
{% block conteudo %}
{% load crispy_forms_tags %}

{% endblock %}
```
Do it like previously. The only difference is the third line that you put it on the third one.

***

* To centralize everything, create a _div_ tag and put all the code there in it, like:
```
<div class="container"></div>
```
***

* Move the title to the superior part there.

* In the part **{{formulario}}**, add it to **{{formulario | crispy}}** to allow crispy to style it.

* Last thing. Add the _"btn btn-success"_ class to the _Salvar_ button.

*** 
Now,  we are going to edit *confirmar_exclusao.html* file

* Add the following command as taught:
```
{% extends 'invista_me/base.html' %}
{% block conteudo %}

{% endblock %}
```

* Edit to a _div class="containter"_,

* Centralize the title.

* Style the button _Cancelar_ like: _class="btn btn-default"_

* Style the button _Cofirmar_ like: _class="btn btn-danger"_


