from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# VIEWS -> retornam algo, são funções, request -> response

# View responsável pela tela inicial do Consulta

def medico_view(request):
    print('Página Consulta funcionou')
    return HttpResponse('Página inicial do Consulta')