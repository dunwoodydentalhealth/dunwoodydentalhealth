import itertools,re
BRAND_LINKS="""https://studio.hubhopper.com/podcasts/484745/details
https://www.airgigs.com/user/dunwoodydentalhealth
https://lnk.bio/dunwoodydentalhealth
https://www.letsknowit.com/dunwoodydentalhealth
https://leetcode.com/u/dunwoodydentalhealth/
https://audio.com/dunwoody-dental-health
https://www.zupyak.com/u/Dunwoody-Dental-Health/
https://orcid.org/my-orcid?emailVerified=true&orcid=0009-0005-3751-961X
https://www.audible.in/podcast/Dunwoody-Dental-Health/B0H2BQDDWB
https://metacast.app/itunes/import/6799878111
https://pocketcasts.com/podcast/dunwoody-dental-health/bf0817d0-6336-013f-aebf-0affe66a1943
https://meta.stackexchange.com/users/1929019/dunwoody-dental-health
https://news.prfree.org/@dunwoodydentalhealth/dunwoody-dental-health-strengthens-commitment-to-patient-centered-dental-care-ygp1of97ljb1
https://pressrelease.in/newsroom/dunwoody-dental-health-reaffirms-focus-on-comfort-and-quality-care-6486ad0b
https://www.marketpressrelease.com/managepr.php
https://dunwoodydentalhealth.carrd.co/
https://dunwoodydentalhealth.github.io/
https://articles.abilogic.com/817330/what-makes-dunwoody-dental-health.html
https://www.codifypedia.com/blog/Dunwoody-Dental-Health-on-Why-Regular-Dental-Checkups-Matter-More-Than-People-Think
https://wtoregister.com/en/profile/company/articles""".split()
SOCIAL=[("Linktree","https://linktr.ee/dunwoodydentalhealth"),("Crunchbase","https://www.crunchbase.com/organization/dunwoody-dental-health"),("GitHub","https://github.com/dunwoodydentalhealth"),("Bluesky","http://bsky.app/profile/dunwoodydental.bsky.social"),("Apple Podcasts","https://podcasts.apple.com/us/podcast/id6799878111"),("Spotify","https://open.spotify.com/show/033QrRmAuR9vrLFo2fSF3w"),("TuneIn","https://tunein.com/radio/p4786538/"),("Facebook","https://www.facebook.com/DunwoodyDentalHealth/"),("Instagram","https://www.instagram.com/dunwoodydentalhealth/?hl=en"),("X","https://x.com/Dunwoody_dds"),("YouTube","https://www.youtube.com/@DunwoodyDentalHealth"),("TikTok","https://www.tiktok.com/@dunwoodydentalhealth")]
cyc=itertools.cycle(BRAND_LINKS)
def B(m): return f'<a class="brand-link" href="{next(cyc)}" target="_blank" rel="noopener">Dunwoody Dental Health</a>'
def link(html): return re.sub(r'\{\{B\}\}',B,html)
SITE="https://dunwoodydentalhealth.netlify.app"
import json
def schema(fn):
    if fn=="thanks.html": return ""
    org={"@type":"Dentist","@id":SITE+"/#org","name":"Dunwoody Dental Health","url":SITE+"/","logo":SITE+"/assets/logo.jpg","image":SITE+"/assets/og-image.jpg","description":"Modern dental care designed around your schedule and comfort.","sameAs":[u for n,u in SOCIAL]+BRAND_LINKS[:0]}
    data={"@context":"https://schema.org","@graph":[org,{"@type":"WebSite","@id":SITE+"/#site","url":SITE+"/","name":"Dunwoody Dental Health","publisher":{"@id":SITE+"/#org"}}]}
    if fn=="about.html": data["@graph"].append({"@type":"AboutPage","url":SITE+"/about.html","name":"About Us","about":{"@id":SITE+"/#org"}})
    if fn=="contact.html": data["@graph"].append({"@type":"ContactPage","url":SITE+"/contact.html","name":"Contact Us","about":{"@id":SITE+"/#org"}})
    return '<script type="application/ld+json">'+json.dumps(data)+'</script>'
def page(fn,title,desc,body,active):
    nav=''.join(f'<a href="{h}"{" aria-current=\"page\"" if h==active else ""}>{t}</a>' for h,t in [("index.html","Home"),("about.html","About Us"),("contact.html","Contact Us")])
    soc=''.join(f'<a href="{u}" target="_blank" rel="noopener me">{n}</a>' for n,u in SOCIAL)
    html=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{"" if fn=="index.html" else fn}"><meta name="robots" content="{"noindex,follow" if fn=="thanks.html" else "index,follow,max-image-preview:large"}"><meta name="theme-color" content="#1AA9E1"><meta name="author" content="Dunwoody Dental Health">{schema(fn)}
