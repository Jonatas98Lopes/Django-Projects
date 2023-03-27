# O que são caminhos no Django?

Caminhos são formas de entrar em páginas. Quando nós acessamos uma nova página num site, nós digitamos a variação do link diretamente na barra do navegador ou nós somos redirecionados por um botão que nós pressionamos.

## Como nós adicionamos, editamos ou excluímos caminhos?

Através do arquivo _urls.py_ localizado na pasta principal do projeto. Por padrão, ele vem com uma extensão _admin_. Se nós adicionarmos _admin/_ no final do link, nós somos redirecionados para esta página. Nós não temos uma página inicial de primeira. Nós precisamos adicioná-la aqui.

## Como nós criamos nossa página inicial?

* Primeiro, nós precisamos importar o arquivo _views.py_ do app que queremos rodar nessa página. O arquivo é responsável por devolver uma resposta para o usuário quando ele requesitar uma página.
   * Se nós apenas quisermos exibir um texto simples quando o usuário pedir, nós podemos ir para aquele arquivo  _views.py_ e importar a função  _HttpResponse_ com o comando: _from django.shortcuts import HttpResponse_.
* Agora que nós importamos a função que precisamos, nós podemos criar uma função para renderizar algo na tela quando o usuário requesitar informação. No Django, cada função será responsável por cada página basicamente.

_Exemplo:_
```
def pagina_inicial(request):
    return HttpResponse("Olá, eu sou a página inicial.")
```
##### Obs: Request é uma varíavel de boa prática. Ela recebe todos os dados de entrada.

* Agora, nós precisamos informar o arquivo _urls.py_ que nós temos uma função para renderizar uma mensagem e criar uma caminho de extensão para acessá-la. Uma vez que é a nossa página inicial. nós não precisamos adicionar nada no caminho e não deixe espaços.

_Exemplo_:

```
path('',views.pagina_inicial)
```

## Como eu criaria uma página chamada _Contato_?

* Nós voltaríamos para _views.py_.

* Outra função, como:

```
def contato(request):
    return HttpResponse('Entre em contato com Albert Einstein')
```

* Volte para _urls.py_.

* Crie um novo caminho e chame a função que nós acabamos de criar, como:

```
path('contato', views.contato, name='contato')
```
#### Obs: A propriedade _name_ será útil mais tarde. 

