# What are paths in Django?

Paths are the ways to go into pages. When we access a new page in a website, we either type the variation of the link directly in the browser bar or we are redirected by a button that we pressed.

## How can we add, edit or exclude paths?

Through the file _urls.py_ located in the main folder of the project. As standard, it comes with an _admin_ extension. If we add _admin/_ at the end of the link, we are redirected to this page. We do not have an inicial page at first. We need to add it here.

## How do we create our initial page?

* First, we need to import the _views.py_ file from the app we want to run that page. Import it into _urls.py_. This file is responsible for returning an answer for the user when they request a page.
   * If we just want to display a simple text when the user asks, we can go to that _views.py_ file and import the function _HttpResponse_ with the command: _from django.shortcuts import HttpResponse_.
* Now that we have imported the function we need, we can create a function to render something on the screen when the user requests information. In Django, each function will be responsible for each page basically.

_Example:_
```
def initial_page(request):
    return HttpResponse("Hi, I'm the initial page.")
```
##### Obs: Request is a good practice variable. It receives all the input data.

* Now, we need to inform _urls.py_ file that we have a function to render a message, and create an extension path to access it. Once it is the initial page, we do not add anything in the path and do not leave spaces.

_Example_:
```
path('',views.pagina_inicial)
```
## How would I create a page called _Contact_?

* We would go back to _views.py_.

* Another function, like:
```
def contact(request):
    return HttpResponse('Get in touch with Albert Einstein')
```

* Go back to _urls.py_.

* Create a new path and call the function we have just created, like:

```
path('contact', views.contact, name='contact')
```
#### Obs: name will be useful later. 

