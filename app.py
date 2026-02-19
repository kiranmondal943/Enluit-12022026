import streamlit as st
import zipfile
import io
import json
import datetime
import re
import requests

# --- 0. STATE MANAGEMENT ---
def init_state(key, default_val):
    if key not in st.session_state:
        st.session_state[key] = default_val

init_state('hero_h', "Stop Paying Rent for Your Website.")
init_state('hero_sub', "The Titan Engine is the world’s first 0.1s website architecture that runs on $0 monthly fees. Pay once. Own it forever.")
init_state('about_h', "Control Your Empire")
init_state('about_short', "No WordPress dashboard. No plugins to update. Just open your private Google Sheet, change a text, and watch your site update globally in seconds.")
init_state('feat_data', "bolt | The Performance Pillar | **0.1s High-Velocity Loading**. While traditional sites take 3–5s, Titan loads instantly.\nwallet | The Economic Pillar | **$0 Monthly Fees**. We eliminated hosting subscriptions.\ntable | The Functional Pillar | **Google Sheets CMS**. Update prices and photos directly from a simple spreadsheet.\nshield | The Authority Pillar | **Unhackable Security**. Zero-DB Architecture removes the hacker's primary entry point.\nlayers | The Reliability Pillar | **Global Edge Deployment**. Distributed across 100+ servers worldwide.\nstar | The Conversion Pillar | **One-Tap WhatsApp**. Direct-to-Chat technology.")

# --- 1. APP CONFIGURATION ---
st.set_page_config(page_title="Titan v39.2 | Fixed Core", layout="wide", page_icon="⚡", initial_sidebar_state="expanded")

