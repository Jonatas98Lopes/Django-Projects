# In this lesson, we are going to let the user create new investiments for the time.

***

How will we do it?

We are going to have a new page for the user sign up new investiments.

***

* So let us modify the initial_page called _investimento.html_ by adding a button above the table. A button to redirect the user to a new page, like:

```
<h1>Listagem de Investimentos</h1>
<button><a href="{% url 'novo_investimento' %}">Novo Investimento</a></button>
<table>
    <tr>
        <th>Id</th>
        <th>Investimento</th>
        <th>Valor</th>
    </tr>
    {% for value in data %}
        <tr>
            <td>{{value.id}}</td>
            <td>{{value.investimento}}</td>
            <td>{{value.valor}}</td>
            <td><button><a href="{% url 'detalhe' value.id %}">Detalhes</a></button></td>
        </tr>
    {% endfor %}
</table>

```

 ***

 * In this case, we will edit our old page called *novo_investimento.html* and redirect the user there to create new investiments, like:

 ```
 <form action="" method="POST">
    {% csrf_token %}
    <h1>Formulário Novo Investimento</h1>
    <button type="submit">Salvar</button>
</form>
 ```
Now, we will generate a forms to get the user's information dynamically. That is why we have removed label and input.
Besides, We will not define the action in forms since we are going to be using this page to both create new investiments or edit existent ones.

***

We will remove, in _views.py_ file, the previous *novo_investimento* function and add a new function called _criar_ to work on *novo_investimento* template, like:

```
def criar(request):
    return render(request, 'invista_me/novo_investimento.html')
```

***

As we have removed the *novo_investimento* function, we will edit its path to take advantage of the url *novo_investimento/*, like:

```
path('novo_investimento/', views.criar, name='novo_investimento')
```

Now we are going to create something called _modelforms_ that is form to automate the creation of forms to get user's information:

* Go into the Django app folder.

* Create a file called _forms.py_.

* Inserting the following code:

```
from django.forms import ModelForm
from .models import Investimentos


```
Import all your model tables, and import the first line to use ModelForm.

* Create a class like this: **TABLEIMPORTEDNAME + Form**. It is a good practice.

* This class must inherit from ModelForm

* In it, create a class called _Meta_. Here, we say to Django how we want the form to be created.

* The first _Meta_ class property to be defined is the **model**. **model** is from where the class that is base to this form.

* The second one is the **fields**. What columns from Investimentos should be displayed.

Example: 
```
fields = ['investimentos', 'valor', 'pago']
```
Once we need all of them to be display, do it: _finds = '__all__'_

All the done. Let us just add the form to our function _criar_.

```
from .forms import InvestimentoForm

def criar(request):
    investimento_form = InvestimentoForm()
    formulario = {
       'formulario': investimento_form 
    }
    return render(request, 'invista_me/novo_investimento.html', context=formulario)
```

Edit *novo_investimento.html*, like:

```
 <form action="" method="POST">
    {% csrf_token %}
    <h1>Formulário Novo Investimento</h1>
    {{formulario}}
    <button type="submit">Salvar</button>
</form>
```