from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'coach', 'picture', 
    ordering = 'id',

@admin.register(models.Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    ordering = 'id',

@admin.register(models.Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = 'id', 'day', 'hora_ini', 'hora_fim', 'coach',
    ordering = '-id',

@admin.register(models.OcorrenciaAula)
class OcorrenciaAulaAdmin(admin.ModelAdmin):
    list_display = 'id', 'aula', 'data',
    ordering = 'id',

@admin.register(models.Aluno_OcorrenciaAula)
class Aluno_OcorrenciaAulaAdmin(admin.ModelAdmin):
    list_display = 'id', 'aluno', 'ocorrenciaAula', 'presente',
    ordering = 'id',

@admin.register(models.Aluno_Aula)
class Aluno_AulaAdmin(admin.ModelAdmin):
    list_display = 'id', 'aula', 'aluno',
    ordering = 'id',

@admin.register(models.Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = 'id', 'tema_name',
    ordering = 'id',