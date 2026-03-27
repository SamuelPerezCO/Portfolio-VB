from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Profile, Project, Skill, Experience, ContactMessage
from .forms import ContactForm


def _get_profile():
    return Profile.objects.first()


def home(request):
    profile = _get_profile()
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    skills = Skill.objects.all()
    skills_by_category = {}
    for skill in skills:
        cat = skill.get_category_display()
        skills_by_category.setdefault(cat, []).append(skill)

    context = {
        'profile': profile,
        'featured_projects': featured_projects,
        'skills_by_category': skills_by_category,
    }
    return render(request, 'portfolio/home.html', context)


def about(request):
    profile = _get_profile()
    experiences = Experience.objects.all()
    work_exp = experiences.filter(type='work')
    education = experiences.filter(type='education')
    context = {
        'profile': profile,
        'work_experiences': work_exp,
        'education': education,
    }
    return render(request, 'portfolio/about.html', context)


def projects(request):
    profile = _get_profile()
    all_projects = Project.objects.all()
    skills = Skill.objects.filter(projects__isnull=False).distinct()

    # Filter by technology
    tech_filter = request.GET.get('tech')
    if tech_filter:
        all_projects = all_projects.filter(technologies__slug=tech_filter)

    context = {
        'profile': profile,
        'projects': all_projects,
        'skills': skills,
        'active_filter': tech_filter,
    }
    return render(request, 'portfolio/projects.html', context)


def project_detail(request, slug):
    profile = _get_profile()
    project = get_object_or_404(Project, slug=slug)
    related = Project.objects.filter(
        technologies__in=project.technologies.all()
    ).exclude(pk=project.pk).distinct()[:3]

    context = {
        'profile': profile,
        'project': project,
        'related_projects': related,
    }
    return render(request, 'portfolio/project_detail.html', context)


def contact(request):
    profile = _get_profile()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            # Try to send email notification
            try:
                send_mail(
                    subject=f'Portfolio contact: {msg.subject}',
                    message=f'From: {msg.name} <{msg.email}>\n\n{msg.message}',
                    from_email=settings.EMAIL_HOST_USER or 'noreply@portfolio.com',
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(request, 'Your message has been sent! I\'ll get back to you soon.')
            return redirect('contact')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)
