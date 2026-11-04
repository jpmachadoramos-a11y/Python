from django.urls import path
from sistema.views import *

# vollmed.com/admin
# vollmed.com/paciente => index
# vollmed.com/paciente/novo => index
urlpatterns = [
    path('paciente/', index_paciente), # vollmed.com/paciente
    # path('paciente/novo/'), # vollmed.com/paciente/novo/
    # path('paciente/perfil/<int:paciente_id>'), # vollmed.com/paciente/perfil/<int:paciente_id>
    # path('paciente/listagem', listar_pacientes) # vollmed.com/paciente/listagem
]
# path variable