from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.TarefaPageView, name='lista_tarefas'),
    path('done/<int:tarefa_id>', views.done, name='tenso'),
]