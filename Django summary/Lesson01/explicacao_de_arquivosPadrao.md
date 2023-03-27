# Você entende as funções de cada arquivo numa pasta de projeto Django?

## Se a sua resposta for não, não se preocupe porque hoje eu vou ensinar a você de uma vez por todas.

***

### Antes de tudo, abra a sua pasta de projeto Django. Nela, você verá três ícones. São eles:

1. Uma pasta com o mesmo nome da pasta na qual você está atualmente.

1. Um arquivo de banco de dados chamado **db.sqlite3**.
**Importante:** Você verá este arquivo APENAS depois de rodar a aplicação pela primeira vez com o comando: **_python manager.py runserver_**.

1. E um arquivo Python **manage.py**.

***

### Vamos dar uma olhada em todos eles.

* O arquivo **manage.py** configura como a aplicação se comportará. Normalmente, nós não editamos nada nele. Se você realmente precisa mudar algo aqui, certifique-se de que você sabe exatamente o que você está fazendo. Do contrário, o programa não funcionará.
Obs: Nós usamos este arquivo para ver o funcionamento da aplicação no nosso navegador. O comando é: **_python manager.py runserver_**.

***

* O arquivo **db.sqlite3** é um arquivo de banco de dados, como já mencionado. Então, ele será crucial quando nós precisarmos armazenar dados na nossa aplicação. 

***

### Agora, abra a pasta acima deles. Você verá alguns arquivos nela também.

* Arquivo **_py_cache_**: Este arquivo armazena, temporariamente, arquivos que são gerados quando nós rodamos nossa aplicação. Não há necessidade de modificar nada aqui.

* Arquivo **__init__.py**: Uma vez que nós estamos trabalhando com módulos, as mesmas regras para módulos se aplicam aqui. Com o objetivo de que esta pasta atual possa ser usada em outros lugares, nós precisamos deste arquivo.

* Arquivo **urls.py**: Armazena os caminhos para todas as páginas de um site.

* Arquivo **asgi.py** pode ser usado para configurar o **"deployment"**. 
#### Deployment é o processo de hospedar o projeto na internet.

* Arquivo **wsgi.py** pode ser usado para configurar o deployment.

* Arquivo **settings.py** é usado para configurar a língua da aplicação e outras funções.
