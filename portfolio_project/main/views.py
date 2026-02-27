from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .forms import ContactForm

# Public Views
def home(request):
    profile = Profile.objects.first()
    technical_skills = TechnicalSkill.objects.all()
    soft_skills = SoftSkill.objects.all()
    featured_projects = Project.objects.filter(featured=True)[:3]
    internships = Internship.objects.all()[:3]
    
    context = {
        'profile': profile,
        'technical_skills': technical_skills,
        'soft_skills': soft_skills,
        'featured_projects': featured_projects,
        'internships': internships,
    }
    return render(request, 'main/home.html', context)

def about(request):
    profile = Profile.objects.first()
    educations = Education.objects.all()
    
    total_projects = Project.objects.count()
    total_certificates = Certificate.objects.count()
    
    context = {
        'profile': profile,
        'educations': educations,
        'total_projects': total_projects,
        'total_certificates': total_certificates,
    }
    return render(request, 'main/about.html', context)

def projects(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    
    context = {
        'profile':profile,
        'projects': projects,
    }
    return render(request, 'main/projects.html', context)

def project_detail(request, slug):
    profile = Profile.objects.first()
    project = get_object_or_404(Project, slug=slug)
    
    context = {
        'profile': profile,
        'project': project,
    }
    return render(request, 'main/project_detail.html', context)

def internships(request):
    profile = Profile.objects.first()
    internships = Internship.objects.all()
    
    context = {
        'profile' : profile,
        'internships': internships,
    }
    return render(request, 'main/internships.html', context)

def certificates(request):
    profile = Profile.objects.first()
    certificates = Certificate.objects.all()
    
    context = {
        'profile' : profile,
        'certificates': certificates,
    }
    return render(request, 'main/certificates.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to database
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Send email notification
        try:
            admin_subject = f"New Contact Form Submission: {subject}"
            admin_message = f"""
            Name: {name}
            Email: {email}
            Subject: {subject}
            Message: {message}
            """
            send_mail(
                admin_subject,
                admin_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=True,
            )
            
            # Send confirmation to user
            user_subject = "Thank you for contacting me"
            user_message = f"""
            Dear {name},
            
            Thank you for reaching out. I have received your message and will get back to you soon.
            
            Best regards,
            {Profile.objects.first().name if Profile.objects.first() else 'Portfolio Owner'}
            """
            send_mail(
                user_subject,
                user_message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=True,
            )
        except:
            pass  # Email sending failed, but that's okay
        
        messages.success(request, 'Message sent successfully!')
        return redirect('contact')
    
    profile = Profile.objects.first()
    context = {
        'profile': profile,
    }
    return render(request, 'main/contact.html', context)

# Admin Dashboard Views
@login_required
def dashboard(request):
    total_projects = Project.objects.count()
    total_internships = Internship.objects.count()
    total_certificates = Certificate.objects.count()
    total_messages = ContactMessage.objects.filter(is_read=False).count()
    
    recent_messages = ContactMessage.objects.order_by('-timestamp')[:5]
    
    context = {
        'total_projects': total_projects,
        'total_internships': total_internships,
        'total_certificates': total_certificates,
        'total_messages': total_messages,
        'recent_messages': recent_messages,
    }
    return render(request, 'admin_dashboard/dashboard.html', context)

# Profile Management
@login_required
def profile_edit(request):
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(
            name="Your Name",
            title="Full Stack Developer",
            bio="Your bio here",
            email="your.email@example.com"
        )
    
    if request.method == 'POST':
        profile.name = request.POST.get('name')
        profile.title = request.POST.get('title')
        profile.bio = request.POST.get('bio')
        profile.email = request.POST.get('email')
        profile.phone = request.POST.get('phone')
        profile.location = request.POST.get('location')
        profile.github = request.POST.get('github')
        profile.linkedin = request.POST.get('linkedin')
        profile.twitter = request.POST.get('twitter')
        profile.instagram = request.POST.get('instagram')
        
        if request.FILES.get('profile_image'):
            profile.profile_image = request.FILES['profile_image']
        if request.FILES.get('about_image'):
            profile.about_image = request.FILES['about_image']
        if request.FILES.get('resume_file'):
            profile.resume_file = request.FILES['resume_file']
        
        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('dashboard')
    
    context = {
        'profile': profile,
    }
    return render(request, 'admin_dashboard/profile_edit.html', context)

# Skills Management
@login_required
def skills_list(request):
    technical_skills = TechnicalSkill.objects.all()
    soft_skills = SoftSkill.objects.all()
    
    context = {
        'technical_skills': technical_skills,
        'soft_skills': soft_skills,
    }
    return render(request, 'admin_dashboard/skills_list.html', context)

@login_required
def skill_add(request):
    if request.method == 'POST':
        skill_type = request.POST.get('skill_type')
        
        if skill_type == 'technical':
            TechnicalSkill.objects.create(
                name=request.POST.get('name'),
                proficiency=request.POST.get('proficiency', 80),
                icon=request.POST.get('icon', 'fas fa-code'),
                category=request.POST.get('category', ''),
                order=request.POST.get('order', 0)
            )
        else:
            SoftSkill.objects.create(
                name=request.POST.get('name'),
                description=request.POST.get('description', ''),
                icon=request.POST.get('icon', 'fas fa-check-circle'),
                order=request.POST.get('order', 0)
            )
        
        messages.success(request, 'Skill added successfully!')
        return redirect('skills_list')
    
    skill_type = request.GET.get('type', 'technical')
    context = {
        'skill_type': skill_type,
    }
    return render(request, 'admin_dashboard/skill_add.html', context)

@login_required
def skill_edit(request, skill_id, skill_type):
    if skill_type == 'technical':
        skill = get_object_or_404(TechnicalSkill, id=skill_id)
    else:
        skill = get_object_or_404(SoftSkill, id=skill_id)
    
    if request.method == 'POST':
        skill.name = request.POST.get('name')
        if skill_type == 'technical':
            skill.proficiency = request.POST.get('proficiency', 80)
            skill.icon = request.POST.get('icon', 'fas fa-code')
            skill.category = request.POST.get('category', '')
        else:
            skill.description = request.POST.get('description', '')
            skill.icon = request.POST.get('icon', 'fas fa-check-circle')
        skill.order = request.POST.get('order', 0)
        skill.save()
        
        messages.success(request, 'Skill updated successfully!')
        return redirect('skills_list')
    
    context = {
        'skill': skill,
        'skill_type': skill_type,
    }
    return render(request, 'admin_dashboard/skill_edit.html', context)

@login_required
def skill_delete(request, skill_id, skill_type):
    if skill_type == 'technical':
        skill = get_object_or_404(TechnicalSkill, id=skill_id)
    else:
        skill = get_object_or_404(SoftSkill, id=skill_id)
    
    skill.delete()
    messages.success(request, 'Skill deleted successfully!')
    return redirect('skills_list')

# Internships Management
@login_required
def internships_list(request):
    internships = Internship.objects.all()
    context = {
        'internships': internships,
    }
    return render(request, 'admin_dashboard/internships_list.html', context)

@login_required
def internship_add(request):
    if request.method == 'POST':
        internship = Internship.objects.create(
            company=request.POST.get('company'),
            position=request.POST.get('position'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date') or None,
            current=request.POST.get('current') == 'on',
            description=request.POST.get('description'),
            technologies=request.POST.get('technologies'),
            achievements=request.POST.get('achievements', ''),
            order=request.POST.get('order', 0)
        )
        
        if request.FILES.get('company_logo'):
            internship.company_logo = request.FILES['company_logo']
            internship.save()
        
        messages.success(request, 'Internship added successfully!')
        return redirect('internships_list')
    
    return render(request, 'admin_dashboard/internship_add.html')

@login_required
def internship_edit(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)
    
    if request.method == 'POST':
        internship.company = request.POST.get('company')
        internship.position = request.POST.get('position')
        internship.start_date = request.POST.get('start_date')
        internship.end_date = request.POST.get('end_date') or None
        internship.current = request.POST.get('current') == 'on'
        internship.description = request.POST.get('description')
        internship.technologies = request.POST.get('technologies')
        internship.achievements = request.POST.get('achievements', '')
        internship.order = request.POST.get('order', 0)
        
        if request.FILES.get('company_logo'):
            internship.company_logo = request.FILES['company_logo']
        
        internship.save()
        messages.success(request, 'Internship updated successfully!')
        return redirect('internships_list')
    
    context = {
        'internship': internship,
    }
    return render(request, 'admin_dashboard/internship_edit.html', context)

@login_required
def internship_delete(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)
    internship.delete()
    messages.success(request, 'Internship deleted successfully!')
    return redirect('internships_list')

# Certificates Management
@login_required
def certificates_list(request):
    certificates = Certificate.objects.all()
    context = {
        'certificates': certificates,
    }
    return render(request, 'admin_dashboard/certificates_list.html', context)

@login_required
def certificate_add(request):
    if request.method == 'POST':
        certificate = Certificate.objects.create(
            name=request.POST.get('name'),
            issuing_organization=request.POST.get('issuing_organization'),
            issue_date=request.POST.get('issue_date'),
            credential_id=request.POST.get('credential_id', ''),
            credential_url=request.POST.get('credential_url', ''),
            order=request.POST.get('order', 0)
        )
        
        if request.FILES.get('certificate_image'):
            certificate.certificate_image = request.FILES['certificate_image']
            certificate.save()
        
        messages.success(request, 'Certificate added successfully!')
        return redirect('certificates_list')
    
    return render(request, 'admin_dashboard/certificate_add.html')

@login_required
def certificate_edit(request, certificate_id):
    certificate = get_object_or_404(Certificate, id=certificate_id)
    
    if request.method == 'POST':
        certificate.name = request.POST.get('name')
        certificate.issuing_organization = request.POST.get('issuing_organization')
        certificate.issue_date = request.POST.get('issue_date')
        certificate.credential_id = request.POST.get('credential_id', '')
        certificate.credential_url = request.POST.get('credential_url', '')
        certificate.order = request.POST.get('order', 0)
        
        if request.FILES.get('certificate_image'):
            certificate.certificate_image = request.FILES['certificate_image']
        
        certificate.save()
        messages.success(request, 'Certificate updated successfully!')
        return redirect('certificates_list')
    
    context = {
        'certificate': certificate,
    }
    return render(request, 'admin_dashboard/certificate_edit.html', context)

@login_required
def certificate_delete(request, certificate_id):
    certificate = get_object_or_404(Certificate, id=certificate_id)
    certificate.delete()
    messages.success(request, 'Certificate deleted successfully!')
    return redirect('certificates_list')

# Education Management
@login_required
def education_list(request):
    educations = Education.objects.all()
    context = {
        'educations': educations,
    }
    return render(request, 'admin_dashboard/education_list.html', context)

@login_required
def education_add(request):
    if request.method == 'POST':
        education = Education.objects.create(
            institution=request.POST.get('institution'),
            degree=request.POST.get('degree'),
            field_of_study=request.POST.get('field_of_study'),
            start_date=request.POST.get('start_date'),
            end_date=request.POST.get('end_date') or None,
            current=request.POST.get('current') == 'on',
            grade=request.POST.get('grade', ''),
            description=request.POST.get('description', ''),
            order=request.POST.get('order', 0)
        )
        
        if request.FILES.get('institution_logo'):
            education.institution_logo = request.FILES['institution_logo']
            education.save()
        
        messages.success(request, 'Education added successfully!')
        return redirect('education_list')
    
    return render(request, 'admin_dashboard/education_add.html')

@login_required
def education_edit(request, education_id):
    education = get_object_or_404(Education, id=education_id)
    
    if request.method == 'POST':
        education.institution = request.POST.get('institution')
        education.degree = request.POST.get('degree')
        education.field_of_study = request.POST.get('field_of_study')
        education.start_date = request.POST.get('start_date')
        education.end_date = request.POST.get('end_date') or None
        education.current = request.POST.get('current') == 'on'
        education.grade = request.POST.get('grade', '')
        education.description = request.POST.get('description', '')
        education.order = request.POST.get('order', 0)
        
        if request.FILES.get('institution_logo'):
            education.institution_logo = request.FILES['institution_logo']
        
        education.save()
        messages.success(request, 'Education updated successfully!')
        return redirect('education_list')
    
    context = {
        'education': education,
    }
    return render(request, 'admin_dashboard/education_edit.html', context)

@login_required
def education_delete(request, education_id):
    education = get_object_or_404(Education, id=education_id)
    education.delete()
    messages.success(request, 'Education deleted successfully!')
    return redirect('education_list')

# Projects Management
@login_required
def projects_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'admin_dashboard/projects_list.html', context)

@login_required
def project_add(request):
    if request.method == 'POST':
        project = Project.objects.create(
            title=request.POST.get('title'),
            short_description=request.POST.get('short_description'),
            description=request.POST.get('description'),
            tech_stack=request.POST.get('tech_stack'),
            github_link=request.POST.get('github_link', ''),
            live_demo_link=request.POST.get('live_demo_link', ''),
            featured=request.POST.get('featured') == 'on',
            completion_date=request.POST.get('completion_date') or None,
            client=request.POST.get('client', ''),
            role=request.POST.get('role', ''),
            order=request.POST.get('order', 0)
        )
        
        if request.FILES.get('project_image'):
            project.project_image = request.FILES['project_image']
        if request.FILES.get('additional_images'):
            project.additional_images = request.FILES['additional_images']
        
        project.save()
        messages.success(request, 'Project added successfully!')
        return redirect('projects_list')
    
    return render(request, 'admin_dashboard/project_add.html')

@login_required
def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        project.title = request.POST.get('title')
        project.short_description = request.POST.get('short_description')
        project.description = request.POST.get('description')
        project.tech_stack = request.POST.get('tech_stack')
        project.github_link = request.POST.get('github_link', '')
        project.live_demo_link = request.POST.get('live_demo_link', '')
        project.featured = request.POST.get('featured') == 'on'
        project.completion_date = request.POST.get('completion_date') or None
        project.client = request.POST.get('client', '')
        project.role = request.POST.get('role', '')
        project.order = request.POST.get('order', 0)
        
        if request.FILES.get('project_image'):
            project.project_image = request.FILES['project_image']
        if request.FILES.get('additional_images'):
            project.additional_images = request.FILES['additional_images']
        
        project.save()
        messages.success(request, 'Project updated successfully!')
        return redirect('projects_list')
    
    context = {
        'project': project,
    }
    return render(request, 'admin_dashboard/project_edit.html', context)

@login_required
def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    messages.success(request, 'Project deleted successfully!')
    return redirect('projects_list')

# Messages Management
@login_required
def messages_list(request):
    messages_list = ContactMessage.objects.all()
    context = {
        'messages': messages_list,
    }
    return render(request, 'admin_dashboard/messages_list.html', context)

@login_required
def message_detail(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)
    message.is_read = True
    message.save()
    
    context = {
        'message': message,
    }
    return render(request, 'admin_dashboard/message_detail.html', context)

@login_required
def message_delete(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)
    message.delete()
    messages.success(request, 'Message deleted successfully!')
    return redirect('messages_list')