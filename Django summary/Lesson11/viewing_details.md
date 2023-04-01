# In this video, we are going to learn how see specific details about a product.

***

We are going to create a dynamic url to access each _investiment_ we have created so far.

***

* Let us start by modifying the initial page like below:

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
            <td><button><a href="{% url 'detalhe' value.id %}">Detalhes</a></button></td>
        </tr>
    {% endfor %}
</table>
```
Here, some things happen.

   * Firstly, we have added a button in the loop for. That means that for each _investiment_ will be generated a new button.
   * Secondly, in the button, we have an _a_ tag. That will be useful for us since we want to redirect the user to the page of details. This page will be specific for each investiment. We have name as _Detalhes_.
   * The _href_ attribute is necessary to send users to another page. Here we put Django syntax **{{% %}}**, we add the word _url_ to refer to a new link, we put the _name_ attribute value informed in one of _urls.py_ paths. The user will be redirected there.
   * Since we want to create an unique url for each investiment, we get the _id_ value to create an unique url.

***

* We need to create the page to redirect the user now, so do it like:

```
<h1>Detalhe do Investimento</h1>
<table>
    <tr>
        <th>Id</th>
        <th>Investimento</th>
        <th>Valor</th>
        <th>Data</th>
        <th>Pago</th>
    </tr>
    <tr>
        <td>{{dados.id}}</td>
        <td>{{dados.investimento}}</td>
        <td>{{dados.valor}}</td>
        <td>{{dados.data}}</td>
        <td>{{dados.pago}}</td>
    </tr>
</table>
```

The _dados_ variable is informed in _views.py_.


* We create the function to render it.

```
def detalhe(request, id_investimento):
    dados = {
        'dados': Investimentos.objects.get(pk=id_investimento) 
    }
    return render(request,'invista_me/detalhe.html',dados)
```

The data that has been returned in the initial page. - _value.id_ is assigned to the parameter *id_investimento*, and we use it to find all the date in the determined line of the table and to create the url like below.
```
path('<int:id_investimento>/',views.detalhe, name='detalhe')
```