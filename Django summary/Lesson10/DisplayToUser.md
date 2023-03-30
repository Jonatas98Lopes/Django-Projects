# How to display database data to users?

***

We need to create a new page. I suppose you already know how to do it.

***

* Go into your Django app folder.

***

* Go into the _templates_ folder and go into the folder in it too.

***

* Create a new HTML file as our new page, like:

```
<h1>Listagem de Investimentos</h1>
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
        </tr>
    {% endfor %}
</table>
```
   * This information will be our data from the database.
   * Here, we have some columns from our database, only those that we need.
***

* Go to your _views.py_ file and create a function to render it, like:

```
from .models import Investimentos
def investimentos(request):
    dados = {
        'data': Investimentos.object.all()
    }
    return render(request, 'invista_me/investimentos.html', context=dados)
```
   * Notice that we have imported our _Investimentos_ table from the database.
   * We are bringing all the data in the database to our page.

***

* Inform a new url in _urls.py_ file, like:
In this case, we are going to alterate the initial page, like
```
path('', views.investimentos),
```