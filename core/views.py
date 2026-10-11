from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from .models import *
from datetime import date
from threading import Thread


def contact(request):
    if request.method == "POST":
        name = (request.POST.get('name') or '').strip()
        email = (request.POST.get('email') or '').strip()
        subject = (request.POST.get('subject') or '').strip()
        message = (request.POST.get('message') or '').strip()
        phone = (request.POST.get('phone') or '').strip()
        address = (request.POST.get('address') or '').strip()

        if not name or not email or not subject or not message:
            messages.error(request, 'Please fill in name, email, subject and message.')
            return redirect('contact')

        # Save contact
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            phone=phone or None,
            address=address or None,
        )
        email_subject = "Message from suyog"
        email_body = "Thanks for leaving your contact we will contact you soon"
        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', None) or getattr(
            settings, 'EMAIL_HOST_USER', None
        ) or 'noreply@example.com'
        # Always notify site owner; include visitor email only when valid
        recipient_list = [r for r in {email, getattr(settings, 'EMAIL_HOST_USER', '')} if r]

        def _send():
            try:
                send_mail(
                    subject=email_subject,
                    message=email_body,
                    from_email=from_email,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
            except Exception:
                # Background thread: nothing to show the user from here.
                pass

        try:
            thread = Thread(target=_send, daemon=True)  # it is used to make work fast
            thread.start()
            messages.success(request, f'Hi {name}, your form is submitted! Please check your email.')
        except Exception:
            messages.warning(request, f'Hi {name}, your form is submitted. Email notification failed but we received your message.')

        return redirect('contact')

    return render(request, 'core/contact.html')

def home(request):
    birth_date = date(2005, 4, 16)
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return render(request, 'core/home.html', {'age': age})
def project(request):
    project_headings = Project_title.objects.all()
    cateid = request.GET.get("category")
    if cateid:
        # "all" (any case) or a non-numeric value must not crash the page.
        cateid_str = str(cateid).strip()
        if isinstance(cateid, str) and cateid_str.lower() == "all":
            item = Project_items.objects.all()
        elif cateid_str.isdigit() and Project_title.objects.filter(pk=int(cateid_str)).exists():
            item = Project_items.objects.filter(category_id=int(cateid_str))
        elif cateid_str.isdigit():
            # Valid number but no such category -> empty queryset, defaults still show.
            item = Project_items.objects.none()
        else:
            item = Project_items.objects.all()
    else:
        item = Project_items.objects.all()

    default_projects = [
                {
            'heading': 'Heramba Store(E-commerce)',
            'desc': 'An online shopping store with product browsing, cart management, and order handling, built with a clean responsive storefront for a smooth buying experience.',
            'category': 'E-commerce',
            'language_used': 'DRF API CICD react docker',
            'status': 'Live',
            'github_url': None,
            'url': 'https://heramba.store/',
            'image_url': 'images/heramba.png',
            'is_default': True,
        },
         {
            'heading': 'BrandConnect(SaaS)',
            'desc': 'This is a SaaS project — a bank-linked merchant operations platform for managing business, payments, teams, and compliance. Features identity, POS, payments, inventory, accounting, and analytics in one unified workspace.',
            'category': 'Full Stack',
            'language_used': 'Next.js React TypeScript TailwindCSS',
            'status': 'Live',
            'github_url': None,
            'url': 'https://uat.colthinkspace.com/',
            'image_url': 'images/brandconnect.png',
            'is_default': True,
        },

        {
            'heading': 'Sajha Infotech(IT Institute )',
            'desc': 'A company website for Sajha Infotech showcasing IT services, solutions, and contact information with a modern responsive design.',
            'category': 'Full Stack',
            'language_used': 'DRF API react docker CI/CD',
            'status': 'Live',
            'github_url': None,
            'url': 'https://sajhainfotech.com/',
            'image_url': 'images/sajhainfotech.png',
            'is_default': True,
        },
        {
            'heading': 'Learner E-Learning(online learning platform)',
            'desc': 'An online learning platform with expert-led courses, enrollment and cart, certificates, and instructor dashboards — learn at your own pace from anywhere.',
            'category': 'Full Stack',
            'language_used': 'Python Django Bootstrap HTML CSS',
            'status': 'Live',
            'github_url': None,
            'url': 'https://e-learning-oxrc.onrender.com/',
            'image_url': 'images/elaerning.png',
            'is_default': True,
        },
        {
            'heading': 'Weather Application(see real weather)',
            'desc': 'A weather forecasting application that provides real-time weather data, forecasts, and visualizations. Built with clean UI design and API integration for accurate weather information.',
            'category': 'Full Stack',
            'language_used': 'Python Django HTML CSS API',
            'status': 'Delivered',
            'github_url': None,
            'url': 'https://suyogapi.pythonanywhere.com/',
            'image_url': 'images/weather.png',
            'is_default': True,
        },
        {
            'heading': 'BP Hotel Management(Hotel Management System)',
            'desc': 'A complete hotel management system with room booking, guest management, payment processing, and admin dashboard. Built with Python and deployed on PythonAnywhere for reliable hosting.',
            'category': 'Full Stack',
            'language_used': 'Python Django HTML CSS',
            'status': 'Delivered',
            'github_url': None,
            'url': 'https://bphotel.pythonanywhere.com',
            'image_url': 'images/bphotel.png',
            'is_default': True,
        },
        {
            'heading': 'Portfolio Website',
            'desc': 'A modern, responsive portfolio website built with Django and custom CSS. Features 3D animations, smooth scroll effects, dynamic project showcase, and an integrated contact form with email notifications.',
            'category': 'Full Stack',
            'language_used': 'Django HTML CSS JavaScript',
            'status': 'Live',
            'github_url': None,
            'url': 'https://suyogkhadak.onrender.com',
            'image_url': 'images/portfolio.png',
            'is_default': True,
        },
  
        {
            'heading': 'Blog Application',
            'desc': 'A blogging platform that allows users to create, edit, and manage blog posts. Features user authentication, comment system, and responsive design for an optimal reading experience.',
            'category': 'Full Stack',
            'language_used': 'Python Django HTML CSS ',
            'status': 'Delivered',
            'github_url': None,
            'url': 'https://suyogblog.onrender.com/',
            'image_url': 'images/suyogblog.png',
            'is_default': True,
        },
    ]

    context={
            'project_headings':project_headings,
            'item':item,
            'has_db_items': item.exists(),
            'default_projects': default_projects,
    }
    return render(request,'core/project.html',context)

def main(request):
    return render(request,'core/main.html')

def testinomial(request):
    testinomial_items = Testinomial.objects.filter(is_active=True)

    if request.method == "POST":
        name = (request.POST.get('name') or '').strip()
        role = (request.POST.get('role') or '').strip()
        company = (request.POST.get('company') or '').strip()
        email = (request.POST.get('email') or '').strip()
        feedback = (request.POST.get('feedback') or '').strip()
        image = request.FILES.get('images')

        if not name or not feedback:
            messages.error(request, 'Please provide your name and feedback.')
            return redirect('testinomial')

        Testinomial.objects.create(
            name=name,
            role=role or None,
            company=company or None,
            email=email or None,
            feedback=feedback,
            image=image,
        )
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