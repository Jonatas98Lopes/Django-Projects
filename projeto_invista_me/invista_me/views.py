from django.shortcuts import render
from django.shortcuts import HttpResponse

def pagina_inicial(request):
    return HttpResponse('Pronto para investir!')

def contato(request):
    return HttpResponse('Para dúvidas, enviar um email para contato@suporte.com')