from django.shortcuts import HttpResponse, render, redirect
from .models import Investimento
from .forms import InvestimentoForm

"""
def pagina_inicial(request):
    return HttpResponse('Pronto para investir')

def get_contato(request):
    return HttpResponse('Eu quero o seu contato malandro')
def front_end(request):
    pessoa = {
        'nome': 'Jeff',
        'idade': 28,
        'hobbies': 'Games',
    }
    return render(request,'investimentos/index.html',pessoa) """


def investimento_registrado(request):
    investimentos = {
        'tipo_investimento': request.POST.get('TipoInvestimento')
    }
    return render(request, 'investimentos/investimento_registrado.html', investimentos)

def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimentos/investiments.html', context=dados)

def detalhes(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhes.html',dados)

def cadastrar_novo(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        redirect('investiments')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)


def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request,'investimentos/novo_investimento.html',{'formulario': formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investiments')
    
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investiments')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})

