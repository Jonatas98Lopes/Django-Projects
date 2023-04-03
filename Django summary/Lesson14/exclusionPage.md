# How to delete data of a database from a page?

Today, we will do it. We need to redirect the user to an exclusion page from a button in _investimento.html_. So, the first step is to create the button and the HTML file.

* Add a button to the right of every investiment with the command:

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
            <td><button><a href="{% url 'editar' value.id %}">Editar</a></button></td>
            <td><button><a href="{% url 'excluir' value.id %}">Excluir</a></button></td>
        </tr>
    {% endfor %}
</table>
```

* Go into templates folder and in the folder in it.

***

* Create a HTML file called *confirmar_exclusao.html*

***

* In it, insert the code:

```
<form method="POST">
    {% csrf_token %}
    <h1>Confirmar a exclusão {{item.investimento}}</h1>
    <button><a href="{% url 'investimentos' %}">Cancelar</a></button>
    <button type="submit">Confirmar</button>
</form>
```

   * We are going to join the name of the investiment in the title _h1_.
   * We are going to redirect the user to the initial page in case he cancels the exclusion.
   * But if they click on _Confirmar_, we need to exclude the information in the database. That is why we do not redirect the user directly in the _HTML_ file. We will the exclusion operation in _views_ and redirect them there.

***


* Now create the following function in _views.py_:

```
def excluir(request, id_investimento):
    investimento = Investimentos.onjects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request,'invista_me/confirmar_exclusao.html',{'item': investimento} )
```

***

* Create the path now, like:
```
path('confirmarExclusao/<int:id_investimento>', views.excluir, name='excluir'),
```