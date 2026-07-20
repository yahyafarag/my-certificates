import os

# New English Homepage HTML
html_en = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="INJAZ Engineering Performance Solutions - Stop the bleed, multiply your profits. Expert industrial maintenance and engineering consulting by Eng. Yahya Tarek.">
    <title>INJAZ - Engineering Performance Solutions</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
    <style>
        /* Homepage Specific Styles */
        body { overflow-x: hidden; overflow-y: auto; }
        .navbar { position: fixed; top: 0; left: 0; width: 100%; padding: 1.5rem 5%; display: flex; justify-content: space-between; align-items: center; z-index: 100; background: rgba(15, 36, 64, 0.9); backdrop-filter: blur(10px); border-bottom: 1px solid var(--glass-border); }
        .nav-brand { font-size: 1.5rem; font-weight: 800; color: #fff; letter-spacing: 1px; display: flex; align-items: center; gap: 0.5rem; }
        .nav-links { display: flex; gap: 2rem; align-items: center; }
        .nav-links a { color: var(--text-main); text-decoration: none; font-weight: 600; transition: color 0.3s; }
        .nav-links a:hover { color: var(--accent); }
        .lang-switch { border: 1px solid var(--accent); padding: 0.5rem 1rem; border-radius: 20px; color: var(--accent) !important; }
        
        .hero { min-height: 100vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 0 5%; position: relative; z-index: 10; }
        .hero-content { max-width: 900px; margin-top: 4rem; }
        .hero-title { font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 800; line-height: 1.2; margin-bottom: 1rem; }
        .hero-slogan { font-size: clamp(1.2rem, 3vw, 2rem); color: var(--accent); font-weight: 600; margin-bottom: 2rem; }
        .hero-desc { font-size: 1.1rem; color: var(--text-muted); margin-bottom: 3rem; line-height: 1.8; }
        .hero-btns { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
        
        .metrics-bar { display: flex; justify-content: center; flex-wrap: wrap; gap: 2rem; padding: 3rem 5%; background: rgba(0,0,0,0.2); border-top: 1px solid var(--glass-border); border-bottom: 1px solid var(--glass-border); position: relative; z-index: 10; }
        .metric-card { text-align: center; padding: 1rem; }
        .metric-card h3 { font-size: 2.5rem; color: var(--accent); margin-bottom: 0.5rem; font-weight: 800; }
        .metric-card p { color: var(--text-muted); font-size: 1.1rem; text-transform: uppercase; letter-spacing: 1px; }

        .section-title { text-align: center; font-size: 2.5rem; margin-bottom: 3rem; color: #fff; }
        .services-section { padding: 5rem 5%; position: relative; z-index: 10; background: var(--bg-gradient); }
        .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; max-width: 1200px; margin: 0 auto; }
        .service-card { background: rgba(255,255,255,0.03); border: 1px solid var(--glass-border); border-radius: 15px; padding: 2.5rem; text-align: center; transition: transform 0.3s; }
        .service-card:hover { transform: translateY(-10px); border-color: var(--accent); box-shadow: 0 10px 30px var(--accent-glow); }
        .service-card i { font-size: 3rem; color: var(--accent); margin-bottom: 1.5rem; }
        .service-card h4 { font-size: 1.5rem; margin-bottom: 1rem; color: #fff; }
        .service-card p { color: var(--text-muted); line-height: 1.6; }

        .about-section { padding: 5rem 5%; position: relative; z-index: 10; }
        .about-container { max-width: 1200px; margin: 0 auto; display: flex; align-items: center; gap: 4rem; flex-wrap: wrap; }
        .about-img { flex: 1; min-width: 300px; }
        .about-img img { width: 100%; border-radius: 15px; border: 2px solid var(--accent); box-shadow: 0 0 20px var(--accent-glow); }
        .about-text { flex: 2; min-width: 300px; }
        .about-text h2 { font-size: 2.5rem; margin-bottom: 1rem; color: #fff; }
        .about-text h3 { color: var(--accent); margin-bottom: 1.5rem; font-size: 1.2rem; }
        .about-text p { color: var(--text-muted); line-height: 1.8; margin-bottom: 1.5rem; font-size: 1.1rem; }

        .trusted-section { padding: 4rem 0; background: rgba(0,0,0,0.3); overflow: hidden; position: relative; z-index: 10; }
        .marquee { display: flex; width: max-content; animation: scroll 20s linear infinite; gap: 4rem; padding: 0 2rem; }
        .marquee img { height: 60px; object-fit: contain; filter: grayscale(100%) brightness(200%); opacity: 0.6; transition: 0.3s; }
        .marquee img:hover { filter: grayscale(0%); opacity: 1; }
        @keyframes scroll { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

        .footer { text-align: center; padding: 3rem 5%; border-top: 1px solid var(--glass-border); position: relative; z-index: 10; background: var(--bg-gradient); }
        .social-links { display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 2rem; }
        .social-links a { color: var(--text-muted); font-size: 1.8rem; transition: color 0.3s; }
        .social-links a:hover { color: var(--accent); }

        @media (max-width: 768px) {
            .nav-links { display: none; } /* Add hamburger later if needed, but for now simple links */
            .hero-title { font-size: 2rem; }
        }
    </style>
</head>
<body>
    <div id="particles-js" style="position:fixed; top:0; left:0; width:100%; height:100%; z-index:1;"></div>

    <nav class="navbar">
        <div class="nav-brand">
            <i class="fa-solid fa-gear" style="color: var(--accent);"></i> INJAZ
        </div>
        <div class="nav-links">
            <a href="projects.html">Success Portfolio</a>
            <a href="blog.html">Knowledge Hub</a>
            <a href="certificates.html">Certificates</a>
            <a href="index-ar.html" class="lang-switch"><i class="fa-solid fa-globe"></i> العربية</a>
        </div>
    </nav>

    <section class="hero">
        <div class="hero-content">
            <h1 class="hero-title">INJAZ Engineering Performance Solutions</h1>
            <h2 class="hero-slogan">"Stop the bleed, multiply your profits"</h2>
            <p class="hero-desc">We transform factory engineering and maintenance departments from cost centers into profit centers through strategic audits, CMMS implementation, and operational excellence.</p>
            <div class="hero-btns">
                <a href="projects.html" class="btn" style="background: var(--accent); color: #0F2440; font-weight:bold; padding: 1rem 2rem; text-decoration:none; border-radius: 30px;">Explore Success Portfolio</a>
                <a href="mailto:Y_Tarek91@yahoo.com" class="btn" style="border: 2px solid var(--accent); color: var(--accent); font-weight:bold; padding: 1rem 2rem; text-decoration:none; border-radius: 30px;">Book a Consultation</a>
            </div>
        </div>
    </section>

    <section class="metrics-bar">
        <div class="metric-card">
            <h3>50M+</h3>
            <p>EGP Saved</p>
        </div>
        <div class="metric-card">
            <h3>80%</h3>
            <p>Downtime Reduction</p>
        </div>
        <div class="metric-card">
            <h3>98%</h3>
            <p>Asset Readiness</p>
        </div>
        <div class="metric-card">
            <h3>25%</h3>
            <p>Energy Optimization</p>
        </div>
    </section>

    <section class="services-section">
        <h2 class="section-title">Core Engineering Services</h2>
        <div class="services-grid">
            <div class="service-card">
                <i class="fa-solid fa-magnifying-glass-chart"></i>
                <h4>Engineering Audit</h4>
                <p>Comprehensive inspection of your maintenance, energy, and operational workflows to pinpoint exact areas of financial bleeding and hidden capacity.</p>
            </div>
            <div class="service-card">
                <i class="fa-solid fa-server"></i>
                <h4>CMMS Implementation</h4>
                <p>Digital transformation of paper-based maintenance into a smart, preventative system ensuring 100% asset tracking and parts management.</p>
            </div>
            <div class="service-card">
                <i class="fa-solid fa-bolt"></i>
                <h4>Energy Audit</h4>
                <p>Advanced power quality analysis and leak detection to slash electricity bills by 15-25% with rapid ROI implementation plans.</p>
            </div>
            <div class="service-card">
                <i class="fa-solid fa-user-tie"></i>
                <h4>Outsourced Engineering Director</h4>
                <p>Fractional executive leadership to mentor your local team, oversee contractors, and drive strategic growth without the overhead of a full-time GM.</p>
            </div>
        </div>
    </section>

    <section class="about-section">
        <div class="about-container">
            <div class="about-img">
                <img src="assets/images/profile/yahya-logo.jpeg" alt="Eng. Yahya Tarek">
            </div>
            <div class="about-text">
                <h2>Meet The Founder</h2>
                <h3>Eng. Yahya Tarek | Engineering Performance Expert</h3>
                <p>With 15 years of deep industrial experience, Eng. Yahya has managed over 200 sites across massive factory complexes and multi-branch commercial chains.</p>
                <p>Holding a B.Sc. in Electrical Engineering and certified in Lean Six Sigma and Google Project Management, he bridges the gap between technical complexity and executive financial goals.</p>
                <a href="resume/Yahya_Tarek_Farag_Executive_Resume.pdf" download class="btn" style="border: 2px solid var(--accent); color: var(--accent); padding: 0.8rem 1.5rem; text-decoration:none; border-radius: 20px; display:inline-block; margin-top: 1rem;"><i class="fa-solid fa-download"></i> Download Full Resume</a>
            </div>
        </div>
    </section>

    <section class="trusted-section">
        <h2 class="section-title" style="font-size: 1.8rem; margin-bottom: 2rem;">Trusted By Industry Leaders</h2>
        <!-- Marquee twice for seamless loop -->
        <div class="marquee">
            <img src="assets/images/brands/BLABAN.webp" alt="B.Laban">
            <img src="assets/images/brands/FARAG ALLAH.webp" alt="Faragalla">
            <img src="assets/images/brands/BAHEG.webp" alt="Baheeg">
            <img src="assets/images/brands/AM SHALTAT.webp" alt="Am Shaltat">
            <img src="assets/images/brands/BLALM.webp" alt="Chicken Balalm">
            <img src="assets/images/brands/MORTADELLA.webp" alt="Mortadella">
            
            <img src="assets/images/brands/BLABAN.webp" alt="B.Laban">
            <img src="assets/images/brands/FARAG ALLAH.webp" alt="Faragalla">
            <img src="assets/images/brands/BAHEG.webp" alt="Baheeg">
            <img src="assets/images/brands/AM SHALTAT.webp" alt="Am Shaltat">
            <img src="assets/images/brands/BLALM.webp" alt="Chicken Balalm">
            <img src="assets/images/brands/MORTADELLA.webp" alt="Mortadella">
        </div>
    </section>

    <footer class="footer">
        <h3 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.8rem;">Ready to stop the bleed?</h3>
        <div class="social-links">
            <a href="https://www.linkedin.com/in/yahyatarekfarag/" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
            <a href="mailto:Y_Tarek91@yahoo.com"><i class="fa-solid fa-envelope"></i></a>
            <a href="https://wa.me/201080801708" target="_blank"><i class="fa-brands fa-whatsapp"></i></a>
        </div>
        <p style="color: var(--text-muted);">&copy; 2026 INJAZ Engineering Performance Solutions. All Rights Reserved.</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        window.addEventListener('load', () => {
            if(typeof particlesJS !== 'undefined') {
                particlesJS('particles-js', {
                  "particles": {
                    "number": { "value": 50, "density": { "enable": true, "value_area": 800 } },
                    "color": { "value": "#F28C28" },
                    "shape": { "type": "circle" },
                    "opacity": { "value": 0.5, "random": false },
                    "size": { "value": 3, "random": true },
                    "line_linked": { "enable": true, "distance": 150, "color": "#F28C28", "opacity": 0.2, "width": 1 },
                    "move": { "enable": true, "speed": 1.5, "direction": "none", "random": false, "straight": false, "out_mode": "out", "bounce": false }
                  },
                  "interactivity": {
                    "detect_on": "canvas",
                    "events": { "onhover": { "enable": true, "mode": "grab" }, "onclick": { "enable": true, "mode": "push" }, "resize": true },
                    "modes": { "grab": { "distance": 140, "line_linked": { "opacity": 1 } }, "push": { "particles_nb": 4 } }
                  },
                  "retina_detect": true
                });
            }
        });
    </script>
</body>
</html>
"""

# New Arabic Homepage HTML
html_ar = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="إنجاز لحلول الأداء الهندسي - أوقف النزيف، وضاعف أرباحك. خبراء الصيانة الصناعية والإدارة الهندسية بقيادة م. يحيى طارق.">
    <title>إنجاز - لحلول الأداء الهندسي</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/style.css">
    <style>
        body { overflow-x: hidden; overflow-y: auto; font-family: 'Tajawal', sans-serif; }
        .navbar { position: fixed; top: 0; left: 0; width: 100%; padding: 1.5rem 5%; display: flex; justify-content: space-between; align-items: center; z-index: 100; background: rgba(15, 36, 64, 0.9); backdrop-filter: blur(10px); border-bottom: 1px solid var(--glass-border); }
        .nav-brand { font-size: 1.5rem; font-weight: 800; color: #fff; letter-spacing: 0px; display: flex; align-items: center; gap: 0.5rem; }
        .nav-links { display: flex; gap: 2rem; align-items: center; }
        .nav-links a { color: var(--text-main); text-decoration: none; font-weight: 700; transition: color 0.3s; }
        .nav-links a:hover { color: var(--accent); }
        .lang-switch { border: 1px solid var(--accent); padding: 0.5rem 1rem; border-radius: 20px; color: var(--accent) !important; }
        
        .hero { min-height: 100vh; display: flex; align-items: center; justify-content: center; text-align: center; padding: 0 5%; position: relative; z-index: 10; }
        .hero-content { max-width: 900px; margin-top: 4rem; }
        .hero-title { font-size: clamp(2.5rem, 6vw, 4.5rem); font-weight: 900; line-height: 1.2; margin-bottom: 1rem; }
        .hero-slogan { font-size: clamp(1.5rem, 4vw, 2.5rem); color: var(--accent); font-weight: 800; margin-bottom: 2rem; }
        .hero-desc { font-size: 1.2rem; color: var(--text-muted); margin-bottom: 3rem; line-height: 1.8; }
        .hero-btns { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
        
        .metrics-bar { display: flex; justify-content: center; flex-wrap: wrap; gap: 3rem; padding: 3rem 5%; background: rgba(0,0,0,0.2); border-top: 1px solid var(--glass-border); border-bottom: 1px solid var(--glass-border); position: relative; z-index: 10; }
        .metric-card { text-align: center; padding: 1rem; }
        .metric-card h3 { font-size: 2.5rem; color: var(--accent); margin-bottom: 0.5rem; font-weight: 900; direction: ltr; }
        .metric-card p { color: var(--text-muted); font-size: 1.2rem; font-weight: 700; }

        .section-title { text-align: center; font-size: 2.5rem; font-weight: 800; margin-bottom: 3rem; color: #fff; }
        .services-section { padding: 5rem 5%; position: relative; z-index: 10; background: var(--bg-gradient); }
        .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; max-width: 1200px; margin: 0 auto; }
        .service-card { background: rgba(255,255,255,0.03); border: 1px solid var(--glass-border); border-radius: 15px; padding: 2.5rem; text-align: center; transition: transform 0.3s; }
        .service-card:hover { transform: translateY(-10px); border-color: var(--accent); box-shadow: 0 10px 30px var(--accent-glow); }
        .service-card i { font-size: 3rem; color: var(--accent); margin-bottom: 1.5rem; }
        .service-card h4 { font-size: 1.5rem; font-weight: 800; margin-bottom: 1rem; color: #fff; }
        .service-card p { color: var(--text-muted); line-height: 1.8; font-size: 1.1rem; }

        .about-section { padding: 5rem 5%; position: relative; z-index: 10; }
        .about-container { max-width: 1200px; margin: 0 auto; display: flex; align-items: center; gap: 4rem; flex-wrap: wrap; }
        .about-img { flex: 1; min-width: 300px; }
        .about-img img { width: 100%; border-radius: 15px; border: 2px solid var(--accent); box-shadow: 0 0 20px var(--accent-glow); }
        .about-text { flex: 2; min-width: 300px; }
        .about-text h2 { font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem; color: #fff; }
        .about-text h3 { color: var(--accent); font-weight: 700; margin-bottom: 1.5rem; font-size: 1.3rem; }
        .about-text p { color: var(--text-muted); line-height: 1.9; margin-bottom: 1.5rem; font-size: 1.2rem; }

        .trusted-section { padding: 4rem 0; background: rgba(0,0,0,0.3); overflow: hidden; position: relative; z-index: 10; }
        .marquee { display: flex; width: max-content; animation: scroll 20s linear infinite; gap: 4rem; padding: 0 2rem; direction: ltr; }
        .marquee img { height: 60px; object-fit: contain; filter: grayscale(100%) brightness(200%); opacity: 0.6; transition: 0.3s; }
        .marquee img:hover { filter: grayscale(0%); opacity: 1; }
        @keyframes scroll { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

        .footer { text-align: center; padding: 3rem 5%; border-top: 1px solid var(--glass-border); position: relative; z-index: 10; background: var(--bg-gradient); }
        .social-links { display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 2rem; }
        .social-links a { color: var(--text-muted); font-size: 1.8rem; transition: color 0.3s; }
        .social-links a:hover { color: var(--accent); }

        @media (max-width: 768px) {
            .nav-links { display: none; }
            .hero-title { font-size: 2.2rem; }
        }
    </style>
</head>
<body>
    <div id="particles-js" style="position:fixed; top:0; left:0; width:100%; height:100%; z-index:1; direction:ltr;"></div>

    <nav class="navbar">
        <div class="nav-brand">
            <i class="fa-solid fa-gear" style="color: var(--accent); margin-left: 0.5rem;"></i> إنجاز
        </div>
        <div class="nav-links">
            <a href="projects-ar.html">سابقة الأعمال</a>
            <a href="blog-ar.html">المدونة الهندسية</a>
            <a href="certificates-ar.html">الشهادات والاعتمادات</a>
            <a href="index.html" class="lang-switch" style="font-family: 'Inter', sans-serif;"><i class="fa-solid fa-globe"></i> English</a>
        </div>
    </nav>

    <section class="hero">
        <div class="hero-content">
            <h1 class="hero-title">إنجاز لحلول الأداء الهندسي</h1>
            <h2 class="hero-slogan">"أوقف النزيف، وضاعف أرباحك"</h2>
            <p class="hero-desc">نحوّل الإدارات الهندسية وأقسام الصيانة في مصنعك من مجرد "مراكز تكلفة" إلى "مراكز ربح" عبر التدقيق الاستراتيجي، وحلول إدارة الصيانة الرقمية (CMMS)، وتحسين العمليات التشغيلية.</p>
            <div class="hero-btns">
                <a href="projects-ar.html" class="btn" style="background: var(--accent); color: #0F2440; font-weight:800; padding: 1rem 2rem; text-decoration:none; border-radius: 30px;">تصفح سابقة الأعمال</a>
                <a href="mailto:Y_Tarek91@yahoo.com" class="btn" style="border: 2px solid var(--accent); color: var(--accent); font-weight:800; padding: 1rem 2rem; text-decoration:none; border-radius: 30px;">احجز استشارتك الآن</a>
            </div>
        </div>
    </section>

    <section class="metrics-bar">
        <div class="metric-card">
            <h3>+50M</h3>
            <p>جنيه تم توفيرها</p>
        </div>
        <div class="metric-card">
            <h3>80%</h3>
            <p>انخفاض في التوقف</p>
        </div>
        <div class="metric-card">
            <h3>98%</h3>
            <p>جاهزية الأصول</p>
        </div>
        <div class="metric-card">
            <h3>25%</h3>
            <p>توفير في الطاقة</p>
        </div>
    </section>

    <section class="services-section">
        <h2 class="section-title">خدماتنا الهندسية الأساسية</h2>
        <div class="services-grid">
            <div class="service-card">
                <i class="fa-solid fa-magnifying-glass-chart"></i>
                <h4>التدقيق الهندسي الشامل</h4>
                <p>فحص ميداني وتحليل دقيق لإجراءات الصيانة، استهلاك الطاقة، والعمليات التشغيلية لتحديد مواطن الهدر المالي وفرص التحسين الفورية.</p>
            </div>
            <div class="service-card">
                <i class="fa-solid fa-server"></i>
                <h4>تأسيس نظام الصيانة (CMMS)</h4>
                <p>التحول الرقمي الكامل من الصيانة الورقية العشوائية إلى نظام استباقي يضمن التتبع الكامل للأصول، قطع الغيار، وأوامر العمل.</p>
            </div>
            <div class="service-card">
                <i class="fa-solid fa-bolt"></i>
                <h4>تدقيق كفاءة الطاقة</h4>
                <p>تحليل متقدم لجودة الطاقة (Power Quality) واكتشاف التسريبات لتقليل فواتير الكهرباء والغاز بنسبة 15-25% بخطة استرداد سريعة.</p>
            </div>
            <div class="service-card">
                <i class="fa-solid fa-user-tie"></i>
                <h4>المدير الهندسي بالإنابة</h4>
                <p>قيادة استراتيجية بدوام جزئي لتوجيه فريقك المحلي، الإشراف على المقاولين، وتحقيق الأهداف المالية دون أعباء تعيين مدير عام بدوام كامل.</p>
            </div>
        </div>
    </section>

    <section class="about-section">
        <div class="about-container">
            <div class="about-img">
                <img src="assets/images/profile/yahya-logo.jpeg" alt="م. يحيى طارق">
            </div>
            <div class="about-text">
                <h2>تعرف على المؤسس</h2>
                <h3>م. يحيى طارق | خبير الأداء الهندسي والصيانة الصناعية</h3>
                <p>بخبرة عملية تمتد لـ 15 عاماً في القطاع الصناعي، أدار المهندس يحيى أكثر من 200 موقع تشمل مجمعات صناعية عملاقة وسلاسل تجارية ضخمة.</p>
                <p>حاصل على بكالوريوس الهندسة الكهربائية وشهادات معتمدة في إدارة المشاريع (Google) و(Lean Six Sigma)، يمتلك القدرة على ربط التعقيدات الفنية الهندسية بالأهداف المالية للإدارة العليا.</p>
                <a href="resume/Yahya_Tarek_Farag_Executive_Resume.pdf" download class="btn" style="border: 2px solid var(--accent); color: var(--accent); padding: 0.8rem 1.5rem; font-weight: 700; text-decoration:none; border-radius: 20px; display:inline-block; margin-top: 1rem;"><i class="fa-solid fa-download" style="margin-left: 0.5rem;"></i> تحميل السيرة الذاتية (CV)</a>
            </div>
        </div>
    </section>

    <section class="trusted-section">
        <h2 class="section-title" style="font-size: 1.8rem; margin-bottom: 2rem;">شركاء النجاح</h2>
        <!-- Marquee twice for seamless loop -->
        <div class="marquee">
            <img src="assets/images/brands/BLABAN.webp" alt="B.Laban">
            <img src="assets/images/brands/FARAG ALLAH.webp" alt="Faragalla">
            <img src="assets/images/brands/BAHEG.webp" alt="Baheeg">
            <img src="assets/images/brands/AM SHALTAT.webp" alt="Am Shaltat">
            <img src="assets/images/brands/BLALM.webp" alt="Chicken Balalm">
            <img src="assets/images/brands/MORTADELLA.webp" alt="Mortadella">
            
            <img src="assets/images/brands/BLABAN.webp" alt="B.Laban">
            <img src="assets/images/brands/FARAG ALLAH.webp" alt="Faragalla">
            <img src="assets/images/brands/BAHEG.webp" alt="Baheeg">
            <img src="assets/images/brands/AM SHALTAT.webp" alt="Am Shaltat">
            <img src="assets/images/brands/BLALM.webp" alt="Chicken Balalm">
            <img src="assets/images/brands/MORTADELLA.webp" alt="Mortadella">
        </div>
    </section>

    <footer class="footer">
        <h3 style="color: #fff; margin-bottom: 1.5rem; font-size: 1.8rem;">هل أنت مستعد لإيقاف النزيف؟</h3>
        <div class="social-links">
            <a href="https://www.linkedin.com/in/yahyatarekfarag/" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
            <a href="mailto:Y_Tarek91@yahoo.com"><i class="fa-solid fa-envelope"></i></a>
            <a href="https://wa.me/201080801708" target="_blank"><i class="fa-brands fa-whatsapp"></i></a>
        </div>
        <p style="color: var(--text-muted);">&copy; 2026 إنجاز لحلول الأداء الهندسي. جميع الحقوق محفوظة.</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        window.addEventListener('load', () => {
            if(typeof particlesJS !== 'undefined') {
                particlesJS('particles-js', {
                  "particles": {
                    "number": { "value": 50, "density": { "enable": true, "value_area": 800 } },
                    "color": { "value": "#F28C28" },
                    "shape": { "type": "circle" },
                    "opacity": { "value": 0.5, "random": false },
                    "size": { "value": 3, "random": true },
                    "line_linked": { "enable": true, "distance": 150, "color": "#F28C28", "opacity": 0.2, "width": 1 },
                    "move": { "enable": true, "speed": 1.5, "direction": "none", "random": false, "straight": false, "out_mode": "out", "bounce": false }
                  },
                  "interactivity": {
                    "detect_on": "canvas",
                    "events": { "onhover": { "enable": true, "mode": "grab" }, "onclick": { "enable": true, "mode": "push" }, "resize": true },
                    "modes": { "grab": { "distance": 140, "line_linked": { "opacity": 1 } }, "push": { "particles_nb": 4 } }
                  },
                  "retina_detect": true
                });
            }
        });
    </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_en)

with open('index-ar.html', 'w', encoding='utf-8') as f:
    f.write(html_ar)

print("New Homepage Layout Implemented Successfully!")
