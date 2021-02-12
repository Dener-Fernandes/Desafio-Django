from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Tarefa(models.Model):
    descricao = models.CharField(max_length = 30)
    status_tarefa = models.CharField(max_length = 9, default = 'PENDENTE')
    usuario_tarefa = models.ForeignKey(User, on_delete = models.CASCADE) 

    def __str__(self):
        return self.descricao