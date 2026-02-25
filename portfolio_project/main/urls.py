from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Public URLs
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('internships/', views.internships, name='internships'),
    path('certificates/', views.certificates, name='certificates'),
    path('contact/', views.contact, name='contact'),
    
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='admin_dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Admin Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Profile Management
    path('dashboard/profile/', views.profile_edit, name='profile_edit'),
    
    # Skills Management
    path('dashboard/skills/', views.skills_list, name='skills_list'),
    path('dashboard/skills/add/', views.skill_add, name='skill_add'),
    path('dashboard/skills/edit/<int:skill_id>/<str:skill_type>/', views.skill_edit, name='skill_edit'),
    path('dashboard/skills/delete/<int:skill_id>/<str:skill_type>/', views.skill_delete, name='skill_delete'),
    
    # Internships Management
    path('dashboard/internships/', views.internships_list, name='internships_list'),
    path('dashboard/internships/add/', views.internship_add, name='internship_add'),
    path('dashboard/internships/edit/<int:internship_id>/', views.internship_edit, name='internship_edit'),
    path('dashboard/internships/delete/<int:internship_id>/', views.internship_delete, name='internship_delete'),
    
    # Certificates Management
    path('dashboard/certificates/', views.certificates_list, name='certificates_list'),
    path('dashboard/certificates/add/', views.certificate_add, name='certificate_add'),
    path('dashboard/certificates/edit/<int:certificate_id>/', views.certificate_edit, name='certificate_edit'),
    path('dashboard/certificates/delete/<int:certificate_id>/', views.certificate_delete, name='certificate_delete'),
    
    # Education Management
    path('dashboard/education/', views.education_list, name='education_list'),
    path('dashboard/education/add/', views.education_add, name='education_add'),
    path('dashboard/education/edit/<int:education_id>/', views.education_edit, name='education_edit'),
    path('dashboard/education/delete/<int:education_id>/', views.education_delete, name='education_delete'),
    
    # Projects Management
    path('dashboard/projects/', views.projects_list, name='projects_list'),
    path('dashboard/projects/add/', views.project_add, name='project_add'),
    path('dashboard/projects/edit/<int:project_id>/', views.project_edit, name='project_edit'),
    path('dashboard/projects/delete/<int:project_id>/', views.project_delete, name='project_delete'),
    
    # Messages Management
    path('dashboard/messages/', views.messages_list, name='messages_list'),
    path('dashboard/messages/<int:message_id>/', views.message_detail, name='message_detail'),
    path('dashboard/messages/delete/<int:message_id>/', views.message_delete, name='message_delete'),
]