<link rel="icon" href="favicon.ico" sizes="32x32"><link rel="icon" type="image/png" href="assets/favicon.png"><link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta property="og:type" content="website"><meta property="og:site_name" content="Dunwoody Dental Health"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{SITE}/assets/og-image.jpg"><meta property="og:url" content="{SITE}/{"" if fn=="index.html" else fn}"><meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{SITE}/assets/og-image.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700;900&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css"></head><body>
<header class="site-header"><div class="wrap bar"><a href="index.html" class="logo"><img src="assets/logo.jpg" alt="Dunwoody Dental Health logo" width="220"></a>
<button class="menu-btn" aria-label="Open menu" aria-expanded="false">Menu</button><nav class="nav" aria-label="Main">{nav}<a class="btn btn-sm" href="contact.html#book">Book a visit</a></nav></div></header>
<main>{link(body)}</main>
<footer class="site-footer"><div class="wrap foot"><div><img src="assets/logo.jpg" alt="Dunwoody Dental Health" width="200"><p>{link("{{B}} offers modern, comfortable and transparent dental care for patients of all ages.")}</p></div>
<div><h3>Pages</h3><p class="flinks">{nav}</p></div><div><h3>Follow us</h3><p class="flinks">{soc}</p></div></div>
<div class="wrap copy">&copy; <span id="yr">2026</span> Dunwoody Dental Health. All rights reserved.</div></footer>
<script src="js/main.js"></script></body></html>'''
    open(fn,'w').write(html)

def fig(n,alt,cls=""): return f'<figure class="ph {cls}"><img src="images/patient-{n}.jpg" alt="{alt}" loading="lazy" onerror="this.remove()"></figure>'

why=[("Fast and Efficient Care","Your visit should feel organized from start to finish. We keep things moving smoothly and completely respect your busy daily schedule."),("Same Day Dentistry","Need treatment urgently? We can often take care of your dental procedures on the exact same day, helping you avoid unnecessary extra visits."),("Modern Technology","Digital scans and advanced imaging help us diagnose issues clearly, explain treatment paths better, and perform procedures much more efficiently."),("Clear and Transparent Communication","You will always know what we see, what we recommend, and what your options are, without ever feeling rushed or pushed into decisions.")]
ben=[("Reduced Dental Anxiety","Our gentle techniques, calming environment, and supportive staff ensure that even nervous patients feel completely safe, relaxed, and comfortable throughout their visit."),("Flexible Financial Solutions","We offer convenient payment plans, membership options, and accept major PPO insurance to ensure quality dental care easily fits your personal budget."),("Save Valuable Time","With streamlined appointments and same-day treatment capabilities, we minimize time away from your work and family commitments while maximizing oral health outcomes."),("Long-Term Oral Health","Our proactive approach focuses on preventing future complications, ensuring your teeth and gums remain strong, healthy, and functional for many years to come.")]
svc=["Preventive Care & Cleanings","Comprehensive Dental Exams","Fillings & Crowns","Dental Implants","Emergency Dentistry","Cosmetic Dentistry","Clear Aligners","Oral Surgery"]
cards=lambda L:''.join(f'<article class="card"><h3>{t}</h3><p>{d}</p></article>' for t,d in L)

home=f'''
<section class="hero"><div class="wrap hero-grid"><div>
<img class="hero-logo" src="assets/logo.jpg" alt="Dunwoody Dental Health logo" width="420">
<h1>Modern Dental Care Designed Around Your Schedule And Comfort</h1>
<p class="lead">Preventive care, implants, aligners and emergency visits, all explained clearly and delivered on your time.</p>
<p class="cta"><a class="btn" href="contact.html#book">Book an appointment</a><a class="btn btn-ghost" href="#services">See our services</a></p></div>
{fig(1,"Smiling patient at a dental clinic","arch hero-img")}</div></section>

<section class="sec"><div class="wrap split">{fig(2,"Dentist speaking with a patient","arch")}<div>
<h2>About Dunwoody Dental Health</h2>
<p>{{{{B}}}} is a trusted dental clinic dedicated to providing exceptional, patient-centered care in a welcoming and modern environment. Serving our local community with pride, the practice offers comprehensive dental services, including preventive care, cosmetic dentistry, dental implants, restorative treatments, emergency dentistry, and clear aligners. With a team of experienced professionals, advanced dental technology, and a commitment to honest communication, {{{{B}}}} ensures every patient receives personalized treatment tailored to their unique needs. Our focus on comfort, quality, and long-term oral health has earned us a reputation for compassionate care, helping patients of all ages achieve healthy, confident smiles. Whether you need a routine cleaning or advanced restorative work, we strive to make every visit efficient, transparent, and completely stress-free.</p>
<p><a class="textlink" href="about.html">More about our practice</a></p></div></div></section>

