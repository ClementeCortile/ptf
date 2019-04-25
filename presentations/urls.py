from django.urls import path

from . import views

urlpatterns = [
    path('', views.allpresentations, name='allpresentations'),
    path('<int:presentation_id>/', views.presentationsdetail, name='presentationsdetail'),
]

