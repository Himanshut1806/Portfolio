from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Contact
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
            'path':'images/ecommerce.png',
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
            'company': 'Augurs Technology Pvt.Ltd',
            'position': 'Python Developer Intern',
            'description': 'Click here to view Certificate',
            'Duration': 'December 2024 - Present',
            'Location': 'Lucknow',
        },
        {
            'company': 'OPL Innovate',
            'position': 'Java Developer Intern',
            'description': 'Click here to view Certificate',
            'Duration': 'March 2024 - June 2024 (3 Months)',
            'Location': 'Ahmedabad',
            'certificate_url': 'https://drive.google.com/file/d/1ZeikDHUTnc_Xx8WLgLR3KhB-ISy92upt/view?usp=drivesdk'
        },
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
    resume_path = "myapp/Himanshu_s_Resume.pdf"
    if staticfiles_storage.exists(resume_path):
        with staticfiles_storage.open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="Himanshu_s_Resume.pdf"'
            return response
    else:
        return HttpResponse("resume not found", status=404)  

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