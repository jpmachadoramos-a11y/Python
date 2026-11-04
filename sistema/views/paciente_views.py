from django.shortcuts import render
# from django.http import HttpResponse
from sistema.models import Paciente

# Create your views here.
# VIEWS -> retornam algo, são funções, request -> response
# View responsável pela tela inicial do Paciente
def index_paciente (request):
    return render(
        request, 
        'index.html',
        '',
        )



# View responsável por listar todos os pacientes
# def listar_pacientes(request):
#     pacientes = Paciente.objects.all() # -> [obj1, obj2, obj3]

#     context = [
#         'pacientes', pacientes,
#     ]

#     return render(
#         request,
#         'paciente/listar.html',
#         context, 
#     )


# GLOBAL -> á uma página inteira
# PARTIALS -> Uma parte da página (header, footer, formulário)

# SPA

# MVT -> Templates/global/base.html