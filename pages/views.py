# from django.views.generic import TemplateView
from django.shortcuts import render

# class HomePageView(TemplateView):
#     template_name = 'home.html'

def HomePageView(request):
    if request.user.is_authenticated:
        return render(request, 'lista_tarefas.html')
    else:
        return render(request, 'home.html')


   