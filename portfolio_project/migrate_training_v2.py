import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from main.models import Internship, Training

trainings_count = 0
for i in Internship.objects.all():
    # Find existing Training entry or create it
    t, created = Training.objects.get_or_create(
        title=i.position, 
        organization=i.company
    )
    # Update fields including the image
    t.start_date = i.start_date
    t.end_date = i.end_date
    t.current = i.current
    t.description = i.description
    t.technologies = i.technologies
    if i.company_logo:
        t.image = i.company_logo
    t.save()
    trainings_count += 1

print(f'Sync complete. Processed {trainings_count} entries.')
