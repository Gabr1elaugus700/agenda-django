from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Coach(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Aluno(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    old = models.IntegerField()  # Usar IntegerField para idade
    phone = models.CharField(blank=True, null=True, max_length=50)
    login = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)
    created_in = models.DateTimeField(default=timezone.now)
    obs = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, null=True, upload_to='pictures/')
    category = models.CharField(max_length=50, blank=True)
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    coach = models.ForeignKey(
        Coach, 
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Aula(models.Model):
    day = models.CharField(max_length=50)
    hora_ini = models.TimeField()
    hora_fim = models.TimeField()
    coach = models.ForeignKey(
        Coach, 
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    
    def __str__(self) -> str:
        return f'{self.id} {self.day} {self.hora_ini} {self.coach} '

class OcorrenciaAula(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    data = models.DateField()
    alunos_presentes = models.ManyToManyField('Aluno', through='Aluno_OcorrenciaAula') 

    def __str__(self) -> str:
        return f'{self.aula} em {self.data}'

class Aluno_OcorrenciaAula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    ocorrenciaAula = models.ForeignKey(OcorrenciaAula, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.aluno} em {self.ocorrenciaAula}'

class Aluno_Aula(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.SET_NULL, null=True)  
    aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.id} {self.aula} {self.aluno}'

class Tema(models.Model):
    tema_name = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return f'{self.id} {self.tema_name}'