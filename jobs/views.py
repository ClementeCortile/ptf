from django.shortcuts import render

from .models import Job
from projects import models


def home(request):
    jobs = Job.objects
    projects = models.Projects.objects
    return render(request, 'jobs/home.html', {'jobs': jobs,
                                              'projects': projects})

def musicchallange(request):
    return render(request, 'blog/MusicChallange.html')