from urllib import request
from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from .models import *
from datetime import date
from django.shortcuts import render

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
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        user=Contact(name=name,email=email,subject=subject,message=message,phone=phone,address=address)
        user.save()
        subject="Message from suyog"
        message="Thanks for leaving your contact we will contact you soon"
        from_email='ksuyog697@gmail.com'
        recipient_list=[email,'suyog697@gmail.com']
        send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list,fail_silently=False)
        messages.success(request,f'hi {name} your form is submitted please check your email')


        return redirect('contact')
    return render(request,'core/contact.html')
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
    context={
            'project_headings':project_headings,
            'item':item,
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
    context={
        'testinomial_items':testinomial_items
    }
    
    return render(request, 'core/testinomial.html',context)