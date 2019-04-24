from django.shortcuts import render

from presentations import models

def allpresentations(request):
    presentations = models.Presentations.objects
    return render(request, 'presentations/presentations.html', {'presentations': presentations})

