from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . import models, forms

# Create your views here.

def TarefaPageView(request):
    if request.user.is_authenticated:
        usuario_tarefa = User.objects.get(id = request.session['_auth_user_id'])
        tarefas_lista = models.Tarefa.objects.filter(usuario_tarefa = usuario_tarefa)
        data_dict = {
        'tarefas_lista': tarefas_lista,
        }
        return render(request, 'lista_tarefas.html', data_dict)
    else:
        return redirect('/')


def CriarTarefaPageView(request):
    if request.user.is_authenticated:
        return render(request, 'criar_tarefa.html')
    else:
        return redirect('/')

def AdicionarTarefa(request):
    if request.method == 'POST':
        if len(request.POST['descricao']) < 4 or len(request.POST['descricao']) > 30:
            return render(request, 'criar_tarefa.html')
        else:
            usuario_tarefa = User.objects.get(id = request.session['_auth_user_id'])
            nova_tarefa = models.Tarefa.objects.create(
                descricao = request.POST['descricao'],
                status_tarefa = 'PENDENTE',
                usuario_tarefa = usuario_tarefa
            )
            return redirect('/tarefas')

def AtualizarTarefaPageView(request, tarefa_id):
    if request.user.is_authenticated:
        tarefa = models.Tarefa.objects.get(id = tarefa_id)
        data_dict = {'tarefa': tarefa}
        return render(request, 'atualizar_tarefa.html', data_dict)
    else:
        return redirect('/')

def AtualizarTarefa(request, tarefa_id):
    if request.method == 'POST':
        tarefa = models.Tarefa.objects.get(id = tarefa_id)
        if len(request.POST['descricao']) < 4 or len(request.POST['descricao']) > 30:
            data_dict = {'tarefa': tarefa}
            return render(request, 'atualizar_tarefa.html', data_dict)
        else:
            tarefa.descricao = request.POST['descricao']
            if tarefa.status_tarefa == 'REALIZADA':
                tarefa.status_tarefa = 'PENDENTE'
            tarefa.save()
            return redirect('/tarefas')
    
def ExcluirTarefaPageView(request, tarefa_id):
    if request.user.is_authenticated:
        tarefa = models.Tarefa.objects.get(id = tarefa_id)
        data_dict = {'tarefa': tarefa}
        return render(request, 'excluir_tarefa.html', data_dict)
    else:
        return redirect('/')

def ExcluirTarefa(request, tarefa_id):
    tarefa = models.Tarefa.objects.get(id = tarefa_id)
    tarefa.delete()
    return redirect('/tarefas')

def ConcluirTarefa(request, tarefa_id):
    tarefa = models.Tarefa.objects.get(id = tarefa_id)

    tarefa.status_tarefa = 'REALIZADA'
    tarefa.save()
    return redirect('/tarefas')
    









