from django.shortcuts import render

from .facade import get_all_projects, get_project, get_extra_project_images


def portfolio(request):
    projects = get_all_projects()
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/masonry-3-columns.html', context)


def portfolio_detail(request, slug):
    project = get_project(slug=slug)
    extra_images = get_extra_project_images(slug=slug)
    context = {
        'project': project,
        'extra_images': extra_images,
    }
    return render(request, 'portfolio/detail.html', context)
