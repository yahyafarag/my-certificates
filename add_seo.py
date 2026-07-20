import os
import glob
from bs4 import BeautifulSoup

base_url = "https://yahyafarag.github.io/yahya-web-site"
image_url = f"{base_url}/assets/images/profile/yahya-logo.jpeg"

def add_seo_tags():
    files = glob.glob("*.html")
    for file in files:
        if file == "404.html" or file.startswith("cv-viewer"):
            continue
            
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
            
        soup = BeautifulSoup(html, 'html.parser')
        head = soup.head
        if not head:
            continue
            
        # Clean up old SEO tags to avoid duplicates
        for tag in head.find_all('meta', property=True):
            if tag['property'].startswith('og:') or tag['property'].startswith('twitter:'):
                tag.decompose()
        for tag in head.find_all('meta', attrs={'name': ['twitter:card', 'twitter:title', 'twitter:description', 'twitter:image', 'description']}):
            tag.decompose()
        for tag in head.find_all('link', rel=['canonical', 'alternate']):
            tag.decompose()
        for script in head.find_all('script', type='application/ld+json'):
            script.decompose()

        is_ar = "-ar" in file
        lang = "ar" if is_ar else "en"
        alt_file = file.replace("-ar.html", ".html") if is_ar else file.replace(".html", "-ar.html")
        alt_lang = "en" if is_ar else "ar"
        
        # Determine title and desc
        title_tag = soup.find('title')
        title = title_tag.text if title_tag else "INJAZ Engineering"
        
        desc = "Engineering Performance Solutions by Yahya Tarek. Specialized in industrial maintenance, automation, and operational excellence."
        if is_ar:
            desc = "حلول الأداء الهندسي والصيانة الصناعية والأتمتة. استشارات هندسية احترافية لزيادة الأرباح وتقليل الهدر مع م. يحيى طارق."

        if "article" in file or "case-study" in file:
            h1 = soup.find('h1')
            if h1:
                title = h1.text + (" | INJAZ" if "INJAZ" not in h1.text else "")
                title_tag.string = title

        # Create new tags
        seo_html = f"""
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{base_url}/{file}">
    <link rel="alternate" hreflang="{lang}" href="{base_url}/{file}">
    <link rel="alternate" hreflang="{alt_lang}" href="{base_url}/{alt_file}">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{base_url}/{file}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="{image_url}">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="{base_url}/{file}">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{image_url}">
"""
        
        # Inject JSON-LD
        schema_type = "Article" if ("article" in file or "case-study" in file or "blog" in file) else "ProfilePage"
        json_ld = f"""
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "{schema_type}",
      "name": "{title}",
      "description": "{desc}",
      "url": "{base_url}/{file}",
      "author": {{
        "@type": "Person",
        "name": "Yahya Tarek Farag",
        "jobTitle": "General Manager of Engineering"
      }}
    }}
    </script>
"""
        
        seo_soup = BeautifulSoup(seo_html + json_ld, 'html.parser')
        for tag in seo_soup.contents:
            if tag.name:
                head.append(tag)

        # Fix HTML lang attribute if missing
        if soup.html:
            soup.html['lang'] = lang
            soup.html['dir'] = 'rtl' if is_ar else 'ltr'
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Added SEO to {file}")

if __name__ == "__main__":
    add_seo_tags()
