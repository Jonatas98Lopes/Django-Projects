# Now, we are going to learn how to block as many pages as we need in our project.

The first step was to make the user sign in. We are going to restric him.

***

In our project we want to keep available the initial page and _detalhes.html_ page for everyone to see them. But we do not want users without to add, edit or exclude investments in our pages. In other words, we need to block these pages. Howw

***

* Go into the _views.py_ file that renders the pages we want to restrict.

* Being in the apropriate _views.py_, import the following line:

```
from django.contrib.auth.decorators import login_required.
```

We are going to user a decorator point to thhe import *login_required*. This will make the login_required function be asked always when a user tries to access the pages blocked. A decorator is a form to make user that a function will always be executed before another.

***

* Now, identify the functions that render the exclusion page, the edition page and the adding page, and put a decorator like:

```
@login_required
def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'invista_me/novo_investimento.html', context=formulario) 


@login_required
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

@login_required
def excluir(request, id_investimento):
    investimento = Investimentos.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'invista_me/confirmar_exclusao.html', {'item': investimento})
```

***

However, there is a standard path that will redirect to a login page, in a folder that we do not use. We need to inform the correct one. Let us do it.

***

* Go into _setting.py_.

* Add the command:
```
LOGIN_URL = 'login'  
```
The value atfer equals sign is the _name_ attribute informed in _urls.py_.
***
It must be working efficiently.
