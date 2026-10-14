from django.forms import forms 
from sistema.models import *
#checagem de email
#checagem de senha
#checagem de dado inserido

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'crm',]

