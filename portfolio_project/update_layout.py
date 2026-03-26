import os
import re

base_path = r'c:\Users\gauri\Desktop\Portfolio\portfolio_project\templates\main\base.html'
home_path = r'c:\Users\gauri\Desktop\Portfolio\portfolio_project\templates\main\home.html'

with open(base_path, 'r', encoding='utf-8') as f:
    base = f.read()

base = base.replace(
    "background: linear-gradient(135deg, #020617 0%, #020c1b 100%);",
    "background: #0b0f19;"
)

base = re.sub(r'/\* Sidebar \*/.*?/\* Main Wrapper \*/', '''/* Top Navigation */
        .top-nav {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 80px;
            background: rgba(11, 15, 25, 0.9);
            backdrop-filter: blur(10px);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 4rem;
            z-index: 50;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }

        .nav-brand {
            font-size: 1.5rem;
            font-weight: 700;
            color: #00f5d4 !important;
            text-decoration: none;
            font-family: 'Poppins', sans-serif;
            cursor: pointer;
        }

        .nav-menu {
            display: flex;
            align-items: center;
            gap: 2.5rem;
        }

        .nav-link {
            color: #94a3b8;
            font-size: 0.9rem;
            font-weight: 500;
            text-decoration: none;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
        }

        .nav-link:hover, .nav-link.active {
            color: #ffffff;
        }

        .nav-button {
            padding: 0.6rem 1.5rem;
            background: #00f5d4;
            color: #020617;
            border-radius: 9999px;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            text-decoration: none;
            cursor: pointer;
        }

        .nav-button:hover {
            background: #00c6ff;
            box-shadow: 0 0 10px rgba(0, 245, 212, 0.3);
        }

        /* Main Wrapper */''', base, flags=re.DOTALL)

base = base.replace('''        .main-wrapper {
            margin-left: 80px;
            height: 100vh;
            width: calc(100% - 80px);
            position: relative;
            overflow: hidden;
        }''', '''        .main-wrapper {
            margin-top: 80px;
            height: calc(100vh - 80px);
            width: 100%;
            position: relative;
            overflow: hidden;
        }''')

base = base.replace('''        .bg-lines {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: linear-gradient(rgba(0, 245, 212, 0.04) 1px, transparent 1px),
                              linear-gradient(90deg, rgba(0, 245, 212, 0.04) 1px, transparent 1px);
            background-size: 50px 50px;
            z-index: -2;
            pointer-events: none;
        }''', '''        .bg-lines {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #0b0f19;
            background-image: linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
                              linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
            background-size: 40px 40px;
            z-index: -2;
            pointer-events: none;
        }''')

base = base.replace(
    "background: radial-gradient(circle at center, rgba(0, 245, 212, 0.03) 0%, transparent 60%);",
    "display: none;"
)

base = re.sub(r'@media \(max-width: 768px\) \{.*?\}\s*</style>', '''@media (max-width: 768px) {
            body {
                overflow-y: auto;
            }
            .top-nav {
                padding: 0 1.5rem;
            }
            .nav-menu {
                display: none;
            }
            .main-wrapper {
                margin-top: 80px;
                width: 100%;
                height: calc(100vh - 80px);
            }
        }
    </style>''', base, flags=re.DOTALL)

base = re.sub(r'<!-- Sidebar Navigation -->.*?</aside>', '''<!-- Top Navigation -->
    <nav class="top-nav">
        <a data-target="home" class="nav-brand nav-link">Shambhavi</a>
        
        <div class="nav-menu">
            <a data-target="home" class="nav-link active">Home</a>
            <a data-target="about" class="nav-link">About</a>
            <a data-target="achievements" class="nav-link">Certificate</a>
            <a data-target="skills" class="nav-link">Skills</a>
            <a data-target="projects" class="nav-link">Projects</a>
            <a data-target="contact" class="nav-link">Contact</a>
        </div>
        
        <a data-target="contact" class="nav-button nav-link">Get in Touch</a>
    </nav>''', base, flags=re.DOTALL)

# Also update the JS link logic slightly
base = base.replace(
    "if(nav.getAttribute('data-target') === targetId) link.classList.add('active');",
    "if(nav.getAttribute('data-target') === targetId) nav.classList.add('active');"
)

with open(base_path, 'w', encoding='utf-8') as f:
    f.write(base)


with open(home_path, 'r', encoding='utf-8') as f:
    home = f.read()

