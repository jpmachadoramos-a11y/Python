from django.urls import path
from sistema.views import *

urlpatterns = [
    path('paciente/', index), # vollmed.com/paciente
    path('paciente/novo/'), # vollmed.com/paciente/novo/
    path('paciente/perfil/<int:paciente_id>'), # vollmed.com/paciente/perfil/<int:paciente_id>
    path('paciente/listagem', listar_pacientes) # vollmed.com/paciente/listagem



]
# path variable