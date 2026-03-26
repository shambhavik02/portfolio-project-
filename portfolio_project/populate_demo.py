from main.models import TechnicalSkill, SoftSkill, Certificate, Project, Education
from datetime import date

# Technical Skills
skills = [
    ('Python', 'fab fa-python', 'Core Programming', 1, 95),
    ('Machine Learning', 'fas fa-robot', 'Modeling & Algorithms', 2, 85),
    ('Data Analysis', 'fas fa-chart-line', 'Analytics', 3, 90),
    ('SQL', 'fas fa-database', 'Database Management', 4, 80),
    ('Tableau', 'fas fa-project-diagram', 'Visualization', 5, 75),
    ('Statistics', 'fas fa-calculator', 'Mathematics', 6, 85),
]

for name, icon, cat, order, prof in skills:
    TechnicalSkill.objects.update_or_create(
        name=name, 
        defaults={'icon': icon, 'category': cat, 'order': order, 'proficiency': prof}
    )

# Soft Skills
soft_skills = [
    ('Problem Solving', 'fas fa-lightbulb'),
    ('Critical Thinking', 'fas fa-brain'),
]
for name, icon in soft_skills:
    SoftSkill.objects.update_or_create(name=name, defaults={'icon': icon})

# Certificates (for Training section)
certs = [
    ('Data Science Professional Certificate', 'IBM', date(2023, 5, 15)),
    ('Machine Learning Specialization', 'DeepLearning.AI', date(2023, 8, 20)),
    ('Advanced Excel for Data Science', 'Microsoft', date(2023, 2, 10)),
]

for name, org, dt in certs:
    Certificate.objects.update_or_create(
        name=name, 
        defaults={'issuing_organization': org, 'issue_date': dt}
    )

print("Sample data populated successfully!")
