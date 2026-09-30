from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('sistema.urls.py')) # Preciso chamar as urls do app sistema
    # path('') # Preciso chamar as urls do app portal
]