hero_replacement = '''<!-- Hero Section -->
<section id="home" class="min-h-full flex items-center pt-24 pb-12">
    <div class="max-w-7xl mx-auto w-full px-6 lg:px-12 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
        
        <div class="order-2 lg:order-1 flex flex-col items-start text-left">
            <div class="border border-primary-500/30 text-primary-400 text-sm px-4 py-1.5 rounded-full mb-6 flex items-center gap-2">
                <span>✨</span> Welcome to my Portfolio
            </div>
            
            <h1 class="text-4xl lg:text-7xl font-bold font-heading mb-4 text-white uppercase tracking-wide">
                HI, I'M <br/>
                <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#00f5d4] to-[#b224ef] drop-shadow-[0_0_8px_rgba(0,245,212,0.4)]">SHAMBHAVI</span>
            </h1>
            
            <div class="flex items-center gap-4 text-sm md:text-base font-medium text-white mb-8">
                <span class="flex items-center gap-2"><i class="fas fa-laptop-code text-white"></i> Aspiring Engineer</span>
                <span class="text-primary-500/50">|</span>
                <span class="flex items-center gap-2"><i class="fas fa-chart-bar text-white"></i> Data Science Enthusiast</span>
            </div>

            <div class="text-base text-slate-400 leading-relaxed max-w-lg font-light mb-10">
                {{ about.description }}
            </div>
            
            <div class="flex flex-wrap gap-6 items-center">
                <a href="#projects" class="nav-link-trigger bg-primary-500 text-dark-100 font-bold px-6 py-3 rounded-full hover:bg-primary-400 transition-colors shadow-[0_0_15px_rgba(0,245,212,0.4)]" data-target="projects">
                    View Work &rarr;
                </a>
                
                {% if profile.resume_file %}
                <a href="{% url 'download_cv' %}" class="inline-flex items-center gap-2 px-6 py-3 rounded-full border border-primary-500/50 text-white font-medium hover:bg-primary-500/10 transition-colors">
                   📄 Resume
                </a>
                {% endif %}
            </div>

            <div class="flex items-center gap-4 mt-12">
                {% if profile.github %}
                <a href="{{ profile.github }}" target="_blank" class="w-10 h-10 rounded-full border border-slate-700 flex items-center justify-center text-slate-400 hover:text-white hover:border-primary-400 transition-colors"><i class="fab fa-github"></i></a>
                {% endif %}
                {% if profile.linkedin %}
                <a href="{{ profile.linkedin }}" target="_blank" class="w-10 h-10 rounded-full border border-slate-700 flex items-center justify-center text-slate-400 hover:text-white hover:border-primary-400 transition-colors"><i class="fab fa-linkedin-in"></i></a>
                {% endif %}
                <a href="mailto:{{ profile.email }}" class="w-10 h-10 rounded-full border border-slate-700 flex items-center justify-center text-slate-400 hover:text-white hover:border-primary-400 transition-colors"><i class="fas fa-envelope"></i></a>
            </div>
        </div>

        <div class="order-1 lg:order-2 w-full flex justify-center lg:justify-end relative">
            {% if profile.profile_image %}
            <div class="w-72 h-72 lg:w-[400px] lg:h-[400px] rounded-full p-[4px] bg-gradient-to-tr from-[#00f5d4] via-blue-500 to-[#b224ef] shadow-[0_0_30px_rgba(0,245,212,0.3)]">
                <img src="{{ profile.profile_image.url }}" alt="Shambhavi Kumari" class="w-full h-full object-cover rounded-full border-[8px] border-[#0b0f19]">
            </div>
            {% endif %}
        </div>
        
    </div>
</section>'''

home = re.sub(r'<!-- Hero Section -->.*?</section>', hero_replacement, home, count=1, flags=re.DOTALL)

skills_content_to_extract = re.search(r'<!-- Skills Subsection -->.*</div>\s*</div>', home, flags=re.DOTALL)
if skills_content_to_extract:
    skills_html = skills_content_to_extract.group(0)
    home = home.replace(skills_html, '')
    
    box_format_skills = '''<!-- Skills Section -->
<section id="skills" class="min-h-full py-20 relative z-10">
    <div class="max-w-4xl mx-auto w-full px-6 lg:px-12">
        <h2 class="text-xl md:text-2xl font-semibold text-left text-primary-400 mb-10 font-heading">
            My Skills
        </h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            {% regroup technical_skills by category as skill_groups %}
            {% for group in skill_groups %}
            <div class="bg-transparent border border-slate-700/60 p-8 rounded-3xl group">
                <h3 class="text-2xl font-bold text-white mb-6 font-heading">{{ group.grouper }}</h3>
                <div class="flex flex-wrap gap-4">
                    {% for skill in group.list %}
                    <div class="flex items-center gap-3 px-5 py-2.5 rounded-full border border-slate-700/60 bg-dark-200/50 hover:border-primary-500/50 transition-all cursor-default relative overflow-hidden">
                        <i class="{{ skill.icon|default:'fas fa-code' }} text-xl text-slate-300 hover:text-primary-400 transition-colors"></i>
                        <span class="text-sm font-semibold text-slate-300 hover:text-white transition-colors">{{ skill.name }}</span>
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
'''
    about_match = re.search(r'<!-- About Section -->.*?</section>', home, flags=re.DOTALL)
    if about_match:
        about_full = about_match.group(0)
        home = home.replace(about_full, about_full + '\n\n' + box_format_skills)

# Fix Nav selector in JS inside home.html
home = home.replace('.sidebar .nav-link', '.top-nav .nav-link')

with open(home_path, 'w', encoding='utf-8') as f:
    f.write(home)

print("Done updating")