# --- 2. CSS ENGINE ---
st.markdown("""
    <style>
    :root { --primary: #0f172a; --accent: #ef4444; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] { background-color: #ffffff !important; border: 1px solid #cbd5e1 !important; color: #0f172a !important; border-radius: 8px !important; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5rem; background: linear-gradient(135deg, #0f172a 0%, #334155 100%); color: white; font-weight: 800; border: none; box-shadow: 0 4px 15px rgba(15, 23, 42, 0.3); text-transform: uppercase; letter-spacing: 1px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v39.2 | Stable Release")
    st.divider()
    
    with st.expander("🤖 Titan AI Generator"):
        groq_key = st.text_input("Groq API Key", type="password")
        biz_desc = st.text_input("Business Description")
        if st.button("✨ Generate Copy"):
            if groq_key and biz_desc:
                try:
                    url = "https://api.groq.com/openai/v1/chat/completions"
                    headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
                    prompt = f"Return JSON for '{biz_desc}': hero_h, hero_sub, about_h, about_short, feat_data (icon|Title|Desc format)."
                    data = {"messages": [{"role": "user", "content": prompt}], "model": "llama-3.1-8b-instant", "response_format": {"type": "json_object"}}
                    resp = requests.post(url, headers=headers, json=data).json()['choices'][0]['message']['content']
                    for k,v in json.loads(resp).items(): st.session_state[k] = str(v)
                    st.success("Generated! Refreshing..."); st.rerun()
                except: st.error("AI Error")

    with st.expander("🎨 Design Studio", expanded=True):
        theme_mode = st.selectbox("Base Theme", ["Clean Corporate", "Midnight SaaS", "Glassmorphism", "Stark Minimalist"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary", "#0F172A") 
        s_color = c2.color_picker("Action", "#EF4444")  
        h_font = st.selectbox("Headings", ["Montserrat", "Space Grotesk", "Oswald"])
        b_font = st.selectbox("Body", ["Inter", "Open Sans", "Roboto"])
        hero_layout = st.selectbox("Alignment", ["Left", "Center"])
        border_rad = "8px"
        anim_type = st.selectbox("Animation", ["Fade Up", "Zoom In", "None"])

    with st.expander("🧩 Modules"):
        show_hero = st.checkbox("Hero", True); show_stats = st.checkbox("Stats", True); show_features = st.checkbox("Features", True)
        show_pricing = st.checkbox("Pricing", True); show_inventory = st.checkbox("Store", True); show_blog = st.checkbox("Blog", True)
        show_gallery = st.checkbox("About", True); show_testimonials = st.checkbox("Testimonials", True); show_faq = st.checkbox("FAQ", True)
        show_cta = st.checkbox("CTA", True); show_booking = st.checkbox("Booking", True)

    with st.expander("⚙️ SEO"):
        seo_area = st.text_input("Service Area", "Global"); gsc_tag = st.text_input("G-Verify ID"); og_image = st.text_input("OG Image URL")

# --- 4. INPUT TABS ---
st.title("🏗️ StopWebRent Builder v39.2")
tabs = st.tabs(["1. Identity", "2. Content", "3. Marketing", "4. Pricing", "5. Store", "6. Booking", "7. Blog", "8. Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "StopWebRent.com")
        biz_phone = st.text_input("Phone", "966572562151")
        biz_email = st.text_input("Email", "hello@kaydiemscriptlab.com")
    with c2:
        prod_url = st.text_input("URL", "https://www.stopwebrent.com")
        biz_addr = st.text_area("Address", "Kaydiem Script Lab, Kolkata, India", height=100)
        map_iframe = st.text_area("Map Embed", placeholder='<iframe src="..."></iframe>', height=100)
        seo_d = st.text_area("Meta Desc", "Stop paying monthly fees.", height=100)
        logo_url = st.text_input("Logo URL")

    pwa_short = st.text_input("App Name", "SWR App"); pwa_icon = st.text_input("App Icon", logo_url)
    lang_sheet = st.text_input("Lang Sheet CSV")
    c1,c2,c3 = st.columns(3); fb_link = c1.text_input("FB"); x_link = c2.text_input("X"); wa_num = c3.text_input("WhatsApp", "966572562151")
    li_link = st.text_input("LinkedIn"); yt_link = st.text_input("YouTube")

with tabs[1]:
    hero_h = st.text_input("Headline", st.session_state.hero_h)
    hero_sub = st.text_input("Subtext", st.session_state.hero_sub)
    hero_video_id = st.text_input("YT Video ID")
    c1,c2,c3 = st.columns(3); hero_img_1 = c1.text_input("Img 1","https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600"); hero_img_2 = c2.text_input("Img 2"); hero_img_3 = c3.text_input("Img 3")
    
    c1,c2,c3 = st.columns(3)
    stat_1 = c1.text_input("Stat 1", "0.1s"); label_1 = c1.text_input("L1", "Speed")
    stat_2 = c2.text_input("Stat 2", "$0"); label_2 = c2.text_input("L2", "Fees")
    stat_3 = c3.text_input("Stat 3", "100%"); label_3 = c3.text_input("L3", "Owned")
    
    f_title = st.text_input("Feat. Title", "Value Pillars")
    feat_data_input = st.text_area("Features", st.session_state.feat_data, height=150)
    about_h_in = st.text_input("About Title", st.session_state.about_h)
    about_short_in = st.text_area("About Short", st.session_state.about_short)
    about_long = st.text_area("About Long", "Full content...", height=150)
    about_img = st.text_input("About Img", "https://images.unsplash.com/photo-1543286386-713df548e9cc?q=80&w=1600")

with tabs[2]:
    top_bar_enabled = st.checkbox("Top Bar"); top_bar_text = st.text_input("Bar Text", "Launch Sale!"); top_bar_link = st.text_input("Bar Link", "#pricing")
    popup_enabled = st.checkbox("Exit Popup"); popup_delay = st.slider("Delay", 1,30,5); popup_title = st.text_input("Pop Title", "Wait!"); popup_text = st.text_input("Pop Text", "Get 10% Off"); popup_cta = st.text_input("Pop Button", "Claim")

with tabs[3]:
    c1,c2,c3 = st.columns(3)
    titan_price = c1.text_input("Titan", "$199"); titan_mo = c1.text_input("Titan/mo", "$0")
    wix_name = c2.text_input("Comp", "Wix"); wix_mo = c2.text_input("Comp/mo", "$29")
    save_val = c3.text_input("Savings", "$1,466")

with tabs[4]:
    sheet_url = st.text_input("Store CSV", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Default Prod Img", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800")
    c1,c2 = st.columns(2); paypal_link = c1.text_input("PayPal"); upi_id = c2.text_input("UPI")

with tabs[5]:
    booking_embed = st.text_area("Calendly Code", height=100); booking_title = st.text_input("Book Title"); booking_desc = st.text_input("Book Desc")

with tabs[6]:
    blog_sheet_url = st.text_input("Blog CSV"); blog_hero_title = st.text_input("Blog Hero", "Insights"); blog_hero_sub = st.text_input("Blog Sub", "Updates")

with tabs[7]:
    testi_data = st.text_area("Testimonials", "Name | Quote"); faq_data = st.text_area("FAQ", "Q? ? A"); priv_txt = st.text_area("Privacy"); term_txt = st.text_area("Terms")

# --- 5. COMPILER FUNCTIONS ---

def format_text(text):
    if not text: return ""
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    return text.replace('\n', '<br>')

def gen_schema():
    s = {"@context":"https://schema.org","@type":"LocalBusiness","name":biz_name,"url":prod_url}
    return f'<script type="application/ld+json">{json.dumps(s)}</script>'

def gen_pwa_manifest():
    return json.dumps({"name":biz_name,"short_name":pwa_short,"start_url":"./index.html","display":"standalone","theme_color":p_color,"icons":[{"src":pwa_icon,"sizes":"512x512","type":"image/png"}]})

def gen_sw():
    return """self.addEventListener('install',e=>{e.waitUntil(caches.open('v1').then(c=>c.addAll(['./index.html'])));});self.addEventListener('fetch',e=>{e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)));});"""

def gen_popup():
    if not popup_enabled: return ""
    return f"""
    <div id="lead-popup" style="display:none;position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);background:var(--card);padding:2rem;z-index:2000;border-radius:12px;box-shadow:0 20px 50px rgba(0,0,0,0.5);width:90%;max-width:400px;text-align:center;">
        <span onclick="document.getElementById('lead-popup').style.display='none'" style="position:absolute;top:10px;right:15px;cursor:pointer;font-size:1.5rem;">&times;</span>
        <h2>{popup_title}</h2><p>{popup_text}</p>
        <a href="https://wa.me/{wa_num}" class="btn btn-accent" style="width:100%">{popup_cta}</a>
    </div>
    """

def get_theme_css():
    bg, txt, card = "#ffffff", "#0f172a", "rgba(255,255,255,0.9)"
    if "Midnight" in theme_mode: bg, txt, card = "#0f172a", "#f8fafc", "rgba(30,41,59,0.9)"
    align = "center" if hero_layout == "Center" else "left"
    
    return f"""
    :root {{ --p: {p_color}; --s: {s_color}; --bg: {bg}; --txt: {txt}; --card: {card}; --radius: {border_rad}; --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif; }}
    * {{ box-sizing: border-box; }} html {{ scroll-behavior: smooth; }}
    body {{ background: var(--bg); color: var(--txt); font-family: var(--b-font); margin: 0; }}
    h1,h2,h3 {{ font-family: var(--h-font); color: var(--p); }}
    .container {{ max-width: 1280px; margin: 0 auto; padding: 0 20px; }}
    .btn {{ display: inline-block; padding: 1rem 2rem; border-radius: var(--radius); background: var(--s); color: white; text-decoration: none; font-weight: bold; border:none; cursor:pointer; }}
    .btn-primary {{ background: var(--p); }}
    
    nav {{ position: fixed; top: 0; width: 100%; z-index: 1000; background: var(--card); backdrop-filter: blur(10px); padding: 1rem 0; border-bottom:1px solid rgba(0,0,0,0.1); }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links a {{ margin-left: 1.5rem; text-decoration: none; color: var(--txt); font-weight: 600; }}
    
    .hero {{ position: relative; min-height: 80vh; display: flex; align-items: center; justify-content: center; background: var(--p); text-align: {align}; padding-top:80px; }}
    .hero h1 {{ color: white; font-size: clamp(2.5rem, 5vw, 4.5rem); }}
    .hero p {{ color: rgba(255,255,255,0.9); font-size: 1.2rem; max-width: 700px; margin: 0 auto 2rem; }}
    .hero-overlay {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1; }}
    .hero-content {{ position: relative; z-index: 2; width: 100%; }}
    .carousel-slide {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0; transition: opacity 1s; }}
    .carousel-slide.active {{ opacity: 1; }}

    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }}
    .card {{ background: var(--card); padding: 2rem; border-radius: var(--radius); border: 1px solid rgba(128,128,128,0.1); }}
    .about-grid, .contact-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }}
    
    footer {{ background: var(--p); color: white; padding: 4rem 0; margin-top: auto; }}
    footer a {{ color: rgba(255,255,255,0.7); text-decoration: none; display: block; margin-bottom: 0.5rem; }}
    
    .pricing-table {{ width: 100%; border-collapse: collapse; }}
    .pricing-table th {{ background: var(--p); color: white; padding: 1rem; }}
    .pricing-table td {{ padding: 1rem; border-bottom: 1px solid #eee; }}
    
    #cart-float {{ position: fixed; bottom: 30px; right: 90px; background: var(--p); color: white; padding: 15px; border-radius: 50px; z-index: 998; cursor: pointer; }}
    #cart-modal {{ display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%,-50%); background: white; padding: 2rem; z-index: 1001; border-radius: 12px; width: 90%; max-width: 400px; color:black; }}
    .share-row a {{ margin-right: 10px; display: inline-block; }}

    @media (max-width: 768px) {{
        .nav-links {{ display: none; }}
        .about-grid, .contact-grid {{ grid-template-columns: 1fr; gap: 2rem; }}
    }}
    .reveal {{ opacity: 0; transform: translateY(30px); transition: 0.8s; }} .reveal.active {{ opacity: 1; transform: translateY(0); }}
    """

def gen_common_js():
    return f"""
    <script>
    window.addEventListener('scroll',()=>{{document.querySelectorAll('.reveal').forEach(r=>{{if(r.getBoundingClientRect().top<window.innerHeight-100)r.classList.add('active')}})}});
    setTimeout(()=>{{if(document.getElementById('lead-popup'))document.getElementById('lead-popup').style.display='block'}},{popup_delay*1000});
    
    let cart = JSON.parse(localStorage.getItem('titanCart')) || [];
    function renderCart() {{ document.getElementById('cart-count').innerText=cart.length; if(cart.length) document.getElementById('cart-float').style.display='block'; }}
    function addToCart(n,p) {{ cart.push({{name:n,price:p}}); localStorage.setItem('titanCart',JSON.stringify(cart)); renderCart(); alert('Added'); }}
    function checkout() {{ 
        let msg="Order:%0A"; cart.forEach(i=>{{msg+=`- ${{i.name}} (${{i.price}})%0A`}}); 
        window.open(`https://wa.me/{wa_num}?text=${{msg}}`); 
    }}
    window.onload=renderCart;
    </script>
    """

def get_simple_icon(name):
    name = name.lower().strip()
    path = "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"
    if "bolt" in name: path = "M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"
    return f'<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="{path}"/></svg>'

# --- CONTENT BLOCKS ---
def gen_hero():
    media = f"""<div class="carousel-slide active" style="background-image:url('{hero_img_1}')"></div><div class="carousel-slide" style="background-image:url('{hero_img_2}')"></div><script>let s=document.querySelectorAll('.carousel-slide'),c=0;setInterval(()=>{{s[c].classList.remove('active');c=(c+1)%s.length;s[c].classList.add('active')}},4000)</script>"""
    return f"""<section class="hero"><div class="hero-overlay"></div>{media}<div class="container hero-content"><h1>{hero_h}</h1><p>{hero_sub}</p><a href="#pricing" class="btn btn-accent">See Pricing</a></div></section>"""

def gen_features():
    c = ""
    for l in feat_data_input.split('\n'):
        p = l.split('|')
        if len(p)>=3: c+=f"""<div class="card reveal"><div style="color:var(--s);margin-bottom:1rem;">{get_simple_icon(p[0])}</div><h3>{p[1]}</h3><div>{format_text(p[2])}</div></div>"""
    return f"""<section id="features"><div class="container"><h2 style="text-align:center;margin-bottom:3rem;">{f_title}</h2><div class="grid-3">{c}</div></div></section>"""

def gen_stats():
    return f"""<div style="background:var(--p);color:white;padding:3rem 0;text-align:center;"><div class="container grid-3"><div class="reveal"><h3>{stat_1}</h3><p>{label_1}</p></div><div class="reveal"><h3>{stat_2}</h3><p>{label_2}</p></div><div class="reveal"><h3>{stat_3}</h3><p>{label_3}</p></div></div></div>"""

def gen_pricing():
    if not show_pricing: return ""
    return f"""<section id="pricing"><div class="container"><h2 style="text-align:center;">Pricing</h2><div class="pricing-wrapper"><table class="pricing-table"><thead><tr><th>Category</th><th style="background:var(--s);">Titan</th><th>{wix_name}</th></tr></thead><tbody><tr><td>Setup</td><td>{titan_price}</td><td>$0</td></tr><tr><td>Monthly</td><td>{titan_mo}</td><td>{wix_mo}</td></tr><tr><td><strong>Savings</strong></td><td style="color:var(--s);font-weight:bold;">{save_val}</td><td>$0</td></tr></tbody></table></div></div></section>"""

def gen_about():
    return f"""<section id="about"><div class="container"><div class="about-grid"><div class="reveal"><h2>{about_h_in}</h2><div>{format_text(about_short_in)}</div><a href="about.html" class="btn btn-primary">Read More</a></div><img src="{about_img}" style="width:100%;border-radius:var(--radius);"></div></div></section>"""

def gen_faq():
    items = "".join([f"<details><summary>{l.split('?')[0]}?</summary><p>{l.split('?')[1]}</p></details>" for l in faq_data.split('\n') if "?" in l])
    return f"""<section id="faq"><div class="container" style="max-width:800px;"><h2 style="text-align:center;">FAQ</h2>{items}</div></section>"""

# --- PAGE GENERATORS ---
def gen_blog_post_html():
    return f"""
    <div id="post-content" style="padding-top:100px;">Loading...</div>
    {gen_csv_parser()}
    <script>
    async function init() {{
        const id = new URLSearchParams(window.location.search).get('id');
        const res = await fetch('{blog_sheet_url}');
        const txt = await res.text();
        const rows = parseFullCSV(txt);
        for(let r of rows) {{
            if(r[0]===id) {{
                document.getElementById('post-content').innerHTML = `
                    <div style="background:var(--p);color:white;padding:4rem 1rem;text-align:center;"><h1>${{r[1]}}</h1></div>
                    <div class="container" style="max-width:800px;padding:3rem 1rem;">
                        <img src="${{r[5]}}" style="width:100%;border-radius:12px;margin-bottom:2rem;">
                        <div style="line-height:1.8;font-size:1.1rem;">${{parseMarkdown(r[6])}}</div>
                    </div>
                `;
            }}
        }}
    }}
    init();
    </script>
    """

def gen_blog_index():
    return f"""
    {gen_inner_header(blog_hero_title)}
    <section><div class="container"><div id="blog-grid" class="grid-3">Loading...</div></div></section>
    {gen_csv_parser()}
    <script>
    async function init() {{
        const res = await fetch('{blog_sheet_url}');
        const txt = await res.text();
        const rows = parseFullCSV(txt);
        const b = document.getElementById('blog-grid'); b.innerHTML='';
        for(let i=1;i<rows.length;i++) {{
            let r = rows[i]; if(r.length>4) b.innerHTML+=`<div class="card"><img src="${{r[5]}}" style="width:100%;height:200px;object-fit:cover;"><h3><a href="post.html?id=${{r[0]}}" style="color:var(--txt)">${{r[1]}}</a></h3><p>${{r[4]}}</p></div>`;
        }}
    }}
    init();
    </script>
    """

def gen_product_page(is_demo=False):
    return f"""
    <section style="padding:150px 0;"><div class="container" id="prod">Loading...</div></section>
    {gen_csv_parser()}
    <script>
    async function init() {{
        const id = new URLSearchParams(window.location.search).get('item');
        const res = await fetch('{sheet_url}');
        const txt = await res.text();
        const rows = parseFullCSV(txt);
        for(let r of rows) {{
            if(r[0]===id || ('{is_demo}'==='True')) {{
                document.getElementById('prod').innerHTML = `
                    <div class="about-grid">
                        <img src="${{r[3].split('|')[0]}}" style="width:100%;border-radius:12px;">
                        <div><h1>${{r[0]}}</h1><h2 style="color:var(--s)">${{r[1]}}</h2><p>${{r[2]}}</p><button onclick="addToCart('${{r[0]}}','${{r[1]}}')" class="btn btn-primary">Add to Cart</button></div>
                    </div>
                `;
                break;
            }}
        }}
    }}
    init();
    </script>
    """

def gen_inner_header(t): return f"""<section class="hero" style="min-height:40vh;background:var(--p);"><div class="container"><h1>{t}</h1></div></section>"""

# --- 6. PAGE ASSEMBLY ---
home = ""
if show_hero: home += gen_hero()
if show_stats: home += gen_stats()
if show_features: home += gen_features()
if show_pricing: home += gen_pricing()
if show_inventory: home += gen_inventory()
if show_gallery: home += gen_about()
if show_faq: home += gen_faq()
if show_cta: home += f'<section style="background:var(--s);text-align:center;color:white;padding:4rem;"><div class="container"><h2>Ready?</h2><a href="contact.html" class="btn" style="background:white;color:var(--s)">Contact</a></div></section>'

# --- 7. DEPLOY ---
c1, c2 = st.columns([3,1])
with c1: st.components.v1.html(build_page("Home", home), height=600, scrolling=True)
with c2:
    if st.button("🚀 DOWNLOAD ZIP", type="primary"):
        z = io.BytesIO()
        with zipfile.ZipFile(z, "a", zipfile.ZIP_DEFLATED, False) as zf:
            zf.writestr("index.html", build_page("Home", home))
            zf.writestr("about.html", build_page("About", f"{gen_inner_header('About')}<div class='container'>{format_text(about_long)}</div>"))
            zf.writestr("contact.html", build_page("Contact", f"""{gen_inner_header("Contact")}<section><div class="container"><div class="contact-grid"><div><p>{biz_addr}</p><p>{biz_phone}</p><p>{biz_email}</p></div><div><form action="https://formsubmit.co/{biz_email}" method="POST"><input type="text" name="n" placeholder="Name" style="width:100%;margin-bottom:10px;padding:10px;"><input type="email" name="e" placeholder="Email" style="width:100%;margin-bottom:10px;padding:10px;"><button class="btn btn-primary">Send</button></form></div></div></div></section>"""))
            zf.writestr("privacy.html", build_page("Privacy", f"{gen_inner_header('Privacy')}<div class='container'>{format_text(priv_txt)}</div>"))
            zf.writestr("terms.html", build_page("Terms", f"{gen_inner_header('Terms')}<div class='container'>{format_text(term_txt)}</div>"))
            zf.writestr("booking.html", build_page("Book", f"{gen_inner_header(booking_title)}<div class='container' style='text-align:center;'>{booking_embed}</div>"))
            zf.writestr("blog.html", build_page("Blog", gen_blog_index()))
            zf.writestr("post.html", build_page("Post", gen_blog_post_html()))
            zf.writestr("product.html", build_page("Product", gen_product_page(False)))
            zf.writestr("manifest.json", gen_pwa_manifest())
            zf.writestr("service-worker.js", gen_sw())
        st.download_button("📥 Save Zip", z.getvalue(), "stopwebrent.zip", "application/zip")
