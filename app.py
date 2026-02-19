import streamlit as st
import streamlit.components.v1 as components # <--- CRITICAL FIX
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
init_state('feat_data', "bolt | The Performance Pillar | **0.1s High-Velocity Loading**. While traditional sites take 3–5s, Titan loads instantly.\nwallet | The Economic Pillar | **$0 Monthly Fees**. We eliminated hosting subscriptions. You pay once and own the raw source code forever.\ntable | The Functional Pillar | **Google Sheets CMS**. Update prices and photos directly from a simple spreadsheet.\nshield | The Authority Pillar | **Unhackable Security**. By removing the database, we removed the hacker's primary entry point.\nlayers | The Reliability Pillar | **Global Edge Deployment**. Distributed across 100+ servers worldwide.\nstar | The Conversion Pillar | **One-Tap WhatsApp**. Customers tap one button to start a conversation.")

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Titan v40.4 | Stable", 
    layout="wide", 
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# --- 2. SIDEBAR ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v40.4 | Verified Build")
    st.divider()
    
    # AI GENERATOR
    with st.expander("🤖 Titan AI Generator", expanded=False):
        groq_key = st.text_input("Groq API Key", type="password")
        biz_desc = st.text_input("Business Description")
        if st.button("✨ Generate Copy"):
            if not groq_key or not biz_desc:
                st.error("Missing Data")
            else:
                try:
                    url = "https://api.groq.com/openai/v1/chat/completions"
                    headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
                    prompt = f"Return JSON for '{biz_desc}': hero_h, hero_sub, about_h, about_short, feat_data (icon|Title|Desc)."
                    data = {"messages": [{"role": "user", "content": prompt}], "model": "llama3-8b-8192", "response_format": {"type": "json_object"}}
                    resp = requests.post(url, headers=headers, json=data).json()['choices'][0]['message']['content']
                    for k,v in json.loads(resp).items(): st.session_state[k] = str(v)
                    st.success("Generated! Refresh page.")
                except: st.error("AI Error")

    # DESIGN
    with st.expander("🎨 Visual DNA", expanded=True):
        theme_mode = st.selectbox("Base Theme", ["Clean Corporate", "Midnight SaaS", "Glassmorphism", "Cyberpunk Neon", "Luxury Gold", "Stark Minimalist"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#0F172A") 
        s_color = c2.color_picker("Action (CTA)", "#EF4444")  
        h_font = st.selectbox("Headings", ["Montserrat", "Space Grotesk", "Oswald"])
        b_font = st.selectbox("Body Text", ["Inter", "Open Sans", "Roboto"])
        border_rad = st.select_slider("Corner Roundness", ["0px", "8px", "24px", "50px"], value="8px")
        anim_type = st.selectbox("Animation", ["Fade Up", "Zoom In", "None"])

    # MODULES
    with st.expander("🧩 Modules", expanded=False):
        show_hero = st.checkbox("Hero", True)
        show_stats = st.checkbox("Stats", True)
        show_features = st.checkbox("Features", True)
        show_pricing = st.checkbox("Pricing", True)
        show_inventory = st.checkbox("Store", True)
        show_blog = st.checkbox("Blog", True)
        show_gallery = st.checkbox("About", True)
        show_testimonials = st.checkbox("Testimonials", True)
        show_faq = st.checkbox("FAQ", True)
        show_cta = st.checkbox("CTA", True)
        show_booking = st.checkbox("Booking", True)

    # SEO
    with st.expander("⚙️ SEO & Analytics", expanded=False):
        seo_area = st.text_input("Service Area", "Global")
        seo_kw = st.text_input("SEO Keywords", "web design")
        gsc_tag = st.text_input("Google Verification")
        og_image = st.text_input("Social Share Image")

# --- 3. INPUT TABS ---
st.title("🏗️ StopWebRent Site Builder")
tabs = st.tabs(["1. Identity", "2. Content", "3. Pricing", "4. Store", "5. Booking", "6. Blog", "7. Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "StopWebRent.com")
        biz_phone = st.text_input("Phone", "966572562151")
        biz_email = st.text_input("Email", "hello@stopwebrent.com")
    with c2:
        prod_url = st.text_input("URL", "https://www.stopwebrent.com")
        biz_addr = st.text_area("Address", "Kaydiem Script Lab, Kolkata")
        map_iframe = st.text_area("Map Embed", height=100)
        seo_d = st.text_area("Meta Desc", "Stop paying monthly fees.")
        logo_url = st.text_input("Logo URL")

    st.subheader("📱 PWA & Social")
    pwa_icon = st.text_input("App Icon", logo_url)
    lang_sheet = st.text_input("Translation CSV")
    sc1, sc2, sc3 = st.columns(3)
    fb_link = sc1.text_input("Facebook")
    x_link = sc2.text_input("Twitter")
    wa_num = sc3.text_input("WhatsApp (No +)", "966572562151")

with tabs[1]:
    hero_h = st.text_input("Headline", st.session_state.hero_h)
    hero_sub = st.text_input("Subtext", st.session_state.hero_sub)
    hc1, hc2, hc3 = st.columns(3)
    hero_img_1 = hc1.text_input("Slide 1", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600")
    hero_img_2 = hc2.text_input("Slide 2", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1600")
    hero_img_3 = hc3.text_input("Slide 3", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1600")
    
    st.divider()
    c1, c2, c3 = st.columns(3)
    stat_1 = c1.text_input("Stat 1", "0.1s")
    label_1 = c1.text_input("Label 1", "Speed")
    stat_2 = c2.text_input("Stat 2", "$0")
    label_2 = c2.text_input("Label 2", "Fees")
    stat_3 = c3.text_input("Stat 3", "100%")
    label_3 = c3.text_input("Label 3", "Ownership")
    
    f_title = st.text_input("Features Title", "Value Pillars")
    feat_data_input = st.text_area("Features List", st.session_state.feat_data, height=150)
    
    about_h_in = st.text_input("About Title", st.session_state.about_h)
    about_img = st.text_input("About Image", "https://images.unsplash.com/photo-1543286386-713df548e9cc?q=80&w=1600")
    about_short_in = st.text_area("About Short", st.session_state.about_short, height=100)
    about_long = st.text_area("About Long", "**The Trap**\nMost business owners...", height=150)

with tabs[2]:
    c1, c2, c3 = st.columns(3)
    titan_price = c1.text_input("Titan Price", "$199")
    titan_mo = c1.text_input("Titan Monthly", "$0")
    wix_name = c2.text_input("Comp Name", "Wix")
    wix_mo = c2.text_input("Comp Monthly", "$29/mo")
    save_val = c3.text_input("Savings", "$1,466")

with tabs[3]:
    sheet_url = st.text_input("Store CSV", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Product Fallback Img", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800")
    c1, c2 = st.columns(2)
    paypal_link = c1.text_input("PayPal Link")
    upi_id = c2.text_input("UPI ID")

with tabs[4]:
    booking_embed = st.text_area("Calendly Embed", height=100)
    booking_title = st.text_input("Book Title", "Book Now")
    booking_desc = st.text_input("Book Subtext", "Select a slot.")

with tabs[5]:
    blog_sheet_url = st.text_input("Blog CSV")
    blog_hero_title = st.text_input("Blog Title", "Insights")
    blog_hero_sub = st.text_input("Blog Subtext", "News.")

with tabs[6]:
    testi_data = st.text_area("Testimonials", "Name | Quote", height=100)
    faq_data = st.text_area("FAQ", "Q? ? A", height=100)
    priv_txt = st.text_area("Privacy", "Text...", height=100)
    term_txt = st.text_area("Terms", "Text...", height=100)

# --- 4. COMPILER ENGINE ---

def format_text(text):
    if not text: return ""
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    lines = text.split('\n')
    html = ""
    in_list = False
    for line in lines:
        if line.strip().startswith("* "):
            if not in_list: html += '<ul style="margin-bottom:1rem; padding-left:1.5rem;">'; in_list = True
            html += f'<li style="margin-bottom:0.5rem; opacity:0.9;">{line.strip()[2:]}</li>'
        else:
            if in_list: html += "</ul>"; in_list = False
            if line.strip(): html += f"<p style='margin-bottom:1rem; opacity:0.9;'>{line}</p>"
    if in_list: html += "</ul>"
    return html

def gen_schema():
    s = {"@context":"https://schema.org","@type":"LocalBusiness","name":biz_name,"url":prod_url}
    return f'<script type="application/ld+json">{json.dumps(s)}</script>'

def gen_pwa_manifest():
    return json.dumps({"name":biz_name,"start_url":"./index.html","display":"standalone","theme_color":p_color,"icons":[{"src":pwa_icon,"sizes":"512x512","type":"image/png"}]})

def gen_sw():
    return """self.addEventListener('install', (e) => { e.waitUntil(caches.open('titan-v1').then((c) => c.addAll(['./index.html']))); }); self.addEventListener('fetch', (e) => { e.respondWith(caches.match(e.request).then((r) => r || fetch(e.request))); });"""

def gen_csv_parser():
    return """
    <script>
    function parseCSVLine(str) {
        const res = []; let cur = ''; let inQuote = false;
        for (let i = 0; i < str.length; i++) {
            const c = str[i];
            if (c === '"') { if (inQuote && str[i+1] === '"') { cur += '"'; i++; } else { inQuote = !inQuote; } }
            else if (c === ',' && !inQuote) { res.push(cur.trim()); cur = ''; } else { cur += c; }
        }
        res.push(cur.trim()); return res;
    }
    function parseFullCSV(txt) {
        const rows = []; let row = []; let cur = ''; let inQuote = false;
        for (let i = 0; i < txt.length; i++) {
            const c = txt[i]; const next = txt[i+1];
            if (c === '"') { if (inQuote && next === '"') { cur += '"'; i++; } else { inQuote = !inQuote; } }
            else if (c === ',' && !inQuote) { row.push(cur.trim()); cur = ''; }
            else if ((c === '\\n' || (c === '\\r' && next === '\\n')) && !inQuote) {
                row.push(cur.trim()); rows.push(row); row = []; cur = ''; if (c === '\\r') i++;
            } else { cur += c; }
        }
        if (cur || row.length) { row.push(cur.trim()); rows.push(row); }
        return rows;
    }
    function parseMarkdown(text) {
        if (!text) return '';
        let html = text.replace(/\\r\\n/g, '\\n').replace(/\\n/g, '<br><br>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
        return html;
    }
    </script>
    """

def get_theme_css():
    # --- VARIABLE NAME FIX ---
    bg_c, txt_c, card_c, nav_c = "#ffffff", "#0f172a", "rgba(255,255,255,0.8)", "rgba(255,255,255,0.9)"
    if "Midnight" in theme_mode: bg_c, txt_c, card_c, nav_c = "#0f172a", "#f8fafc", "rgba(30,41,59,0.9)", "rgba(15,23,42,0.9)"
    if "Cyberpunk" in theme_mode: bg_c, txt_c, card_c, nav_c = "#050505", "#00ff9d", "rgba(10,10,10,0.9)", "rgba(0,0,0,0.9)"
    if "Luxury" in theme_mode: bg_c, txt_c, card_c, nav_c = "#101010", "#D4AF37", "rgba(20,20,20,0.9)", "rgba(0,0,0,0.9)"
    if "Stark" in theme_mode: bg_c, txt_c, card_c, nav_c = "#ffffff", "#000000", "#ffffff", "rgba(255,255,255,1)"
    
    anim_css = ".reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s ease; } .reveal.active { opacity: 1; transform: translateY(0); }"
    if anim_type == "None": anim_css = ""

    return f"""
    :root {{ --p: {p_color}; --s: {s_color}; --bg: {bg_c}; --txt: {txt_c}; --card: {card_c}; --nav: {nav_c}; --radius: {border_rad}; }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{ background-color: var(--bg); color: var(--txt); font-family: var(--b-font); margin: 0; line-height: 1.6; overflow-x: hidden; }}
    h1, h2, h3 {{ font-family: var(--h-font); color: var(--txt); font-weight: 800; line-height: 1.2; margin-bottom: 0.5rem; }}
    
    .container {{ max-width: 1280px; margin: 0 auto; padding: 0 24px; }}
    .btn {{ display: inline-flex; align-items: center; justify-content: center; padding: 0.8rem 2rem; border-radius: var(--radius); font-weight: 700; text-transform: uppercase; cursor: pointer; border: none; text-decoration: none; color: white; transition: 0.3s; min-height: 3rem; }}
    .btn-primary {{ background: var(--p); }} .btn-accent {{ background: var(--s); }}
    
    nav {{ position: fixed; top: 0; width: 100%; z-index: 1000; padding: 1rem 0; background: var(--nav); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(128,128,128,0.1); }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links a {{ margin-left: 2rem; text-decoration: none; font-weight: 600; color: var(--txt); opacity: 0.8; transition:0.2s; }}
    .mobile-menu {{ display: none; font-size: 1.5rem; cursor: pointer; }}
    
    .hero {{ min-height: 90vh; display: flex; align-items: center; justify-content: center; position: relative; background: var(--p); padding-top: 80px; }}
    .hero-content {{ z-index: 2; width: 100%; text-align: center; }}
    .hero h1 {{ color: white !important; font-size: clamp(2.5rem, 5vw, 4.5rem); text-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
    .hero p {{ color: rgba(255,255,255,0.95); max-width: 700px; margin: 0 auto 2rem; font-size: 1.2rem; }}
    .carousel-slide {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; opacity: 0; transition: 1.5s; }}
    .carousel-slide.active {{ opacity: 1; }}
    .hero-overlay {{ background: rgba(0,0,0,0.5); position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; }}

    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }}
    .about-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center; }}
    .contact-grid {{ display: grid; grid-template-columns: 1fr 2fr; gap: 3rem; }}
    
    .card {{ background: var(--card); padding: 2rem; border-radius: var(--radius); border: 1px solid rgba(128,128,128,0.1); transition: 0.3s; height: 100%; }}
    .card:hover {{ transform: translateY(-5px); box-shadow: 0 10px 30px rgba(0,0,0,0.1); border-color: var(--s); }}
    .prod-img {{ width: 100%; height: 250px; object-fit: cover; border-radius: calc(var(--radius) - 4px); margin-bottom: 1rem; background: #f1f5f9; }}
    
    .pricing-wrapper {{ overflow-x: auto; margin: 2rem 0; }}
    .pricing-table {{ width: 100%; border-collapse: collapse; min-width: 600px; }}
    .pricing-table th {{ background: var(--p); color: white; padding: 1.5rem; }}
    .pricing-table td {{ padding: 1.5rem; border-bottom: 1px solid rgba(128,128,128,0.1); }}
    
    .blog-badge {{ background: var(--s); color: white; padding: 0.3rem 0.8rem; border-radius: 50px; font-size: 0.75rem; font-weight: bold; margin-bottom: 1rem; display:inline-block; }}
    
    #cart-float {{ position: fixed; bottom: 100px; right: 30px; background: var(--p); color: white; padding: 15px 20px; border-radius: 50px; z-index: 998; display: flex; gap: 10px; cursor: pointer; }}
    #cart-modal {{ display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: var(--card); width: 90%; max-width: 450px; padding: 2rem; border-radius: 16px; z-index: 1001; box-shadow: 0 50px 100px rgba(0,0,0,0.5); border: 1px solid rgba(128,128,128,0.2); backdrop-filter: blur(20px); }}
    #cart-overlay {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; }}
    
    footer {{ background: var(--p); padding: 4rem 0; color: white; margin-top: auto; }}
    .footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; }}
    footer a {{ color: rgba(255,255,255,0.7); text-decoration: none; display: block; margin-bottom: 0.5rem; }}
    
    section {{ padding: clamp(3rem, 5vw, 5rem) 0; }}
    
    {anim_css}
    
    @media (max-width: 768px) {{
        .hero {{ min-height: 70vh; }}
        .nav-links {{ position: fixed; top: 70px; left: -100%; width: 100%; height: 100vh; background: var(--bg); flex-direction: column; padding: 2rem; align-items: flex-start; transition: 0.3s; border-top: 1px solid rgba(0,0,0,0.1); }}
        .nav-links.active {{ left: 0; }}
        .mobile-menu {{ display: block; }}
        .about-grid, .contact-grid {{ grid-template-columns: 1fr; gap: 2rem; }}
        .detail-view {{ grid-template-columns: 1fr; }}
    }}
    """

def gen_common_js():
    clean_wa = wa_num.replace("+", "").replace(" ", "")
    return f"""
    <script>
    window.addEventListener('scroll', () => {{
        document.querySelectorAll('.reveal').forEach(r => {{
            if(r.getBoundingClientRect().top < window.innerHeight - 80) r.classList.add('active');
        }});
    }});
    function toggleMenu() {{ document.querySelector('.nav-links').classList.toggle('active'); }}
    
    async function toggleLang() {{
        try {{
            const res = await fetch('{lang_sheet}');
            const txt = await res.text();
            const rows = txt.split(/\\r\\n|\\n/);
            rows.forEach(row => {{
                const cols = row.match(/(".*?"|[^",\s]+)(?=\s*,|\s*$)/g);
                if(cols && cols.length >= 2) {{
                    const id = cols[0].replace(/"/g, '').trim();
                    const text = cols[1].replace(/"/g, '').trim();
                    const el = document.getElementById(id);
                    if(el) el.innerText = text;
                }}
            }});
        }} catch(e) {{}}
    }}
    
    let cart = JSON.parse(localStorage.getItem('titanCart')) || [];
    function addToCart(name, price) {{
        cart.push({{name, price}});
        localStorage.setItem('titanCart', JSON.stringify(cart));
        updateCartDisplay();
        alert(name + " added!");
    }}
    function updateCartDisplay() {{
        const el = document.getElementById('cart-count');
        if(el) el.innerText = cart.length;
        if(cart.length > 0) document.getElementById('cart-float').style.display = 'flex';
    }}
    function toggleCart() {{ 
        const m = document.getElementById('cart-modal');
        const o = document.getElementById('cart-overlay');
        const d = m.style.display === 'block' ? 'none' : 'block';
        m.style.display = d; o.style.display = d;
        if(d === 'block') renderCartItems();
    }}
    function renderCartItems() {{
        const b = document.getElementById('cart-items');
        b.innerHTML = '';
        let total = 0;
        cart.forEach((item, i) => {{
            const price = parseFloat(item.price.replace(/[^0-9.]/g, '')) || 0;
            total += price;
            b.innerHTML += `<div style="display:flex; justify-content:space-between; padding:0.5rem 0; border-bottom:1px solid #eee;"><span>${{item.name}}</span><span>${{item.price}} <span onclick="remItem(${{i}})" style="color:red; cursor:pointer; margin-left:10px;">x</span></span></div>`;
        }});
        document.getElementById('cart-total').innerText = total.toFixed(2);
    }}
    function remItem(i) {{ cart.splice(i,1); localStorage.setItem('titanCart', JSON.stringify(cart)); renderCartItems(); updateCartDisplay(); }}
    function checkoutWhatsApp() {{
        let msg = "New Order:%0A";
        let total = 0;
        cart.forEach(i => {{ msg += `- ${{i.name}} (${{i.price}})%0A`; total += parseFloat(i.price.replace(/[^0-9.]/g,'')) || 0; }});
        msg += `%0ATotal: ${{total.toFixed(2)}}%0A%0APayment: UPI {upi_id} | PayPal {paypal_link}`;
        window.open(`https://wa.me/{clean_wa}?text=${{msg}}`, '_blank');
    }}
    window.addEventListener('load', updateCartDisplay);
    </script>
    """

def get_simple_icon(name):
    name = name.lower().strip()
    path = "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"
    if "bolt" in name: path = "M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"
    if "wallet" in name: path = "M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"
    return f'<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="{path}"/></svg>'

# --- SECTION GENERATORS ---
def gen_hero():
    return f"""
    <section class="hero">
        <div class="hero-overlay"></div>
        <div class="carousel-slide active" style="background-image: url('{hero_img_1}')"></div>
        <div class="carousel-slide" style="background-image: url('{hero_img_2}')"></div>
        <div class="carousel-slide" style="background-image: url('{hero_img_3}')"></div>
        <div class="container hero-content">
            <h1>{hero_h}</h1>
            <p>{hero_sub}</p>
            <div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
                <a href="#pricing" class="btn btn-accent">Calculate Savings</a>
                <a href="contact.html" class="btn" style="background:rgba(255,255,255,0.2); backdrop-filter:blur(10px);">Get Free Audit</a>
            </div>
        </div>
    </section>
    <script>
        let slides = document.querySelectorAll('.carousel-slide');
        let currentSlide = 0;
        setInterval(() => {{
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }}, 4000);
    </script>
    """

def gen_features():
    cards = ""
    for line in feat_data_input.split('\n'):
        if "|" in line:
            parts = line.split('|')
            cards += f"""<div class="card reveal"><div style="color:var(--s); margin-bottom:1rem;">{get_simple_icon(parts[0])}</div><h3>{parts[1].strip()}</h3><div>{format_text(parts[2].strip())}</div></div>"""
    return f"""<section id="features"><div class="container"><div class="section-head reveal"><h2>{f_title}</h2></div><div class="grid-3">{cards}</div></div></section>"""

def gen_stats():
    return f"""
    <div style="background:var(--p); color:white; padding:3rem 0; text-align:center;">
        <div class="container grid-3">
            <div class="reveal"><h3 style="color:#ffffff; margin:0; font-size:3rem;">{stat_1}</h3><p style="color:rgba(255,255,255,0.7);">{label_1}</p></div>
            <div class="reveal"><h3 style="color:#ffffff; margin:0; font-size:3rem;">{stat_2}</h3><p style="color:rgba(255,255,255,0.7);">{label_2}</p></div>
            <div class="reveal"><h3 style="color:#ffffff; margin:0; font-size:3rem;">{stat_3}</h3><p style="color:rgba(255,255,255,0.7);">{label_3}</p></div>
        </div>
    </div>
    """

def gen_pricing():
    if not show_pricing: return ""
    return f"""
    <section id="pricing"><div class="container">
        <div class="section-head reveal"><h2>Cost Comparison</h2></div>
        <div class="pricing-wrapper reveal">
            <table class="pricing-table">
                <thead><tr><th>Expense</th><th style="background:var(--s);">Titan Engine</th><th>{wix_name}</th></tr></thead>
                <tbody>
                    <tr><td>Setup</td><td><strong>{titan_price}</strong></td><td>$0</td></tr>
                    <tr><td>Monthly</td><td><strong>{titan_mo}</strong></td><td>{wix_mo}</td></tr>
                    <tr><td><strong>Savings</strong></td><td style="color:var(--s); font-size:1.3rem;">You Save {save_val}</td><td>$0</td></tr>
                </tbody>
            </table>
        </div>
    </div></section>
    """

def gen_inventory_js(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""
    {gen_csv_parser()}
    <script>
    {demo_flag}
    async function loadInv() {{
        try {{
            const res = await fetch('{sheet_url}');
            const txt = await res.text();
            const lines = txt.split(/\\r\\n|\\n/);
            const box = document.getElementById('inv-grid');
            if(!box) return;
            box.innerHTML = '';
            for(let i=1; i<lines.length; i++) {{
                if(!lines[i].trim()) continue;
                const c = parseCSVLine(lines[i]);
                let img = c[3] && c[3].length > 5 ? c[3] : '{custom_feat}';
                let stripe = (c.length > 4 && c[4].includes('http')) ? c[4] : '';
                
                if(c.length > 1) {{
                    let btn = stripe 
                        ? `<a href="${{stripe}}" class="btn btn-primary" style="width:100%;">Buy Now</a>`
                        : `<button onclick="addToCart('${{c[0]}}', '${{c[1]}}')" class="btn btn-primary" style="width:100%;">Add to Cart</button>`;
                        
                    box.innerHTML += `
                    <div class="card reveal">
                        <img src="${{img}}" class="prod-img" loading="lazy">
                        <div>
                            <h3>${{c[0]}}</h3>
                            <p style="font-weight:bold; color:var(--s); margin-bottom:0.5rem;">${{c[1]}}</p>
                            <p style="font-size:0.9rem; opacity:0.8; margin-bottom:1rem;">${{c[2]}}</p>
                            ${{btn}}
                        </div>
                    </div>`;
                }}
            }}
        }} catch(e) {{ console.log(e); }}
    }}
    if(document.getElementById('inv-grid')) window.addEventListener('load', loadInv);
    </script>
    """

def gen_inventory():
    if not show_inventory: return ""
    return f"""
    <section id="inventory" style="background:rgba(0,0,0,0.02)"><div class="container">
        <div class="section-head reveal"><h2>Store</h2></div>
        <div id="inv-grid" class="grid-3"><div style="text-align:center; padding:4rem;">Loading...</div></div>
    </div></section>
    {gen_inventory_js(is_demo=False)}
    """

def gen_about_section():
    formatted_about = format_text(about_short_in)
    return f"""
    <section id="about"><div class="container">
        <div class="about-grid">
            <div class="reveal">
                <h2>{about_h_in}</h2>
                <div style="font-size:1.1rem; opacity:0.9; margin-bottom:2rem;">{formatted_about}</div>
                <a href="about.html" class="btn btn-primary">Read More</a>
            </div>
            <img src="{about_img}" class="reveal" loading="lazy" style="width:100%; border-radius:var(--radius); box-shadow:0 20px 50px rgba(0,0,0,0.2);">
        </div>
    </div></section>
    """

def gen_faq_section():
    items = ""
    for line in faq_data.split('\n'):
        if "?" in line:
            parts = line.split('?', 1)
            items += f"<details class='reveal'><summary>{parts[0]}?</summary><p>{parts[1]}</p></details>"
    return f"""<section id="faq"><div class="container" style="max-width:800px;"><div class="section-head reveal"><h2>FAQ</h2></div>{items}</div></section>"""

def gen_footer():
    return f"""<footer><div class="container"><div class="footer-grid"><div><h3>{biz_name}</h3><p>{biz_addr}</p></div><div><h4>Links</h4><a href="index.html">Home</a><a href="blog.html">Blog</a></div></div><div style="margin-top:3rem; text-align:center; opacity:0.6; font-size:0.8rem;">&copy; {biz_name}</div></div></footer>"""

def gen_booking_content():
    return f"""<section class="hero" style="min-height:40vh;background:var(--p);"><div class="container"><h1>{booking_title}</h1><p>{booking_desc}</p></div></section><section><div class="container" style="text-align:center;"><div style="background:white;border-radius:12px;box-shadow:0 10px 40px rgba(0,0,0,0.1);">{booking_embed}</div></div></section>"""

def gen_blog_index_html():
    return f"""
    <section class="hero" style="min-height:40vh; background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('{hero_img_1}'); background-size: cover;">
        <div class="container"><h1 id="blog-title">{blog_hero_title}</h1><p id="blog-sub">{blog_hero_sub}</p></div>
    </section>
    <section><div class="container"><div id="blog-grid" class="grid-3">Loading...</div></div></section>
    {gen_csv_parser()}
    <script>
    async function loadBlog() {{
        try {{
            const res = await fetch('{blog_sheet_url}');
            const txt = await res.text();
            const rows = parseFullCSV(txt);
            const box = document.getElementById('blog-grid'); box.innerHTML = '';
            for(let i=1; i<rows.length; i++) {{
                const r = rows[i];
                if(r.length > 4) box.innerHTML += `<div class="card reveal"><img src="${{r[5]}}" class="prod-img"><div><span class="blog-badge">${{r[3]}}</span><h3><a href="post.html?id=${{r[0]}}" style="color:var(--txt);text-decoration:none">${{r[1]}}</a></h3></div></div>`;
            }}
        }} catch(e) {{}}
    }}
    loadBlog();
    </script>
    """

def gen_blog_post_html():
    return f"""
    <div id="post-container" style="padding-top:100px;">Loading...</div>
    {gen_csv_parser()}
    <script>
    async function loadPost() {{
        const params = new URLSearchParams(window.location.search);
        const slug = params.get('id');
        try {{
            const res = await fetch('{blog_sheet_url}');
            const txt = await res.text();
            const rows = parseFullCSV(txt);
            for(let i=1; i<rows.length; i++) {{
                const r = rows[i];
                if(r[0] === slug) {{
                    const content = parseMarkdown(r[6]);
                    document.getElementById('post-container').innerHTML = `
                        <div style="background:var(--p);padding:4rem 1rem;color:white;text-align:center;">
                            <div class="container"><h1>${{r[1]}}</h1><span class="blog-badge">${{r[3]}}</span></div>
                        </div>
                        <div class="container" style="max-width:800px;padding:3rem 1rem;">
                            <img src="${{r[5]}}" style="width:100%;border-radius:12px;margin-bottom:2rem;">
                            <div style="line-height:1.8;font-size:1.1rem;">${{content}}</div>
                        </div>
                    `;
                    break;
                }}
            }}
        }} catch(e) {{}}
    }}
    loadPost();
    </script>
    """

def gen_product_page_content(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""
    <section style="padding:150px 0;"><div class="container" id="prod-box">Loading...</div></section>
    <script>
    {demo_flag}
    {gen_csv_parser().replace('<script>','').replace('</script>','')}
    async function init() {{
        const id = new URLSearchParams(window.location.search).get('item');
        let target = id; if(isDemo) target = "Demo Item";
        try {{
            const res = await fetch('{sheet_url}');
            const rows = parseFullCSV(await res.text()).slice(1);
            for(let col of rows) {{
                if(isDemo) target = col[0];
                if(col[0] === target) {{
                    document.getElementById('prod-box').innerHTML = `
                        <div class="detail-view">
                            <img src="${{col[3]}}" style="width:100%; border-radius:20px;">
                            <div><h1>${{col[0]}}</h1><p style="font-size:1.5rem; color:var(--s); font-weight:bold;">${{col[1]}}</p><p>${{col[2]}}</p><button class="btn btn-primary" onclick="addToCart('${{col[0]}}','${{col[1]}}')">Add to Cart</button></div>
                        </div>
                    `;
                    break;
                }}
            }}
        }} catch(e) {{}}
    }}
    init();
    </script>
    """

def gen_inner_header(title):
    return f"""<section class="hero" style="min-height: 40vh; background:var(--p);"><div class="container"><h1>{title}</h1></div></section>"""

def build_page(title, content, extra_js=""):
    css = get_theme_css()
    meta = f'<link rel="manifest" href="manifest.json"><meta name="theme-color" content="{p_color}">'
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title} | {biz_name}</title>{meta}{gen_schema()}<link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ','+')}:wght@400;700;900&family={b_font.replace(' ','+')}:wght@300;400;600&display=swap" rel="stylesheet"><style>{css}</style></head><body>{gen_nav()}{content}{gen_footer()}{gen_wa_widget()}{gen_cart_system()}{gen_common_js()}{gen_sw()}{extra_js}</body></html>"""

# --- 6. ASSEMBLE HOME ---
home_content = ""
if show_hero: home_content += gen_hero()
if show_stats: home_content += gen_stats()
if show_features: home_content += gen_features()
if show_pricing: home_content += gen_pricing()
if show_inventory: home_content += gen_inventory()
if show_gallery: home_content += gen_about_section()
if show_testimonials: 
    t_cards = "".join([f'<div class="card reveal" style="text-align:center;"><i>"{x.split("|")[1]}"</i><br><b>- {x.split("|")[0]}</b></div>' for x in testi_data.split('\n') if "|" in x])
    home_content += f'<section style="background:#f8fafc"><div class="container"><div class="section-head reveal"><h2>Client Stories</h2></div><div class="grid-3">{t_cards}</div></div></section>'
if show_faq: home_content += gen_faq_section()
if show_cta: home_content += f'<section style="background:var(--s); color:white; text-align:center;"><div class="container reveal"><h2>Start Owning Your Future</h2><p style="margin-bottom:2rem;">Stop paying rent.</p><a href="contact.html" class="btn" style="background:white; color:var(--s);">Get Started</a></div></section>'

# --- 7. DEPLOY ---
c1, c2 = st.columns([3, 1])
with c1:
    prev = st.radio("Preview", ["Home", "Product", "Blog Index", "Blog Post", "Booking", "Privacy", "Terms", "Contact"], horizontal=True)
    if prev == "Home": components.html(build_page("Home", home_content), height=600, scrolling=True)
    elif prev == "Product": components.html(build_page("Prod", gen_product_page_content(True)), height=600, scrolling=True)
    elif prev == "Blog Index": components.html(build_page("Blog", gen_blog_index_html()), height=600, scrolling=True)
    elif prev == "Blog Post": components.html(build_page("Post", gen_blog_post_html()), height=600, scrolling=True)
    elif prev == "Booking": components.html(build_page("Book", gen_booking_content()), height=600, scrolling=True)
    elif prev == "Privacy": components.html(build_page("Privacy", f"{gen_inner_header('Privacy')}<div class='container'>{format_text(priv_txt)}</div>"), height=600, scrolling=True)
    elif prev == "Terms": components.html(build_page("Terms", f"{gen_inner_header('Terms')}<div class='container'>{format_text(term_txt)}</div>"), height=600, scrolling=True)
    elif prev == "Contact": 
        contact_html = f"""{gen_inner_header("Contact Us")}<section><div class="container"><div class="contact-grid"><div><div class="card"><h3>Get In Touch</h3><p>{biz_addr}</p><p><a href="tel:{biz_phone}">{biz_phone}</a></p><p>{biz_email}</p></div></div><div class="card"><h3>Send Message</h3><form action="https://formsubmit.co/{biz_email}" method="POST"><label>Name</label><input type="text" name="name" required><label>Email</label><input type="email" name="email" required><label>Message</label><textarea name="msg" rows="4" required></textarea><button class="btn btn-primary" type="submit">Send</button></form></div></div><br><div style="border-radius:12px;overflow:hidden;">{map_iframe}</div></div></section>"""
        components.html(build_page("Contact", contact_html), height=600, scrolling=True)

with c2:
    if st.button("DOWNLOAD WEBSITE ZIP", type="primary"):
        z_b = io.BytesIO()
        with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as zf:
            zf.writestr("index.html", build_page("Home", home_content))
            zf.writestr("about.html", build_page("About", f"{gen_inner_header('About')}<div class='container'>{format_text(about_long)}</div>"))
            
            contact_html = f"""{gen_inner_header("Contact Us")}<section><div class="container"><div class="contact-grid"><div><div class="card"><h3>Get In Touch</h3><p>{biz_addr}</p><p><a href="tel:{biz_phone}">{biz_phone}</a></p><p>{biz_email}</p></div></div><div class="card"><h3>Send Message</h3><form action="https://formsubmit.co/{biz_email}" method="POST"><label>Name</label><input type="text" name="name" required><label>Email</label><input type="email" name="email" required><label>Message</label><textarea name="msg" rows="4" required></textarea><button class="btn btn-primary" type="submit">Send</button></form></div></div><br><div style="border-radius:12px;overflow:hidden;">{map_iframe}</div></div></section>"""
            zf.writestr("contact.html", build_page("Contact", contact_html))
            
            zf.writestr("privacy.html", build_page("Privacy", f"{gen_inner_header('Privacy')}<div class='container'>{format_text(priv_txt)}</div>"))
            zf.writestr("terms.html", build_page("Terms", f"{gen_inner_header('Terms')}<div class='container'>{format_text(term_txt)}</div>"))
            zf.writestr("booking.html", build_page("Book Now", gen_booking_content()))
            zf.writestr("product.html", build_page("Product", gen_product_page_content(is_demo=False)))
            if show_blog:
                zf.writestr("blog.html", build_page("Blog", gen_blog_index_html()))
                zf.writestr("post.html", build_page("Article", gen_blog_post_html()))
            zf.writestr("manifest.json", gen_pwa_manifest())
            zf.writestr("service-worker.js", gen_sw())
            zf.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {prod_url}/sitemap.xml")
            
        st.download_button("📥 Click to Save", z_b.getvalue(), "stopwebrent_site.zip", "application/zip")
