from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . import models, forms

# Create your views here.

def TarefaPageView(request):
    if request.user.is_authenticated:
        # form = forms.TarefaForm()
        # data_dict = {'form': form}
        # if request.method == 'POST':
        #     form = forms.TarefaForm(request.POST)
        #     if form.is_valid():
        #         form.save(commit=True)
        #     else:
        #         print('Erro!!!!')
        tarefas_lista = models.Tarefa.objects.order_by('descricao')
        data_dict = {
        'tarefas_lista': tarefas_lista,
        }
        return render(request, 'lista_tarefas.html', data_dict)
    else:
        return redirect('/')

def done(request, tarefa_id):
    user = User.objects.get(id=request.session['user_id'])
    tarefa = models.Tarefa.objects.get(id=tarefa_id)

    tarefa.status_tarefa.remove(user)

    # Recuperando os objetos das duas tabelas?
    tarefas_lista = user.tarefa_adicionada.all()


    data_dict = {
        'tarefas_lista': tarefas_lista,
    }

    return redirect('/tarefas', data_dict)
