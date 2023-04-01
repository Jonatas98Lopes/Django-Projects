from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Investimentos
from .forms import InvestimentoForm
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

def criar(request):
    investimento_form = InvestimentoForm()
    formulario = {
        'formulario': investimento_form
    }
    return render(request, 'invista_me/novo_investimento.html', context=formulario) 
