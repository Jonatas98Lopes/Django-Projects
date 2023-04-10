from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Investimentos
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required
def pagina_inicial(request):
    return HttpResponse('Pronto para investir!')

def contato(request):
    return HttpResponse('Para dúvidas, enviar um email para contato@suporte.com')

def minha_historia(request):
    pessoa = {
        'name': 'Bob',
        'age': 32,
        'hobby': 'Games'
    }
    return render(request, 'invista_me/minha_historia.html', pessoa)

""" def novo_investimento(request):
    return render(request, 'invista_me/novo_investimento.html') """

def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('TipoInvestimento')
    }
    return render(request, 'invista_me/investimento_registrado.html', investimento)

def investimento(request):
    dados = {
        'data': Investimentos.objects.all()
    }
    return render(request, 'invista_me/investimento.html', context=dados)

def detalhe(request, id_investimento):
    dados = {
        'dados': Investimentos.objects.get(pk=id_investimento) 
    }
    return render(request,'invista_me/detalhe.html',dados)

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
            
      
          
        