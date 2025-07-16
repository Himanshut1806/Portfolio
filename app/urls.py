from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about, name="about"),
    path('projects/', views.projects, name="projects"),
    path('experience/', views.experience , name="experience"),
    path('certificate/', views.certificate , name="certificate"),
    path('contact/', views.contact , name="contact"),
    # path('resume/', views.resume , name="resume"),
    path('contact1/',views.contact1,name="contact1"),
]