from django.shortcuts import render, get_object_or_404

from presentations import models

def allpresentations(request):
    presentations = models.Presentations.objects
    return render(request, 'presentations/presentations.html', {'presentation': presentations})

def presentationsdetail(request, presentation_id):
    detailpresentation = get_object_or_404(models.Presentations, pk=presentation_id)
    return render(request, 'presentations/presentationsdetail.html', {'presentations': detailpresentation})