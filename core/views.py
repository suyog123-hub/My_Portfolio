import threading
from urllib import request
from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
from datetime import date
from django.shortcuts import render
from threading import Thread
def about(request):
    birth_date = date(2005, 4, 16) 
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    context = {
        'age': age,
    }
    
    return render(request, 'core/about.html', context)



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        # Save contact
        user = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            phone=phone,
            address=address
        )
        subject="Message from suyog"
        message="Thanks for leaving your contact we will contact you soon"
        from_email="ksuyog697@gmail.com"
        recipient_list=[email, 'ksuyog049@gmail.com']
        try:
            thread = Thread(target=send_mail,kwargs={
            "subject":subject,
            "message": message,
            "from_email": from_email,
            "recipient_list": recipient_list,
            "fail_silently": False ,
            },daemon=True) # it is used to make work fast 
            thread.start()
            messages.success(request, f'Hi {name}, your form is submitted! Please check your email.')
            
        except Exception as e:
            messages.warning(request, f'Hi {name}, your form is submitted. Email notification failed but we received your message.')
        
        return redirect('contact')
    
    return render(request, 'core/contact.html')

def home(request):
    return render(request,'core/home.html')
def project(request):
    project_headings=Project_title.objects.all()
    cateid=request.GET.get("category")
    if cateid == str(6):
        item=Project_items.objects.all()
    elif cateid:
        item=Project_items.objects.filter(category=cateid) 
    else:
        item=Project_items.objects.all()

    default_projects = [
        {
            'heading': 'Portfolio Website',
            'desc': 'A modern, responsive portfolio website built with Django and custom CSS. Features 3D animations, smooth scroll effects, dynamic project showcase, and an integrated contact form with email notifications.',
            'category': 'Full Stack',
            'language_used': 'Django HTML CSS JavaScript',
            'url': 'https://suyogkhadak.onrender.com',
            'image_url': '',
            'is_default': True,
        },
        {
            'heading': 'BP Hotel Management',
            'desc': 'A complete hotel management system with room booking, guest management, payment processing, and admin dashboard. Built with Python and deployed on PythonAnywhere for reliable hosting.',
            'category': 'Full Stack',
            'language_used': 'Python Django HTML CSS',
            'url': 'https://bphotel.pythonanywhere.com',
            'image_url': '',
            'is_default': True,
        },
        {
            'heading': 'REST API Backend',
            'desc': 'A scalable RESTful API backend built with Django REST Framework. Features JWT authentication, CRUD operations, pagination, filtering, and comprehensive API documentation with Swagger.',
            'category': 'Backend',
            'language_used': 'Python Django REST DRF PostgreSQL',
            'url': '#',
            'image_url': '',
            'is_default': True,
        },
    ]

    context={
            'project_headings':project_headings,
            'item':item,
            'default_projects': default_projects,
    }
    return render(request,'core/project.html',context)
def skills(request):
    skills=Skill.objects.all()
    skils_tools=Skill_tools.objects.all()
    context={
        'skills':skills,
        'skils_tools':skils_tools
    }
    return render(request,'core/skills.html',context)
def main(request):
    return render(request,'core/main.html')

def testinomial(request):
    testinomial_items=Testinomial.objects.filter(is_active=True)
    
    if request.method == "POST" and request.FILES:
        name = request.POST.get('name')
        role = request.POST.get('role')
        company = request.POST.get('company')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        image=request.FILES['images']
        user =Testinomial(name=name, role=role, company=company, email=email, feedback=feedback,image=image)
        user.save()
        messages.success(request, f'Hi {name}, your feedback has been submitted!')
        return redirect('testinomial')

    default_testimonials = [
        {
            'name': 'Ram Sharma',
            'role': 'Project Manager',
            'company': 'TechCorp Nepal',
            'feedback': 'Suyog delivered an exceptional portfolio website that exceeded all expectations. His attention to detail, clean code, and creative design made our project stand out. Highly recommend his work!',
            'image_url': '',
            'is_default': True,
        },
        {
            'name': 'Sita Patel',
            'role': 'CTO',
            'company': 'StartupHub',
            'feedback': 'Working with Suyog was a fantastic experience. He built a robust hotel management system that streamlined our operations. His backend skills and problem-solving abilities are top-notch.',
            'image_url': '',
            'is_default': True,
        },
        {
            'name': 'Anil Kumar',
            'role': 'Client',
            'company': 'Freelance Project',
            'feedback': 'Suyog is a talented developer who truly understands full-stack development. He delivered the project on time with clean, maintainable code. The REST API he built was well-structured and thoroughly documented.',
            'image_url': '',
            'is_default': True,
        },
    ]
    
    context={
        'testinomial_items':testinomial_items,
        'default_testimonials': default_testimonials,
    }
    
    return render(request, 'core/testinomial.html',context)