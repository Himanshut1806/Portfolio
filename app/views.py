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
    projects_show=[
        {
            'title': 'Portfolio',
            'path': 'images/portfolio.png',
        },

        {
            'title':'Ecommerce',
            'path':'images/web.png',
        },  

        {
            'title': 'CRUD',
            'path': 'images/CRUD.PNG',
        },

        {
            'title':'Blog Project',
            'path':'images/Blogs.png',
        },

    ]
    return render (request,"projects.html",{"projects_show": projects_show})

def experience(request):
    experience = [
        {
        "company": "RR Corporate Pvt. Ltd.",
        "position": "Python Developer",
        "Duration": "Aug 2025 – Present",
        "Location": "Lucknow, India",
        "description": "Working on backend development, Python-based feature implementation, and application maintenance to ensure efficient and scalable system workflows.",
        "certificate_url": "#"
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
    # PDF ka exact path yahan set hota hai
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