from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Profile(models.Model):
    # Personal Information
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, help_text="Your professional title")
    bio = models.TextField(help_text="Short bio for home page")
    
    # Images
    profile_image = models.ImageField(upload_to='profile/', help_text="Profile picture for home page")
    about_image = models.ImageField(upload_to='about/', blank=True, null=True, help_text="Image for about page")
    
    # Resume
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True, help_text="PDF Resume file")
    
    # Social Links
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    
    # SEO
    meta_description = models.TextField(blank=True, help_text="SEO meta description")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Profile"

class TechnicalSkill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(blank=True, help_text="Proficiency percentage (1-100),")
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    category = models.CharField(max_length=100, blank=True, help_text="e.g., Frontend, Backend, Database")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Technical Skills"

class SoftSkill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Soft Skills"

class Internship(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='companies/', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    technologies = models.CharField(max_length=500, help_text="Comma separated technologies")
    achievements = models.TextField(blank=True, help_text="Key achievements (one per line)")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.position} at {self.company}"
    
    class Meta:
        ordering = ['-start_date']

class Certificate(models.Model):
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-issue_date']

class Education(models.Model):
    DEGREE_CHOICES = [
        ('high_school', 'High School'),
        ('bachelor', 'Bachelor\'s Degree'),
        ('master', 'Master\'s Degree'),
        ('phd', 'PhD'),
        ('diploma', 'Diploma'),
        ('certificate', 'Certificate'),
    ]
    
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100, choices=DEGREE_CHOICES)
    field_of_study = models.CharField(max_length=200)
    institution_logo = models.ImageField(upload_to='education/', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    grade = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.degree} in {self.field_of_study}"
    
    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = "Education"

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=500, help_text="Brief description for cards")
    description = models.TextField()
    tech_stack = models.CharField(max_length=500, help_text="Comma separated technologies")
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)
    project_image = models.ImageField(upload_to='projects/')
    additional_images = models.ImageField(upload_to='projects/additional/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)
    client = models.CharField(max_length=200, blank=True)
    role = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('project_detail', args=[self.slug])
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-featured', '-completion_date', '-created_date']

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-timestamp']