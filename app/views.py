from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Contact2
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
            'path':'images/ecommerce.PNG',
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
            'Duration': '6 Months',
            'Location': 'Lucknow',
        },
        {
            'company': 'OPL Innovate',
            'position': 'Java Developer Intern',
            'Duration': '3 Months',
            'Location': 'Ahmedabad',
        },
    ]
    return render(request, "experience.html", {"experience": experience})

def certificate(request):
    return render (request, "certificate.html")

def contact(request):
    return render (request,"contact.html")

def resume(request):
    resume_path="myapp/Himanshu_s_Resume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404) 

def contact1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        en = Contact2(name=name, email=email, phone=phone, message=message)
        en.save()
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')