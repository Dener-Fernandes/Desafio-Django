from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.TarefaPageView, name='lista_tarefas'),
    path('criar_tarefas/', views.CriarTarefaPageView, name='adicionar_tarefa_pagina'),
    path('adicionar_tarefa/', views.AdicionarTarefa, name='adicionar_tarefas'),
    path('atualizar_tarefa_pagina/<int:tarefa_id>', views.AtualizarTarefaPageView, name='atualizar_tarefas_pagina'),
    path('atualizar_tarefa/<int:tarefa_id>', views.AtualizarTarefa, name='atualizar_tarefa'),
    path('excluir_tarefa_pagina/<int:tarefa_id>', views.ExcluirTarefaPageView, name='excluir_tarefas_pagina'),
    path('excluir_tarefa/<int:tarefa_id>', views.ExcluirTarefa, name='excluir_tarefa'),
    path('concluir_tarefa/<tarefa>', views.ConcluirTarefa, name='concluir_tarefa'),
]