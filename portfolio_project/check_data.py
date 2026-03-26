import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()
from main.models import Internship, Training
print('--- Internships ---')
for i in Internship.objects.all():
    print(f'Internship: {i.position}, Logo: {i.company_logo}')
print('--- Trainings ---')
for t in Training.objects.all():
    print(f'Training: {t.title}, Image: {t.image}')
