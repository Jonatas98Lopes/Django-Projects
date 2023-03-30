# Iniciando com Django? Aqui vai um resumo para você.

### Obs: Certifique-se de que o Python já está instalado e você selecionou a opção _add to PATH_ na hora da instalação.

***

## Como instalar o Django?

* **No Windows?**

1. Vá para o seu terminal.

2. Digite: **_pip install django_**.

* **No MAC ou Linux?**

1. Vá para o seu terminal.

2. Digite: **_pip3 install django_**.

***

## Principais comandos do Django:

### Certifique-se de que você está no seu terminal.

***

* **django-admin** => Para ver todos os comandos do Django.

***

* **django-admin startproject _nomedoprojeto_** => Para começar um novo projeto Django.

***

* **python manage.py runserver** => Para ver as alterações feitas num servidor local. Copie o link e cole-o no seu navegador.

***
* **python manage.py runserver _(5000)_** => No caso de você ter problemas com relação a uma porta usada, troque a porta assim.

***

## Como começar um projeto Django?

1. Crie uma pasta.

2. Você tem duas opções aqui:

   * Você pode copiar o caminho da sua pasta, abrir o seu terminal, e usar o comando: **_cd (caminho-copiado)_**. - **"cd APENAS no Windows"** - **"ls no Linux ou MAC"**.

   * Quando você estiver na pasta criada, você pode clicar, com **o botão direito** do seu mouse, e procurar pela opção de abrir o seu terminal lá.

3. Execute o comando: **_django-admin startproject nomedoprojeto_.** - Defina o **nomedoprojeto** como desejar. Apenas tenha certeza de não deixar espaços.

* Depois de tudo isto, você deve ter outra pasta dentro daquela pasta inicial criada com o nome assim: **_nomedoprojeto_**. Ou seja, o nome que você colocar naquele comando será o nome da sua pasta de projeto.

***

## Como ver as alterações que eu estou fazendo no meu site?

1. Entre na pasta do projeto. _- A pasta criada com este comando: **django-admin startproject nomedoprojeto.**_

2. Estando lá:

   * Execute o comando: _**python manage.py runserver.**_
   
      * Se este comando apresentar qualquer problema, deve ser por causa de uma porta usada. Execute: _**python manage.py runserver (5000).**_ Escolha qualquer porta que desejar. Não tem que ser _5000_.
   
   * Copie o link _**http://...**_ que foi gerado.
   
   * Cole-o no seu navegador. Aqui, você verá toda nova alteração que você fizer.
   
4. Feche o link. Apenas digite: **_ctrl + c_** - no Windows - para finalizá-lo.
   

