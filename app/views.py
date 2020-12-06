from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse ('time'),
        'Показать содержимое рабочей директории': reverse ('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def vvv(request):
    return HttpResponse('привет')

def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now()
    time = current_time.strftime("%d-%m-%Y %H:%M")
    msg = f'Текущее время: {time}'
    return HttpResponse(msg)


def workdir_view(request):
    msg = "Все папки и файлы:", os.listdir()
    return HttpResponse(msg)
