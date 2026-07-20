import os
import re
from bs4 import BeautifulSoup

nav_en = """
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
"""

nav_ar = """
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
"""

footer = """
    <footer class="footer">
        <h3 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.8rem;">Ready to stop the bleed?</h3>
        <div class="social-links">
            <a href="https://www.linkedin.com/in/yahyatarekfarag/" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
            <a href="mailto:Y_Tarek91@yahoo.com"><i class="fa-solid fa-envelope"></i></a>
            <a href="https://wa.me/201080801708" target="_blank"><i class="fa-brands fa-whatsapp"></i></a>
        </div>
        <p style="color: var(--text-muted);">&copy; 2026 INJAZ Engineering Performance Solutions. All Rights Reserved.</p>
    </footer>
"""

css_overrides = """
    <style>
        body { overflow-x: hidden; overflow-y: auto; background: #0a192f; }
        .page-header { text-align: center; padding: 4rem 2rem; background: var(--bg-gradient); border-bottom: 1px solid var(--glass-border); margin-top: 80px; }
        .page-title { font-size: 3rem; color: #fff; font-weight: 800; margin-bottom: 1rem; }
        .page-subtitle { color: var(--accent); font-size: 1.2rem; font-weight: 600; }
        .content-wrapper { padding: 4rem 5%; max-width: 1200px; margin: 0 auto; display: grid; gap: 2rem; }
        
        .navbar { position: fixed; top: 0; left: 0; width: 100%; padding: 1.5rem 5%; display: flex; justify-content: space-between; align-items: center; z-index: 100; background: rgba(15, 36, 64, 0.9); backdrop-filter: blur(10px); border-bottom: 1px solid var(--glass-border); }
        .nav-brand { font-size: 1.5rem; font-weight: 800; color: #fff; text-decoration:none; display:flex; align-items:center; gap:0.5rem;}
        .nav-links { display: flex; gap: 2rem; align-items: center; }
        .nav-links a { color: var(--text-main); text-decoration: none; font-weight: 600; transition: color 0.3s; }
        .nav-links a:hover { color: var(--accent); }
        .lang-switch { border: 1px solid var(--accent); padding: 0.5rem 1rem; border-radius: 20px; color: var(--accent) !important; }
        .footer { text-align: center; padding: 3rem 5%; border-top: 1px solid var(--glass-border); background: var(--bg-gradient); }
        .social-links { display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 2rem; }
        .social-links a { color: var(--text-muted); font-size: 1.8rem; transition: color 0.3s; }
        
        .project-vault-card, .blog-card, .cert-card { background: rgba(255,255,255,0.02); border: 1px solid var(--glass-border); border-radius: 12px; transition: transform 0.3s, border-color 0.3s; padding: 2rem; display: flex; flex-direction: column; }
        .project-vault-card:hover, .blog-card:hover, .cert-card:hover { transform: translateY(-5px); border-color: var(--accent); }
        .grid-layout { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
        @media (max-width: 768px) { .nav-links { display: none; } }
    </style>
"""

def extract_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()
    except:
        return None, None
    
    soup = BeautifulSoup(html, 'html.parser')
    title_tag = soup.find('title')
    title = title_tag.text if title_tag else "INJAZ"
    
    # We look for section id=certificates
    content_match = re.search(r'(<section.*?id="certificates".*?</section>)', html, flags=re.DOTALL)
    content = content_match.group(1) if content_match else ""
    
    content = content.replace('rgba(236, 72, 153, 0.1)', 'rgba(242, 140, 40, 0.1)')
    content = content.replace('#ec4899', 'var(--accent)')
    return title, content

def rebuild_file(filename, is_ar, page_title, page_subtitle):
    title, content = extract_content(filename)
    if not content:
        print(f"Skipped {filename} (no content found)")
        return

    lang = "ar" if is_ar else "en"
    dir_attr = 'dir="rtl"' if is_ar else 'dir="ltr"'
    nav = nav_ar if is_ar else nav_en
    font_link = '<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&display=swap" rel="stylesheet">' if is_ar else '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">'
    font_family = "font-family: 'Tajawal', sans-serif;" if is_ar else ""
    
    header_html = f'''
    <header class="page-header">
        <h1 class="page-title">{page_title}</h1>
        <p class="page-subtitle">{page_subtitle}</p>
    </header>
    '''

    new_html = f"""<!DOCTYPE html>
<html lang="{lang}" {dir_attr}>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    {font_link}
    <link rel="stylesheet" href="assets/css/style.css">
    {css_overrides}
</head>
<body style="{font_family}">
    {nav}
    {header_html}
    <main class="content-wrapper">
        {content}
    </main>
    {footer}
</body>
</html>
"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Rebuilt {filename}")

rebuild_file('certificates.html', False, 'Accreditations', 'Professional certifications and licenses.')
rebuild_file('certificates-ar.html', True, 'الشهادات والاعتمادات', 'الرخص والشهادات المهنية المعتمدة.')
