# How use templates in my Django projects?

***

The first thing we need to do is create the folder where it will be. Let us do it:

* Go to your app Django.

* Create a new folder called _templates_.

* Create a new folder in it called _APPNAME_. It should have the same name of the app.

#### Obs: Of course, you do not need to create the folder names like that, but it is a good practice.

***

* Being there, you can create as many HTML files as you need.

_Example of a HTMl code:_

```
<div>
    <h1>Minha História</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi laboriosam vero consequuntur, corrupti maxime nemo ut temporibus rerum nihil numquam saepe distinctio autem! Voluptas consequatur, eos maxime omnis praesentium ex.</p>
</div>
```

***

## With the page created, it is time to create the function to render it:

* Go to _views.py_ file.

* There, create a function with name you want. **Do not forget to put the parameter _request_**.

* You use the function _render_ to display it on the browser. __As standard, render is imported from the moment you generate the app.__

_Example of the function:_

```
from django.shortcuts import render

def minha_historia(request):
    return render(request, 'invista_me/minha_historia.html')
```
#### Obs: Use the parameter _request_ to render it. The second parameter is the path to the HTML file. You put the name of that second folder created, that one which carries the app name, a slash, and the name of the HTML file.

## The last step is to go to _urls.py_ in the main folder of the project, and add the new path, like below:

```
path('minha_historia/',views.minha_historia', name='minha_historia'),
```

#### Obs: As you can see, path gets three arguments:

* The name of the path you want to display online in the link.
   * Apart from the initial page, try always to add the slash at the end. If you forget to put it, and you access the link with it, an exception will be raised. 

* Second one is the function from the _views.py_ module. This one will display the page, and the third one is the name that will be used later.      