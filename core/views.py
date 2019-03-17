from django.shortcuts import render

from portfolio.facade import get_last_projects


def home(request):
    projects_home = get_last_projects(6)
    context = {
        'projects_home': projects_home,
    }
    return render(request, 'home.html', context)


def quem_somos(request):
    return render(request, 'quem-somos.html')
