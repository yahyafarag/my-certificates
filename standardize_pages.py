import os
from bs4 import BeautifulSoup

def process_html_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    soup = BeautifulSoup(html, 'html.parser')
    
    # Check if it's already updated (has page-header)
    if soup.find('header', class_='page-header') and not filepath.startswith("article") and not filepath.startswith("case-study"):
        print(f"Skipping {filepath}, already updated.")
        # But wait, articles might need it too.

    is_ar = '-ar.html' in filepath
    lang = 'ar' if is_ar else 'en'
    dir_attr = 'rtl' if is_ar else 'ltr'

    # Navbars
    nav_en = BeautifulSoup("""
    <nav class="navbar" style="background: rgba(15, 36, 64, 1); position: sticky;">
        <div class="nav-brand">
            <i class="fa-solid fa-gear" style="color: var(--accent);"></i> INJAZ
        </div>
        <div class="nav-links">
            <a href="index.html">Home</a>
            <a href="projects.html">Success Portfolio</a>
            <a href="blog.html">Knowledge Hub</a>
            <a href="certificates.html">Certificates</a>
            <a href="index-ar.html" class="lang-switch"><i class="fa-solid fa-globe"></i> العربية</a>
        </div>
    </nav>
    """, 'html.parser')

    nav_ar = BeautifulSoup("""
    <nav class="navbar" style="background: rgba(15, 36, 64, 1); position: sticky;">
        <div class="nav-brand">
            <i class="fa-solid fa-gear" style="color: var(--accent); margin-left: 0.5rem;"></i> إنجاز
        </div>
        <div class="nav-links">
            <a href="index-ar.html">الرئيسية</a>
            <a href="projects-ar.html">سابقة الأعمال</a>
            <a href="blog-ar.html">المدونة الهندسية</a>
            <a href="certificates-ar.html">الشهادات والاعتمادات</a>
            <a href="index.html" class="lang-switch" style="font-family: 'Inter', sans-serif;"><i class="fa-solid fa-globe"></i> English</a>
        </div>
    </nav>
    """, 'html.parser')

    footer = BeautifulSoup("""
    <footer class="footer">
        <h3 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.8rem;">Ready to stop the bleed?</h3>
        <div class="social-links">
            <a href="https://www.linkedin.com/in/yahyatarekfarag/" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
            <a href="mailto:Y_Tarek91@yahoo.com"><i class="fa-solid fa-envelope"></i></a>
            <a href="https://wa.me/201080801708" target="_blank"><i class="fa-brands fa-whatsapp"></i></a>
        </div>
        <p style="color: var(--text-muted);">&copy; 2026 INJAZ Engineering Performance Solutions. All Rights Reserved.</p>
    </footer>
    """, 'html.parser')

    # Remove old navs/headers
    for tag in soup.find_all('nav'):
        tag.decompose()
    for tag in soup.find_all('aside', class_='profile-sidebar'):
        tag.decompose()
    for tag in soup.find_all('div', class_='header'):
        tag.decompose()
    for tag in soup.find_all('div', id='particles-js'):
        tag.decompose()
    for tag in soup.find_all('div', id='particles'):
        tag.decompose()
    for tag in soup.find_all('header', class_='hero'):
        tag.decompose()
    for tag in soup.find_all('footer'):
        tag.decompose()

    # Find the main container
    container = soup.find('div', class_='dashboard-container') or soup.find('section', id='certificates') or soup.find('main', class_='content-wrapper')
    if not container:
        container = soup.find('div', class_='container')
    
    if not container:
        print(f"Warning: Could not find main container in {filepath}")
        return

    # Create new layout structure
    new_body = BeautifulSoup('<body></body>', 'html.parser').body
    new_body.append(nav_ar if is_ar else nav_en)
    
    # Add page header for blog and certificates
    if "blog" in filepath:
        header = BeautifulSoup(f'''
        <header class="page-header" style="margin-top: 80px;">
            <h1 class="page-title">{"مركز المعرفة" if is_ar else "Knowledge Hub"}</h1>
            <p class="page-subtitle">{"رؤى، دراسات حالة، وأفضل الممارسات الهندسية." if is_ar else "Insights, case studies, and engineering best practices."}</p>
        </header>
        ''', 'html.parser')
        new_body.append(header)
    elif "certificates" in filepath:
        header = BeautifulSoup(f'''
        <header class="page-header" style="margin-top: 80px;">
            <h1 class="page-title">{"الشهادات والاعتمادات" if is_ar else "Accreditations"}</h1>
            <p class="page-subtitle">{"الرخص والشهادات المهنية المعتمدة." if is_ar else "Professional certifications and licenses."}</p>
        </header>
        ''', 'html.parser')
        new_body.append(header)
    elif "article" in filepath or "case-study" in filepath:
        # Just give it a top margin to avoid nav overlap
        container['style'] = container.get('style', '') + '; margin-top: 120px;'

    # Clean up inline styles
    html_str = str(container)
    html_str = html_str.replace('rgba(236, 72, 153, 0.1)', 'rgba(242, 140, 40, 0.1)')
    html_str = html_str.replace('#ec4899', 'var(--accent)')
    container = BeautifulSoup(html_str, 'html.parser')

    new_body.append(container)
    new_body.append(footer)

    soup.body.replace_with(new_body)

    # Set base font family and background on body
    soup.body['style'] = "font-family: 'Tajawal', sans-serif; background: #0a192f; overflow-x: hidden; overflow-y: auto;" if is_ar else "background: #0a192f; overflow-x: hidden; overflow-y: auto;"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Updated {filepath}")

files_to_process = [
    'blog.html', 'blog-ar.html', 
    'certificates.html', 'certificates-ar.html',
    'article-cmms.html', 'article-cmms-ar.html',
    'article-greenfield.html', 'article-greenfield-ar.html',
    'article-it-ot.html', 'article-it-ot-ar.html',
    'article-lessons.html', 'article-lessons-ar.html',
    'article-oee.html', 'article-oee-ar.html',
    'article-tco.html', 'article-tco-ar.html',
    'case-study-beverage.html', 'case-study-beverage-ar.html',
    'case-study-cost.html', 'case-study-cost-ar.html',
    'case-study-fastfood.html', 'case-study-fastfood-ar.html'
]

for f in files_to_process:
    process_html_file(f)
