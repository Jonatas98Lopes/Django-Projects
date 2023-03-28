# Now, we are going to see how to get information on the page and send it to your server.
### We will just simulate the process to send information to the server.

***

To start it, we will create a new page, a page to get information from the user.
How to do it? Do you remember it?

* Go into your Django app folder.

* Go into the folder _templates_ and go into the folder in it.

* Create a new HTML file. In this case, we will call it *novo_investimento.html*
 
* Put the following code in it:

```
<form action="{% url 'investimento_registrado' %}" method="POST">
    {% csrf_token %}
    <label>Tipo de investimento</label>
    <input type="text" name='TipoInvestimento'/>
    <button type="submit">Salvar</button>
</form>

```
#### Obs: A tag _forms_ is used to get the information and send it to a determined local. We inform this local in the atribute _action_. 
#### We use the syntax _{% URL 'LOCALTOSENDINFORMATION' %}_, that is Django syntax. We put the url name in this case, it means we will send the user's data there. The *investimento_registrado* is a name assigned to a path in _urls.py_ that we will create below.
#### {% csrf_token %}. Always, when we get information from the user, we use an authentication token. It is a security function.

Now, we need to create a function to render that.

* Go into _views.py_.

* Create a function called *novo_investimento* like below:
```
def novo_investimento(request):
    return render(request, 'invista_me/novo_investimento.html')
```

***

The last thing to do is to inform _urls.py_ a new path, like below:

```
path('novo_investimento/', views.novo_investimento,name="novo_investimento")
```

***

Normally, when we get some data from the user, there is a button to send the information, and to send the same user to another page. So, we need a new page to redirect them. Let us do it:

* Go into your Django app folder.

* Go into the folder _templates_ and go into the folder in it.

* Create a new HTML file. In this case, we will call it *investimento_registrado.html*

* Put the following code in it:

```
<h1>Você Registrou</h1>
{{tipo_investimento}}
```

***

Now, we need to create a function to render that.

* Go into _views.py_.

* Create a function called *investimento_registrado* like below:

```
def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('TipoInvestimento')
    }
    return render(request, 'invista_me/investimento_registrado.html', investimento)
```
#### Obs: The dictionary _investimento_ is used to get information  that is coming from the other page we have created. The value _POST_ was used in the tag _forms_. That is why we mention it here. The value in get is the _name_ atribute we have put in the _input_ tag from *novo_investimento.html* 
***

The last thing to do is to inform _urls.py_ a new path, like below:

```
path('investimento_registrado/', views.investimento_registrado, name="investimento_registrado")
```