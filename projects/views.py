from django.shortcuts import render

from projects import models

def allprojects(request):
    projects = models.Projects.objects
    return render(request, 'projects/projects.html', {'projects': projects})