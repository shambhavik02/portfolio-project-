from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone']
    search_fields = ['name', 'title', 'email']

@admin.register(TechnicalSkill)
class TechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency', 'category', 'order']
    list_editable = ['proficiency', 'order']
    list_filter = ['category']
    search_fields = ['name']

@admin.register(SoftSkill)
class SoftSkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']
    search_fields = ['name']

@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'company']
    search_fields = ['position', 'company', 'description']

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuing_organization', 'issue_date']
    list_filter = ['issuing_organization']
    search_fields = ['name', 'issuing_organization']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['field_of_study', 'degree', 'institution', 'start_date', 'current']
    list_filter = ['degree', 'current']
    search_fields = ['field_of_study', 'institution']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'completion_date', 'created_date']
    list_filter = ['featured']
    search_fields = ['title', 'description', 'tech_stack']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_date', 'updated_date']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'timestamp', 'is_read']
    list_filter = ['is_read', 'timestamp']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['timestamp']