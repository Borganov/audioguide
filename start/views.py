from django.shortcuts import render


def start(request):
    return render(request, 'start/start.html')


def language(request):
    return render(request, 'start/language.html')


def aide(request):
    return render(request, 'start/aide.html')
