# from django.views.generic import TemplateView
from django.shortcuts import render, redirect

# class HomePageView(TemplateView):
#     template_name = 'home.html'

def HomePageView(request):
    if request.user.is_authenticated:
        return redirect('/tarefas')
    else:
        return render(request, 'home.html')


   