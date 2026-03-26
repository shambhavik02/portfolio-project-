from main.models import TechnicalSkill

TechnicalSkill.objects.all().delete()

skills = [
    # Languages
    ('Python',      'devicon-python-plain colored',      'Languages', 1, 95),
    ('SQL',         'devicon-mysql-plain colored',        'Languages', 2, 85),
    ('R',           'devicon-r-plain colored',            'Languages', 3, 70),
    ('CSS',         'devicon-css3-plain colored',        'Languages', 4, 85),
    ('C',           'devicon-c-plain colored',           'Languages', 5, 80),
    ('Java',        'devicon-java-plain colored',        'Languages', 6, 75),

    # Libraries & Tools
    ('NumPy',       'devicon-numpy-plain colored',        'Libraries & Tools', 1, 90),
    ('Pandas',      'devicon-pandas-plain colored',       'Libraries & Tools', 2, 90),
    ('TensorFlow',  'devicon-tensorflow-original colored','Libraries & Tools', 3, 75),
    ('Scikit-learn','devicon-scikitlearn-plain colored',  'Libraries & Tools', 4, 80),
    ('Matplotlib',  'devicon-matplotlib-plain colored',   'Libraries & Tools', 5, 80),
    ('Jupyter',     'devicon-jupyter-plain colored',      'Libraries & Tools', 6, 85),
    ('Django',      'devicon-django-plain colored',      'Libraries & Tools', 7, 85),
    ('JavaScript',  'devicon-javascript-plain colored',  'Libraries & Tools', 8, 90),
    ('React',       'devicon-react-original colored',    'Libraries & Tools', 9, 80),
    ('Tailwind',    'devicon-tailwindcss-plain colored', 'Libraries & Tools', 10, 85),
    ('CSS',         'devicon-css3-plain colored',        'Libraries & Tools', 11, 85),

    # Platforms & Concepts
    ('Machine Learning',  'fas fa-brain',             'Platforms & Concepts', 1, 80),
    ('Data Analysis',     'fas fa-chart-bar',          'Platforms & Concepts', 2, 90),
    ('Statistics',        'fas fa-calculator',         'Platforms & Concepts', 3, 85),
    ('Power BI',          'devicon-azuredevops-plain', 'Platforms & Concepts', 4, 75),
    ('GitHub',            'devicon-github-original',   'Platforms & Concepts', 5, 85),
    ('VS Code',           'devicon-vscode-plain colored','Platforms & Concepts', 6, 90),
]

for name, icon, cat, order, prof in skills:
    TechnicalSkill.objects.create(name=name, icon=icon, category=cat, order=order, proficiency=prof)

print("Skills populated!")

