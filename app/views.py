from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.http import FileResponse, Http404
import os
from django.conf import settings
# Create your views here.

def home(request):
    return render (request,"home.html")

def about(request):
    return render (request,"about.html")

def projects(request):
    projects_show = [

        {
            'title': 'Portfolio Website',
            'desc': 'A personal portfolio built using Django to showcase skills, experience, and projects with a clean UI.',
            'github': 'https://github.com/Himanshut1806/Portfolio'
        },
        {
            'title': 'E-commerce Platform (AShopping)',
            'desc': 'Full Django-based e-commerce system with cart, checkout, session-based cart updates, and Stripe payment integration.',
            'github': 'https://github.com/Himanshut1806/AShopping'
        },
        {
            'title': 'Blog Project',
            'desc': 'A complete blogging system with authentication, CRUD operations, categories, and modern Bootstrap UI.',
            'github': 'https://github.com/Himanshut1806/Blog-Project'
        },
        {
            'title': 'Secure Notes App',
            'desc': 'A Django application for encrypted note storage with authentication and data protection.',
            'github': 'https://github.com/Himanshut1806/Secure-Notes'
        },
        {
            'title': 'Employee CRUD System',
            'desc': 'A CRUD-based Django web app to manage employee records including add, update, and delete functionality.',
            'github': 'https://github.com/Himanshut1806/Employee-CRUD-Operation'
        },
        {
            'title': 'JWT Authentication (Custom User)',
            'desc': 'A Django REST Framework project implementing JWT authentication with a custom user model.',
            'github': 'https://github.com/Himanshut1806/JWT-Authentication-Custom-User-Model'
        },
        {
            'title': 'DRF API Project',
            'desc': 'A Django REST Framework API project demonstrating serializers, viewsets, and API CRUD operations.',
            'github': 'https://github.com/Himanshut1806/DRF-Project'
        },
        {
            'title': 'Django REST Framework Demo',
            'desc': 'An API-driven project showing DRF basics including permissions, authentication, and API routing.',
            'github': 'https://github.com/Himanshut1806/Django-Rest-Framework'
        },
        {
            'title': 'Student CRUD Operation',
            'desc': 'A simple and clean Django CRUD app for managing student data with SQLite database.',
            'github': 'https://github.com/Himanshut1806/Student-CRUD-Opertion'
        },
        {
            'title': 'StudyBud Community App',
            'desc': 'A full-stack community discussion platform built using Django, featuring rooms, topics, login & activity feed.',
            'github': 'https://github.com/Himanshut1806/Studybud'
        },
        {
            'title': 'Django CRUD',
            'desc': 'A classic CRUD project implementing create, read, update, and delete operations using Django.',
            'github': 'https://github.com/Himanshut1806/Django-CRUD'
        }
    ]
    return render(request, "projects.html", {'projects_show': projects_show})




def experience(request):
    experience = [
        {
        "company": "RR Corporate Pvt. Ltd.",
        "position": "Python Developer",
        "Duration": "Aug 2025 – Present",
        "Location": "Lucknow, India",
        "description": "Working on backend development, Python-based feature implementation, and application maintenance to ensure efficient and scalable system workflows.",
        "certificate_url": None 
        },
        {
        "company": "Augurs Technology Pvt. Ltd.",
        "position": "Python Developer Intern",
        "Duration": "Dec 2024 – Jul 2025",
        "Location": "Lucknow, India",
        "description": "Collaborated on Python and Django applications focusing on code quality, debugging, optimization, and working closely with senior developers for feature development.",
        "certificate_url": "https://drive.google.com/file/d/1hFAo6_f6GbCRac7XEG_ZeTTj4wbb_gR6/view?usp=drivesdks"
        },
        {
        "company": "OPL Innovate",
        "position": "Java Developer Intern",
        "Duration": "Mar 2024 – Jun 2024",
        "Location": "Ahmedabad, India",
        "description": "Handled MySQL databases, optimized SQL queries, and contributed to backend application logic and reporting features.",
        "certificate_url":"https://drive.google.com/file/d/1ZeikDHUTnc_Xx8WLgLR3KhB-ISy92upt/view?usp=drivesdk"
        }
        ]
    return render(request, "experience.html", {"experience": experience})


def certificate(request):
    certificates = [
        {
            'title': 'Python Programming',
            'description': 'Certificate in Python Programming',
            'click': 'Click here to view Certificate',
            'url': 'https://drive.google.com/file/d/1_ZlZV-krY1TQCCY_vCUz-34EehBNDST5/view?usp=drivesdk',
            'icon': 'fas fa-certificate text-success',
        },
        {
            'title': 'Python Udemy Bootcamp',
            'description': 'Certificate in Python',
            'click': 'Click here to view Certificate',
            'url': 'https://drive.google.com/file/d/1_aHGh20xQjR404rWTxT0ve9sohKcIhZp/view?usp=drivesdk',
            'icon': 'fas fa-certificate text-primary',
        },
        {
            'title': 'National IP Awareness Mission',
            'description': 'Certificate in National IP Awareness Mission',
            'click': 'Click here to view Certificate',
            'url': 'https://drive.google.com/file/d/119A81H2PKeWijGWS455Brg_rnPoeKxo7/view?usp=drivesdk',
            'icon': 'fas fa-certificate text-info',
        },
    ]
    return render(request, "certificate.html", {"certificates": certificates})


def contact(request):
    return render (request,"contact.html")

def resume(request):
    file_path = os.path.join(settings.BASE_DIR, "app", "static", "myapp", "Himanshu_Resume.pdf")

    if os.path.exists(file_path):
        return FileResponse(open(file_path, "rb"), content_type="application/pdf")
    else:
        raise Http404("Resume not found")

def contact1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        en = Contact(name=name, email=email, phone=phone, message=message)
        en.save()
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')  