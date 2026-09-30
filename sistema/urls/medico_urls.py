from django.urls import path

from sistema.views import medico_view

urlpatterns = [
    path('medico/', medico_view), # vollmed.com/medico
    path('medico/novo/'),
    path('medico/perfil/<int:medico_id>'),
    path('medico/listagem'),
]