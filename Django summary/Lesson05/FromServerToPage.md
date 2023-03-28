# Today, we are going to see how to send data from your server to your page. Dynamic data.
#### Obs: We will be simulating the process. We will not use database functions yet.

***
## Here, are the steps:

* Go into _views.py_ file. A file from a Django app.

* Edit the function from the last lesson like below:
```
def minha_historia(request):
    pessoa = {
        'name': 'Bob',
        'age': 32,
        'hobby': 'Games'
    }
    return render(request, 'invista_me/minha_historia.html', pessoa)
```
#### Obs: As you can see, we have added a map called _pessoa_ with some information in it. Here, we are simulating data from a server. In conclusion, create a dictionary like this, and inform its name as the third argument of the function _render_.

* Now, edit the HTML file *minha_historia.html* like below:
```
<div>
    <h1>Minha História</h1>
    <h4>{{name}}</h4>
    <h4>{{age}}</h4>
    <h4>{{hobby}}</h4>
</div>
```
#### Obs: What have we done? Once _pessoa_ is the third argument in the _render_ of our *minha_historia* function, we can access the values of its keys with the syntax _{{NAMEOFTHEKEY }}_.

Once we have defined the path to the this page in last lesson, we do not need to modify anything in _urls.py_. You can run the application now, being in the folder of the project, run:  _python manage.py runserver_.