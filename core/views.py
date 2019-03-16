from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def quem_somos(request):
    return render(request, 'quem-somos.html')
