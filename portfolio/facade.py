from .models import Project, ProjectImages


def get_all_projects():
    """
    Search all projects on database sorted by title
    :return: tuple of Project
    """
    return tuple(Project.objects.order_by('title'))


def get_last_projects(quantidade=6):
    """
    Search last projects on database sorted by date
    :return: tuple of Project
    """
    return tuple(Project.objects.order_by('-created')[:int(quantidade)])


def get_project(slug):
    """
    Search for a project by slug
    :param slug: project's slug
    :return: Project
    """
    return Project.objects.get(slug=slug)


def get_extra_project_images(slug):
    """
    Search for extra images for the project
    :param slug: project's slug
    :return: ProjectImages
    """
    return ProjectImages.objects.all().filter(project__slug=slug)
