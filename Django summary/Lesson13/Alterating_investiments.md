# Today,  we are going to edit the investiments.

We would like to take advantage of the page edited last lesson, *novo_investimento.html*. We would like to use this template to see the existent information there, or to edit using it.

***

* First, let us create a new button. Each investiment must have a button to edit it. The button added is the _Editar_ one. 

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
            <td><button><a href="{% url 'editar' value.id %}"></a>Editar</button></td>
        </tr>
    {% endfor %}
</table>
```
We want to create a new url using the id property. That is why we inform "{% url 'detalhe' value.id %}"

***

* Second is to create the function to render it.

```
def editar(request, id_investimento):
    investimento = Investimentos.objects.get(pk=id_investimento)
    if request.method == 'GET':
       formulario = InvestimentoForm(instance=investimento)
       form = {
           'formulario': formulario
       }
       return render(request, 'invista_me/novo_investimento.html', form)
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()   
        return redirect('investimentos')

```
Every page that we show information and receive information, we need to use request.POST and request.GET.
When the user accesses the page, he will have all the information there filled. This is done in the if block. instance is used to avoid creating a new investiment.
In case, they edit something, the information will be checked, saved and the user will be redirected.

***

* The last thing to do is create the path. 

```
path('novo_investimento/<int:id_investimento>', views.editar, name="editar"),
```