<section class="sec tint"><div class="wrap"><h2>Why choose us</h2><div class="grid4">{cards(why)}</div></div></section>

<section class="sec" id="services"><div class="wrap"><h2>Services</h2><ul class="svc">{''.join(f'<li>{s}</li>' for s in svc)}</ul></div></section>

<section class="sec tint"><div class="wrap mv">
<div><h2>My mission</h2><p>The mission of {{{{B}}}} is to deliver exceptional, compassionate, and personalized dental care that empowers patients to achieve optimal oral health and radiant smiles. We are committed to fostering a welcoming environment where open communication, modern technology, and clinical excellence meet. By prioritizing patient education and comfort, we aim to eliminate dental anxiety and build lasting relationships built on mutual trust. Every member of our team is dedicated to treating individuals with the utmost respect, ensuring that clinical recommendations always align with the personal needs and wellness goals of each patient. We strive to make quality dentistry accessible, efficient, and stress-free for families and individuals throughout our community, helping everyone walk out with renewed confidence.</p></div>
<div><h2>My vision</h2><p>Our vision is to be the leading dental healthcare provider recognized for clinical excellence, patient-focused innovation, and unwavering community trust. We aspire to redefine the traditional dental experience by seamlessly integrating advanced diagnostic technology, efficient treatment workflows, and a deeply compassionate approach. {{{{B}}}} envisions a future where every patient looks forward to maintaining their dental health because they experience absolute comfort, transparent guidance, and predictable results. Through continuous professional growth, modern practices, and a genuine passion for healthy smiles, we aim to set a new standard for comprehensive dental wellness. We hope to inspire lifelong oral health habits across generations, serving as a reliable medical touchstone for families who value quality and integrity.</p></div></div></section>

<section class="sec"><div class="wrap"><h2>Benefits</h2><div class="grid4">{cards(ben)}</div>
<div class="gallery">{fig(3,"Happy patient after a dental visit","arch")}{fig(4,"Family smiling together","arch")}{fig(5,"Patient receiving a gentle checkup","arch")}</div></div></section>

