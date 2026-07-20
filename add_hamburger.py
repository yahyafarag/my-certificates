import os
import re
import glob

css_to_add = """
        /* Mobile Menu Styles */
        .mobile-menu-btn { display: none; background: none; border: none; color: #fff; font-size: 1.5rem; cursor: pointer; }
        @media (max-width: 768px) {
            .mobile-menu-btn { display: block; }
            .nav-links { 
                position: absolute; top: 100%; left: 0; width: 100%; 
                background: rgba(15, 36, 64, 0.95); backdrop-filter: blur(10px);
                flex-direction: column; padding: 2rem 0; gap: 1.5rem;
                border-bottom: 1px solid var(--glass-border);
                display: none; 
            }
            .nav-links.active { display: flex; }
        }
"""

js_to_add = """
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const mobileBtn = document.querySelector('.mobile-menu-btn');
            const navLinks = document.querySelector('.nav-links');
            if(mobileBtn && navLinks) {
                mobileBtn.addEventListener('click', () => {
                    navLinks.classList.toggle('active');
                });
            }
            
            // Sticky Navbar transparency effect
            const navbar = document.querySelector('.navbar');
            window.addEventListener('scroll', () => {
                if(window.scrollY > 50) {
                    navbar.style.background = 'rgba(15, 36, 64, 0.85)';
                } else {
                    navbar.style.background = 'rgba(15, 36, 64, 1)';
                }
            });
        });
    </script>
"""

def add_mobile_menu():
    html_files = glob.glob("*.html")
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add CSS if not present
        if ".mobile-menu-btn" not in content:
            content = content.replace("</style>", css_to_add + "\n    </style>")
            
        # Add JS if not present
        if "mobileBtn.addEventListener" not in content:
            content = content.replace("</body>", js_to_add + "\n</body>")

        # Inject the hamburger button before nav-links if not present
        if '<button class="mobile-menu-btn"' not in content:
            # We find the nav-brand closing div and insert the button right after it, before nav-links
            # Regex to find <div class="nav-links"> and prepend the button
            content = re.sub(
                r'(<div class="nav-links">)',
                r'<button class="mobile-menu-btn"><i class="fa-solid fa-bars"></i></button>\n        \1',
                content
            )
            
            # Also fix the hiding of nav-links which might be in the inline <style> block from previous redesigns
            content = content.replace("@media (max-width: 768px) { .nav-links { display: none; } }", "")
            content = content.replace("@media (max-width: 768px) {\n            .nav-links { display: none; }", "@media (max-width: 768px) {")

        # Performance fixes: lazy loading for brands marquee in index
        if "index" in file:
            content = content.replace('<img src="assets/images/brands/', '<img loading="lazy" decoding="async" src="assets/images/brands/')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Processed {file}")

if __name__ == "__main__":
    add_mobile_menu()
