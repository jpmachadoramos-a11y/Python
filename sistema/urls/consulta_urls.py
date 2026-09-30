from django.urls import path
from sistema.views import consulta_view

urlpatterns = [
    path('consulta/', consulta_view),
]