<section class="sec band"><div class="wrap center"><h2>Ready for a calmer dental visit?</h2><p class="cta"><a class="btn btn-light" href="contact.html#book">Book an appointment</a></p></div></section>'''
page("index.html","Dunwoody Dental Health | Modern Dental Care Around Your Schedule","Modern dental care designed around your schedule and comfort. Preventive care, implants, clear aligners, emergency dentistry and more at Dunwoody Dental Health.",home,"index.html")

paras=["Welcome to {{B}}, where your smile, comfort, and long-term health are always our top priorities. We believe that visiting the dentist should be a positive, stress-free experience that seamlessly fits into your busy lifestyle. From the moment you walk through our doors, our dedicated team is committed to providing exceptional, patient-centered care in a warm, modern, and welcoming environment.",
"Our practice was built on a simple yet powerful philosophy: dentistry should be honest, efficient, and tailored to the individual. We know that many people feel hesitant or anxious about visiting the dentist, which is why we have designed our entire practice around your ease and convenience. From our streamlined check-in processes to our transparent communication style, we ensure you always know what to expect. There are no hidden surprises, no rushed appointments, and no pressure. Instead, you receive clear explanations, expert guidance, and personalized care from professionals who truly listen.",
"At {{B}}, we offer a comprehensive spectrum of dental services under one roof. Whether you need routine preventive cleanings and exams, restorative fillings and crowns, advanced dental implants, cosmetic transformations, or urgent emergency care, our experienced clinical team has the expertise to handle your needs. We utilize state-of-the-art dental technology, including digital scans and advanced imaging, to diagnose conditions accurately and plan treatments precisely. This modern technology not only improves the safety and accuracy of our procedures but also allows us to complete many treatments on the same day, saving you valuable time and extra trips to the clinic.",
"We recognize that every patient is unique, which is why we never take a one-size-fits-all approach. Your treatment plan is carefully customized to match your specific dental history, personal goals, and comfort level. Our team takes the time to educate you on your oral health, showing you digital images so you can clearly understand what we see and why a specific treatment is recommended. We want you to feel confident and empowered as an active partner in your dental care journey.",
"Affordability and accessibility are core pillars of our practice. We understand that navigating dental insurance and payment options can often feel overwhelming. That is why our knowledgeable staff works closely with you to verify your benefits, explain coverage details clearly, and maximize your insurance plans. For patients without traditional insurance, we offer flexible alternative solutions, including custom membership plans and financing options through trusted providers, ensuring that financial constraints never stand in the way of a healthy smile.",
"Beyond our clinical expertise, what truly sets {{B}} apart is our people. Our dentists, hygienists, and front desk coordinators share a genuine passion for helping others. We treat every patient like family, offering a compassionate touch and an encouraging word to make your time with us enjoyable. Whether we are caring for an elderly family member, a nervous first-time visitor, or a busy professional looking for efficient care, our dedication never wavers.",
"We invite you to experience a new standard of dental care where your schedule is respected, your comfort is prioritized, and your smile is always in expert hands. Come visit {{B}} and discover how easy, modern, and rewarding going to the dentist can truly be."]
P=lambda i:f'<p>{paras[i]}</p>'
about=f'''<section class="page-head"><div class="wrap"><h1>About Us</h1><p class="lead">Honest, efficient dentistry tailored to the individual.</p></div></section>
<section class="sec"><div class="wrap split">{fig(2,"Dentist and patient talking","arch")}<div>{P(0)}{P(1)}</div></div></section>
<section class="sec tint"><div class="wrap split rev"><div>{P(2)}{P(3)}</div>{fig(3,"Patient looking at digital scans with the dentist","arch")}</div></section>
<section class="sec"><div class="wrap split">{fig(4,"Friendly dental team with a patient","arch")}<div>{P(4)}{P(5)}</div></div></section>
<section class="sec band"><div class="wrap center"><p class="big">{paras[6]}</p><p class="cta"><a class="btn btn-light" href="contact.html#book">Book an appointment</a></p></div></section>'''

from urllib.parse import urlparse
def lab(u):
    h=urlparse(u).netloc.replace("www.","");return h
web='<section class="sec tint"><div class="wrap"><h2>Find us around the web</h2><ul class="svc web">'+''.join(f'<li><a class="brand-link" href="{u}" target="_blank" rel="noopener">Dunwoody Dental Health</a> on {lab(u)}</li>' for u in BRAND_LINKS)+'</ul></div></section>'
about=about.replace('<section class="sec band">',web+'<section class="sec band">',1)
page("about.html","About Us | Dunwoody Dental Health","Learn about Dunwoody Dental Health: honest, efficient, patient-centered dentistry with modern technology, flexible payment options and a caring team.",about,"about.html")

contact='''<section class="page-head"><div class="wrap"><h1>Contact Us</h1><p class="lead">Tell us what you need and our team will get back to you to arrange your visit.</p></div></section>
<section class="sec" id="book"><div class="wrap split">
<form class="form" name="contact" method="POST" action="/thanks.html" data-netlify="true" netlify-honeypot="bot-field" novalidate>
<input type="hidden" name="form-name" value="contact"><p hidden><label>Do not fill this out <input name="bot-field"></label></p>
<label>Full name<input name="name" required autocomplete="name"></label>
<label>Email<input type="email" name="email" required autocomplete="email"></label>
<label>Phone<input type="tel" name="phone" autocomplete="tel"></label>
<label>Service needed<select name="service"><option>Preventive Care &amp; Cleanings</option><option>Comprehensive Dental Exam</option><option>Fillings &amp; Crowns</option><option>Dental Implants</option><option>Emergency Dentistry</option><option>Cosmetic Dentistry</option><option>Clear Aligners</option><option>Oral Surgery</option></select></label>
<label>Message<textarea name="message" rows="5" required></textarea></label>
<button class="btn" type="submit">Send message</button><p class="err" role="alert" hidden>Please fill in your name, a valid email and a message.</p></form>
<div><h2>Stay connected</h2><p>Follow {{B}} for dental tips, podcasts and practice news, or message us on any channel below.</p>
<p class="flinks big-links">'''+''.join(f'<a href="{u}" target="_blank" rel="noopener me">{n}</a>' for n,u in SOCIAL)+'''</p>'''+fig(5,"Welcoming dental reception","arch")+'''</div></div></section>'''
page("contact.html","Contact Us | Dunwoody Dental Health","Book a visit or ask a question. Contact Dunwoody Dental Health and our team will get back to you.",contact,"contact.html")
page("thanks.html","Thank you | Dunwoody Dental Health","Your message was sent.",'<section class="page-head"><div class="wrap"><h1>Thank you</h1><p class="lead">Your message was sent. Our team will reply soon.</p><p class="cta"><a class="btn" href="index.html">Back to home</a></p></div></section>',"")

import datetime
d=datetime.date.today().isoformat()
urls=[("",1.0),("about.html",0.8),("contact.html",0.7)]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{d}</lastmod><changefreq>monthly</changefreq><priority>{p}</priority></url>\n" for u,p in urls)+'</urlset>\n')
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nDisallow: /thanks.html\n\nSitemap: {SITE}/sitemap.xml\n")
