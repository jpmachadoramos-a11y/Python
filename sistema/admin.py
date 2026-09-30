from django.contrib import admin

from sistema import models

@admin.register(models.Paciente) #Registrando a classe paciente no portal do python
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'especialidade', 'crm', 'ativo',)

@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente_id', 'medico_id', 'status','consulta_nova')
