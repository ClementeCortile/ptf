from django.shortcuts import render, get_object_or_404

from projects import models

def allprojects(request):
    projects = models.Projects.objects
    return render(request, 'projects/projects.html', {'projects': projects})

def projectsdetail(request, project_id):
    projectdetail = get_object_or_404(models.Projects, pk=project_id)
    return render(request, 'projects/projectsdetails.html', {'projectdetails': projectdetail})
