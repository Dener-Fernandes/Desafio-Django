from django import forms
from tarefas.models import Tarefa 

class TarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = ['descricao', 'status_tarefa']