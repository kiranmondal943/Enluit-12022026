import streamlit as st
import zipfile
import io
import json
import re
import requests
import streamlit.components.v1 as components

# --- 0. STATE & CONFIGURATION ---
st.set_page_config(
    page_title="Titan v40.3 | Ultimate Architect", 
    layout="wide", 
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

def init_state(key, default_val):
    if key not in st.session_state:
        st.session_state[key] = default_val

# Default Data Injection
init_state('hero_h', "Stop Paying Rent for Your Website.")
init_state('hero_sub', "The Titan Engine is the world’s first 0.1s website architecture that runs on $0 monthly fees. Pay once. Own it forever.")
init_state('about_h', "Control Your Empire")
init_state('about_short', "No WordPress dashboard. No plugins to update. Just open your private Google Sheet, change a text, and watch your site update globally in seconds.")
init_state('feat_data', "bolt | The Performance Pillar | **0.1s High-Velocity Loading**. While traditional sites take 3–5s, Titan loads instantly.\nwallet | The Economic Pillar | **$0 Monthly Fees**. We eliminated hosting subscriptions. You pay once and own the raw source code forever.\ntable | The Functional Pillar | **Google Sheets CMS**. Update prices and photos directly from a simple spreadsheet.\nshield | The Authority Pillar | **Unhackable Security**. By removing the database, we removed the hacker's primary entry point.\nlayers | The Reliability Pillar | **Global Edge Deployment**. Distributed across 100+ servers worldwide.\nstar | The Conversion Pillar | **One-Tap WhatsApp**. Customers tap one button to start a conversation.")

# --- 1. SIDEBAR CONTROLS ---
with st.sidebar:
    st.title("⚡ Titan Architect")
    st.caption("v40.3 | Ultimate Build")
    st.divider()
    
    # AI Generator
    with st.expander("🤖 AI Content Generator", expanded=False):
        groq_key = st.text_input("Groq API Key", type="password")
        biz_desc = st.text_input("Business Description")
        if st.button("✨ Generate Site Copy"):
            if not groq_key or not biz_desc:
                st.error("Missing API Key or Description")
            else:
                try:
                    with st.spinner("Architecting your digital empire..."):
                        url = "https://api.groq.com/openai/v1/chat/completions"
                        headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
                        prompt = f"Return strictly valid JSON for '{biz_desc}': keys must be hero_h, hero_sub, about_h, about_short, feat_data (format: icon|Title|Desc per line). Do not include markdown formatting in the JSON."
                        data = {"messages": [{"role": "user", "content": prompt}], "model": "llama3-8b-8192", "response_format": {"type": "json_object"}}
                        resp = requests.post(url, headers=headers, json=data).json()['choices'][0]['message']['content']
                        parsed = json.loads(resp)
                        for k,v in parsed.items(): 
                            if k == 'feat_data' and isinstance(v, list): v = "\n".join(v)
                            st.session_state[k] = str(v)
                        st.success("Generated! Content injected.")
                        st.rerun()
                except Exception as e: st.error(f"AI Error: {str(e)}")

    # Visual DNA
    with st.expander("🎨 Visual DNA", expanded=True):
        theme_mode = st.selectbox("Base Theme", ["Clean Corporate", "Midnight SaaS", "Glassmorphism", "Cyberpunk Neon", "Luxury Gold", "Stark Minimalist"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#0F172A") 
        s_color = c2.color_picker("Action (CTA)", "#EF4444")  
        h_font = st.selectbox("Headings", ["Montserrat", "Space Grotesk", "Oswald", "Playfair Display"])
        b_font = st.selectbox("Body Text", ["Inter", "Open Sans", "Roboto", "Lato"])
        border_rad = st.select_slider("Corner Roundness", ["0px", "4px", "8px", "16px", "24px", "50px"], value="8px")
        anim_type = st.selectbox("Animation", ["Fade Up", "Zoom In", "Slide In", "None"])

    # Feature Toggles
    with st.expander("🧩 Feature Modules", expanded=False):
        show_hero = st.checkbox("Hero Section", True)
        show_stats = st.checkbox("Stats Bar", True)
        show_features = st.checkbox("Features Grid", True)
        show_pricing = st.checkbox("Pricing Table", True)
        show_inventory = st.checkbox("E-Commerce Store", True)
        show_blog = st.checkbox("Blog System", True)
        show_gallery = st.checkbox("About/Gallery", True)
        show_testimonials = st.checkbox("Testimonials", True)
        show_faq = st.checkbox("FAQ Section", True)
        show_cta = st.checkbox("Final CTA", True)
        show_cookie = st.checkbox("Cookie Banner", True)
        show_whatsapp_float = st.checkbox("Floating WhatsApp", True)

    # SEO & Analytics
    with st.expander("⚙️ SEO & Analytics", expanded=False):
        seo_area = st.text_input("Service Area", "Global")
        seo_kw = st.text_input("SEO Keywords", "web design, fast hosting, zero fees")
        gsc_tag = st.text_input("Google Search Console ID")
        og_image = st.text_input("Social Share Image URL")
        
    with st.expander("🩺 Diagnostics", expanded=False):
        if not st.session_state.hero_h: st.warning("Hero Headline Missing")
        else: st.success("Content Loaded")

# --- 2. MAIN INPUTS ---
st.title("🏗️ Titan Site Builder")
tabs = st.tabs(["1. Identity", "2. Content", "3. Pricing", "4. Store", "5. Booking", "6. Blog", "7. Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "StopWebRent.com")
        biz_phone = st.text_input("Phone", "966572562151")
        biz_email = st.text_input("Email", "hello@stopwebrent.com")
    with c2:
        prod_url = st.text_input("Live URL (for SEO)", "https://www.stopwebrent.com")
        biz_addr = st.text_area("Address", "Kaydiem Script Lab, Kolkata")
        map_iframe = st.text_area("Google Maps Embed Code", height=100)
        seo_d = st.text_area("Meta Description", "Stop paying monthly fees. Own your website forever.")
        logo_url = st.text_input("Logo URL (PNG/SVG)")

    st.subheader("📱 Social & PWA")
    pwa_icon = st.text_input("App Icon URL (512x512)", logo_url)
    lang_sheet = st.text_input("Translation CSV URL")
    sc1, sc2, sc3 = st.columns(3)
    fb_link = sc1.text_input("Facebook URL")
    x_link = sc2.text_input("X (Twitter) URL")
    wa_num = sc3.text_input("WhatsApp Number (No +)", "966572562151")

with tabs[1]:
    hero_h = st.text_input("Hero Headline", st.session_state.hero_h)
    hero_sub = st.text_input("Hero Subtext", st.session_state.hero_sub)
    hc1, hc2, hc3 = st.columns(3)
    hero_img_1 = hc1.text_input("Slide 1 URL", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600")
    hero_img_2 = hc2.text_input("Slide 2 URL", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1600")
    hero_img_3 = hc3.text_input("Slide 3 URL", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1600")
    
    st.divider()
    c1, c2, c3 = st.columns(3)
    stat_1 = c1.text_input("Stat 1 Value", "0.1s")
    label_1 = c1.text_input("Stat 1 Label", "Speed")
    stat_2 = c2.text_input("Stat 2 Value", "$0")
    label_2 = c2.text_input("Stat 2 Label", "Fees")
    stat_3 = c3.text_input("Stat 3 Value", "100%")
    label_3 = c3.text_input("Stat 3 Label", "Ownership")
    
    f_title = st.text_input("Features Section Title", "Value Pillars")
    feat_data_input = st.text_area("Features (icon|Title|Desc)", st.session_state.feat_data, height=150)
    
    about_h_in = st.text_input("About Title", st.session_state.about_h)
    about_img = st.text_input("About Image URL", "https://images.unsplash.com/photo-1543286386-713df548e9cc?q=80&w=1600")
    about_short_in = st.text_area("About Summary", st.session_state.about_short, height=100)
    about_long = st.text_area("About Full Text (Markdown)", "**The Trap**\nMost business owners pay rent for their site...", height=150)

with tabs[2]:
    c1, c2, c3 = st.columns(3)
    titan_price = c1.text_input("Your Product Price", "$199")
    titan_mo = c1.text_input("Your Monthly Cost", "$0")
    wix_name = c2.text_input("Competitor Name", "Wix")
    wix_mo = c2.text_input("Competitor Monthly", "$29/mo")
    save_val = c3.text_input("Total Savings Calculation", "$1,466")

with tabs[3]:
    sheet_url = st.text_input("Google Sheet CSV URL (Store)", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Product Fallback Image", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800")
    c1, c2 = st.columns(2)
    paypal_link = c1.text_input("PayPal.me Link")
    upi_id = c2.text_input("UPI ID (India)")

with tabs[4]:
    booking_title = st.text_input("Booking Section Title", "Schedule a Consultation")
    booking_desc = st.text_area("Booking Description", "Book a 15-minute free audit with our senior architects.")
    booking_embed = st.text_area("Calendly/Cal.com Embed Code", height=100)

with tabs[5]:
    blog_sheet_url = st.text_input("Blog CSV URL")
    blog_hero_title = st.text_input("Blog Header Title", "Titan Insights")
    blog_hero_sub = st.text_input("Blog Subtitle", "Architecting the future of the web.")

with tabs[6]:
    testi_data = st.text_area("Testimonials (Name|Quote)", "Elon M.|This architecture is inevitable.\nS. Jobs|It's simple, but powerful.", height=100)
    faq_data = st.text_area("FAQ (Question? ? Answer)", "Is it really free? ? Yes, you own the code.\nHow fast is it? ? Under 0.1 seconds.", height=100)
    priv_txt = st.text_area("Privacy Policy Text", "We respect your data...", height=100)
    term_txt = st.text_area("Terms of Service Text", "By using this site...", height=100)
    cookie_txt = st.text_input("Cookie Banner Text", "We use cookies to ensure you get the best experience.")

# --- 3. THE TITAN ENGINE (COMPILER) ---

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
    s = {"@context":"https://schema.org","@type":"LocalBusiness","name":biz_name,"url":prod_url,"image":logo_url,"telephone":biz_phone,"email":biz_email,"address":biz_addr}
    return f'<script type="application/ld+json">{json.dumps(s)}</script>'

def gen_pwa_manifest():
    return json.dumps({"name":biz_name,"short_name":biz_name[:10],"start_url":"./index.html","display":"standalone","theme_color":p_color,"background_color":"#ffffff","icons":[{"src":pwa_icon,"sizes":"512x512","type":"image/png"}]})

def gen_sw():
    return """self.addEventListener('install', (e) => { e.waitUntil(caches.open('titan-v1').then((c) => c.addAll(['./index.html']))); }); self.addEventListener('fetch', (e) => { e.respondWith(caches.match(e.request).then((r) => r || fetch(e.request))); });"""

def get_theme_css():
    bg, txt, card, nav = "#ffffff", "#0f172a", "rgba(255,255,255,0.8)", "rgba(255,255,255,0.9)"
    if "Midnight" in theme_mode: bg, txt, card, nav = "#0f172a", "#f8fafc", "rgba(30,41,59,0.9)", "rgba(15,23,42,0.9)"
    if "Cyberpunk" in theme_mode: bg, txt, card, nav = "#050505", "#00ff41", "rgba(20,20,20,0.9)", "rgba(0,0,0,0.9)"
    
    anim_css = ".reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s ease; } .reveal.active { opacity: 1; transform: translateY(0); }"
    if anim_type == "None": anim_css = ""

    return f"""
    :root {{ --p: {p_color}; --s: {s_color}; --bg: {bg}; --txt: {txt}; --card: {card}; --nav: {nav}; --radius: {border_rad}; --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif; }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{ background-color: var(--bg); color: var(--txt); font-family: var(--b-font); margin: 0; line-height: 1.6; overflow-x: hidden; }}
    h1, h2, h3 {{ font-family: var(--h-font); color: var(--txt); font-weight: 800; line-height: 1.2; margin-bottom: 0.5rem; }}
    
    .container {{ max-width: 1280px; margin: 0 auto; padding: 0 24px; }}
    .btn {{ display: inline-flex; align-items: center; justify-content: center; padding: 0.8rem 2rem; border-radius: var(--radius); font-weight: 700; text-transform: uppercase; cursor: pointer; border: none; text-decoration: none; color: white; transition: 0.3s; min-height: 3rem; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }}
    .btn:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.15); opacity: 0.9; }}
    .btn-primary {{ background: var(--p); }} .btn-accent {{ background: var(--s); }}
    
    nav {{ position: fixed; top: 0; width: 100%; z-index: 1000; padding: 1rem 0; background: var(--nav); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(128,128,128,0.1); }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links a {{ margin-left: 2rem; text-decoration: none; font-weight: 600; color: var(--txt); opacity: 0.8; transition:0.2s; position: relative; }}
    .nav-links a::after {{ content: ''; position: absolute; width: 0; height: 2px; bottom: -4px; left: 0; background-color: var(--s); transition: width 0.3s; }}
    .nav-links a:hover::after {{ width: 100%; }}
    .mobile-menu {{ display: none; font-size: 1.5rem; cursor: pointer; }}
    
    .hero {{ min-height: 90vh; display: flex; align-items: center; justify-content: center; position: relative; background: var(--p); padding-top: 80px; overflow: hidden; }}
    .hero-content {{ z-index: 2; width: 100%; text-align: center; }}
    .hero h1 {{ color: white !important; font-size: clamp(2.5rem, 5vw, 4.5rem); text-shadow: 0 4px 20px rgba(0,0,0,0.5); margin-bottom: 1.5rem; }}
    .hero p {{ color: rgba(255,255,255,0.95); max-width: 700px; margin: 0 auto 2rem; font-size: 1.2rem; }}
    .carousel-slide {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0; transition: opacity 1.5s ease-in-out; }}
    .carousel-slide.active {{ opacity: 1; transform: scale(1.05); transition: opacity 1.5s, transform 10s; }}
    .hero-overlay {{ background: linear-gradient(to bottom, rgba(0,0,0,0.3), rgba(0,0,0,0.7)); position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; }}

    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }}
    .about-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }}
    .contact-grid {{ display: grid; grid-template-columns: 1fr 2fr; gap: 3rem; }}
    
    .card {{ background: var(--card); padding: 2.5rem; border-radius: var(--radius); border: 1px solid rgba(128,128,128,0.1); transition: 0.3s; height: 100%; display: flex; flex-direction: column; justify-content: space-between; }}
    .card:hover {{ transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.1); border-color: var(--s); }}
    .prod-img {{ width: 100%; height: 250px; object-fit: cover; border-radius: calc(var(--radius) - 4px); margin-bottom: 1.5rem; background: #f1f5f9; }}
    
    .pricing-table {{ width: 100%; border-collapse: collapse; min-width: 600px; background: var(--card); border-radius: var(--radius); overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }}
    .pricing-table th {{ background: var(--p); color: white; padding: 1.5rem; text-align: left; }}
    .pricing-table td {{ padding: 1.5rem; border-bottom: 1px solid rgba(128,128,128,0.1); }}
    
    .blog-badge {{ background: var(--s); color: white; padding: 0.3rem 0.8rem; border-radius: 50px; font-size: 0.75rem; font-weight: bold; margin-bottom: 1rem; display:inline-block; text-transform: uppercase; letter-spacing: 1px; }}
    
    /* Cart & Widgets */
    #cart-float {{ position: fixed; bottom: 30px; right: 30px; background: var(--p); color: white; padding: 15px 25px; border-radius: 50px; z-index: 998; display: flex; gap: 10px; cursor: pointer; box-shadow: 0 10px 30px rgba(0,0,0,0.2); transition: 0.3s; }}
    #cart-float:hover {{ transform: scale(1.05); }}
    #wa-float {{ position: fixed; bottom: 100px; right: 30px; background: #25D366; color: white; width: 60px; height: 60px; border-radius: 50%; z-index: 997; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2); cursor: pointer; text-decoration: none; transition: 0.3s; }}
    #wa-float:hover {{ transform: scale(1.1); }}
    
    #cart-modal {{ display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: var(--card); width: 90%; max-width: 450px; padding: 2.5rem; border-radius: 16px; z-index: 1001; box-shadow: 0 50px 100px rgba(0,0,0,0.5); border: 1px solid rgba(128,128,128,0.2); backdrop-filter: blur(20px); }}
    #cart-overlay {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 1000; }}
    
    #cookie-banner {{ position: fixed; bottom: 0; left: 0; width: 100%; background: var(--txt); color: var(--bg); padding: 1rem; z-index: 2000; display: flex; justify-content: space-between; align-items: center; transform: translateY(100%); transition: transform 0.5s; }}
    #cookie-banner.show {{ transform: translateY(0); }}
    
    footer {{ background: var(--p); padding: 5rem 0 2rem; color: white; margin-top: auto; }}
    .footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 4rem; margin-bottom: 3rem; }}
    footer a {{ color: rgba(255,255,255,0.7); text-decoration: none; display: block; margin-bottom: 0.8rem; transition: 0.3s; }}
    footer a:hover {{ color: white; transform: translateX(5px); }}
    
    section {{ padding: clamp(4rem, 8vw, 6rem) 0; }}
    details summary {{ cursor: pointer; font-weight: bold; padding: 1rem; background: rgba(0,0,0,0.03); border-radius: 8px; margin-bottom: 0.5rem; list-style: none; }}
    details summary::marker {{ display: none; }}
    details[open] summary {{ background: var(--s); color: white; }}
    details p {{ padding: 1rem; }}
    
    {anim_css}
    
    @media (max-width: 768px) {{
        .hero {{ min-height: 70vh; }}
        .nav-links {{ position: fixed; top: 70px; left: -100%; width: 100%; height: 100vh; background: var(--bg); flex-direction: column; padding: 2rem; align-items: flex-start; transition: 0.3s; border-top: 1px solid rgba(0,0,0,0.1); }}
        .nav-links.active {{ left: 0; }}
        .mobile-menu {{ display: block; }}
        .about-grid, .contact-grid {{ grid-template-columns: 1fr; gap: 2rem; }}
        .detail-view {{ grid-template-columns: 1fr; }}
        h1 {{ font-size: 2.5rem; }}
    }}
    """

def gen_common_js():
    clean_wa = wa_num.replace("+", "").replace(" ", "")
    return f"""
    <script>
    // Scroll Reveal
    window.addEventListener('scroll', () => {{
        document.querySelectorAll('.reveal').forEach(r => {{
            if(r.getBoundingClientRect().top < window.innerHeight - 80) r.classList.add('active');
        }});
    }});
    
    // Mobile Menu
    function toggleMenu() {{ document.querySelector('.nav-links').classList.toggle('active'); }}
    
    // CSV Parsers
    function parseCSVLine(str) {{
        const res = []; let cur = ''; let inQuote = false;
        for (let i = 0; i < str.length; i++) {{
            const c = str[i];
            if (c === '"') {{ if (inQuote && str[i+1] === '"') {{ cur += '"'; i++; }} else {{ inQuote = !inQuote; }} }}
            else if (c === ',' && !inQuote) {{ res.push(cur.trim()); cur = ''; }} else {{ cur += c; }}
        }}
        res.push(cur.trim()); return res;
    }}
    function parseFullCSV(txt) {{
        const rows = []; let row = []; let cur = ''; let inQuote = false;
        for (let i = 0; i < txt.length; i++) {{
            const c = txt[i]; const next = txt[i+1];
            if (c === '"') {{ if (inQuote && next === '"') {{ cur += '"'; i++; }} else {{ inQuote = !inQuote; }} }}
            else if (c === ',' && !inQuote) {{ row.push(cur.trim()); cur = ''; }}
            else if ((c === '\\n' || (c === '\\r' && next === '\\n')) && !inQuote) {{
                row.push(cur.trim()); rows.push(row); row = []; cur = ''; if (c === '\\r') i++;
            }} else {{ cur += c; }}
        }}
        if (cur || row.length) {{ row.push(cur.trim()); rows.push(row); }}
        return rows;
    }}
    function parseMarkdown(text) {{
        if (!text) return '';
        let html = text.replace(/\\r\\n/g, '\\n').replace(/\\n/g, '<br><br>')
                       .replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>')
                       .replace(/\\[(.*?)\\]\\((.*?)\\)/g, '<a href="$2">$1</a>');
        return html;
    }}

    // Cart System
    let cart = JSON.parse(localStorage.getItem('titanCart')) || [];
    function addToCart(name, price) {{
        cart.push({{name, price}});
        localStorage.setItem('titanCart', JSON.stringify(cart));
        updateCartDisplay();
        // Visual Feedback
        const float = document.getElementById('cart-float');
        float.style.transform = 'scale(1.2)';
        setTimeout(() => float.style.transform = 'scale(1)', 200);
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
        if(cart.length === 0) b.innerHTML = '<p>Your cart is empty.</p>';
        cart.forEach((item, i) => {{
            const price = parseFloat(item.price.replace(/[^0-9.]/g, '')) || 0;
            total += price;
            b.innerHTML += `<div style="display:flex; justify-content:space-between; padding:0.8rem 0; border-bottom:1px solid rgba(0,0,0,0.05);">
                <span>${{item.name}}</span>
                <span>${{item.price}} <span onclick="remItem(${{i}})" style="color:red; cursor:pointer; margin-left:10px; font-weight:bold;">×</span></span>
            </div>`;
        }});
        document.getElementById('cart-total').innerText = total.toFixed(2);
    }}
    function remItem(i) {{ cart.splice(i,1); localStorage.setItem('titanCart', JSON.stringify(cart)); renderCartItems(); updateCartDisplay(); }}
    function checkoutWhatsApp() {{
        let msg = "New Order Request:%0A";
        let total = 0;
        cart.forEach(i => {{ msg += `- ${{i.name}} (${{i.price}})%0A`; total += parseFloat(i.price.replace(/[^0-9.]/g,'')) || 0; }});
        msg += `%0ATotal Value: ${{total.toFixed(2)}}%0A%0APreferred Payment: UPI {upi_id} | PayPal {paypal_link}`;
        window.open(`https://wa.me/{clean_wa}?text=${{msg}}`, '_blank');
    }}
    
    // Cookie Banner
    window.addEventListener('load', () => {{
        if(!localStorage.getItem('titanCookie')) {{
            setTimeout(() => document.getElementById('cookie-banner').classList.add('show'), 1000);
        }}
        updateCartDisplay();
    }});
    function acceptCookies() {{
        localStorage.setItem('titanCookie', 'true');
        document.getElementById('cookie-banner').classList.remove('show');
    }}
    </script>
    """

def get_simple_icon(name):
    name = name.lower().strip()
    path = "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"
    if "bolt" in name: path = "M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"
    if "wallet" in name: path = "M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"
    if "shield" in name: path = "M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"
    if "star" in name: path = "M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"
    if "layers" in name: path = "M11.99 18.54l-7.37-5.73L3 14.07l9 7 9-7-1.63-1.27-7.38 5.74zM12 16l7.36-5.73L21 9l-9-7-9 7 1.63 1.27L12 16z"
    if "table" in name: path = "M10 10.02h5V21h-5zM17 21h3c1.1 0 2-.9 2-2v-9h-5v11zm3-18H5c-1.1 0-2 .9-2 2v3h19V5c0-1.1-.9-2-2-2zM3 19c0 1.1.9 2 2 2h3V10H3v9z"
    return f'<svg viewBox="0 0 24 24" width="40" height="40" fill="currentColor"><path d="{path}"/></svg>'

# --- SECTION GENERATORS ---
def gen_hero():
    return f"""
    <section class="hero">
        <div class="hero-overlay"></div>
        <div class="carousel-slide active" style="background-image: url('{hero_img_1}')"></div>
        <div class="carousel-slide" style="background-image: url('{hero_img_2}')"></div>
        <div class="carousel-slide" style="background-image: url('{hero_img_3}')"></div>
        <div class="container hero-content reveal active">
            <h1>{hero_h}</h1>
            <p>{hero_sub}</p>
            <div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
                <a href="#pricing" class="btn btn-accent">See Pricing</a>
                <a href="contact.html" class="btn" style="background:rgba(255,255,255,0.15); backdrop-filter:blur(5px); border:1px solid rgba(255,255,255,0.3);">Contact Us</a>
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
        }}, 5000);
    </script>
    """

def gen_features():
    cards = ""
    for line in feat_data_input.split('\n'):
        if "|" in line:
            parts = line.split('|')
            cards += f"""
            <div class="card reveal">
                <div style="color:var(--s); margin-bottom:1.5rem; background:rgba(0,0,0,0.03); width:fit-content; padding:1rem; border-radius:50%;">{get_simple_icon(parts[0])}</div>
                <h3>{parts[1].strip()}</h3>
                <div>{format_text(parts[2].strip())}</div>
            </div>"""
    return f"""<section id="features"><div class="container"><div class="section-head reveal" style="text-align:center; margin-bottom:3rem;"><h2>{f_title}</h2><div style="width:60px; height:4px; background:var(--s); margin:1rem auto;"></div></div><div class="grid-3">{cards}</div></div></section>"""

def gen_stats():
    return f"""
    <div style="background:var(--p); color:white; padding:4rem 0; text-align:center;">
        <div class="container grid-3">
            <div class="reveal"><h3 style="color:#ffffff; margin:0; font-size:3.5rem;">{stat_1}</h3><p style="color:rgba(255,255,255,0.7); text-transform:uppercase; letter-spacing:1px;">{label_1}</p></div>
            <div class="reveal"><h3 style="color:#ffffff; margin:0; font-size:3.5rem;">{stat_2}</h3><p style="color:rgba(255,255,255,0.7); text-transform:uppercase; letter-spacing:1px;">{label_2}</p></div>
            <div class="reveal"><h3 style="color:#ffffff; margin:0; font-size:3.5rem;">{stat_3}</h3><p style="color:rgba(255,255,255,0.7); text-transform:uppercase; letter-spacing:1px;">{label_3}</p></div>
        </div>
    </div>
    """

def gen_pricing():
    if not show_pricing: return ""
    return f"""
    <section id="pricing" style="background:#f8fafc"><div class="container">
        <div class="section-head reveal" style="text-align:center; margin-bottom:3rem;"><h2>Transparent Pricing</h2></div>
        <div class="reveal" style="max-width:800px; margin:0 auto;">
            <table class="pricing-table">
                <thead><tr><th>Expense Item</th><th style="background:var(--s); font-size:1.2rem;">Titan Engine</th><th>{wix_name}</th></tr></thead>
                <tbody>
                    <tr><td><strong>Initial Setup</strong></td><td><strong>{titan_price}</strong></td><td>$0</td></tr>
                    <tr><td><strong>Monthly Hosting</strong></td><td><strong>{titan_mo}</strong></td><td>{wix_mo}</td></tr>
                    <tr><td><strong>Platform Lock-in</strong></td><td><strong>None</strong></td><td>High</td></tr>
                    <tr style="background:rgba(0,0,0,0.02);"><td><strong>10-Year Cost</strong></td><td style="color:var(--s); font-size:1.5rem; font-weight:800;">{save_val} Savings</td><td>$$$ Expensive</td></tr>
                </tbody>
            </table>
            <div style="text-align:center; margin-top:2rem;"><a href="contact.html" class="btn btn-primary">Claim Your Build</a></div>
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
                        <div style="overflow:hidden; border-radius:8px; margin-bottom:1rem;">
                            <img src="${{img}}" class="prod-img" style="margin:0; transition:0.5s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" loading="lazy">
                        </div>
                        <div>
                            <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                                <h3>${{c[0]}}</h3>
                                <span style="font-weight:bold; color:var(--s); background:rgba(0,0,0,0.05); padding:2px 8px; border-radius:4px;">${{c[1]}}</span>
                            </div>
                            <p style="font-size:0.9rem; opacity:0.8; margin-bottom:1.5rem;">${{c[2]}}</p>
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
        <div class="section-head reveal" style="text-align:center; margin-bottom:3rem;"><h2>Our Products</h2></div>
        <div id="inv-grid" class="grid-3"><div style="text-align:center; padding:4rem; width:100%;">Loading products from Cloud...</div></div>
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
                <div style="width:60px; height:4px; background:var(--s); margin:1rem 0 2rem;"></div>
                <div style="font-size:1.1rem; opacity:0.9; margin-bottom:2rem;">{formatted_about}</div>
                <a href="about.html" class="btn btn-primary">Read Our Story</a>
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
    return f"""<section id="faq"><div class="container" style="max-width:800px;"><div class="section-head reveal" style="text-align:center; margin-bottom:3rem;"><h2>Frequently Asked Questions</h2></div>{items}</div></section>"""

def gen_footer():
    wa_float_html = ""
    if show_whatsapp_float:
        clean_wa = wa_num.replace("+", "").replace(" ", "")
        wa_float_html = f"""<a href="https://wa.me/{clean_wa}" target="_blank" id="wa-float" title="Chat on WhatsApp"><svg viewBox="0 0 24 24" width="32" height="32" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.008-.57-.008-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg></a>"""
    
    cookie_banner = ""
    if show_cookie:
        cookie_banner = f"""<div id="cookie-banner"><div>{cookie_txt}</div><button onclick="acceptCookies()" class="btn btn-primary" style="padding:0.5rem 1rem; font-size:0.8rem; margin-left:1rem;">Accept</button></div>"""

    return f"""
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div><h3>{biz_name}</h3><p style="opacity:0.7;">{biz_addr}</p><p><a href="tel:{biz_phone}">{biz_phone}</a><a href="mailto:{biz_email}">{biz_email}</a></p></div>
                <div><h4>Navigate</h4><a href="index.html">Home</a><a href="about.html">About Us</a><a href="contact.html">Contact</a></div>
                <div><h4>Legal</h4><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a></div>
            </div>
            <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:2rem; text-align:center; opacity:0.6; font-size:0.8rem;">
                &copy; {datetime.datetime.now().year} {biz_name}. All rights reserved. Powered by Titan Engine.
            </div>
        </div>
    </footer>
    {wa_float_html}
    {cookie_banner}
    """

def gen_booking_content():
    return f"""<section class="hero" style="min-height:50vh;background:var(--p);"><div class="container reveal"><h1>{booking_title}</h1><p>{booking_desc}</p></div></section><section><div class="container reveal" style="text-align:center;"><div style="background:white; border-radius:12px; box-shadow:0 10px 40px rgba(0,0,0,0.1); overflow:hidden; min-height:600px;">{booking_embed}</div></div></section>"""

def gen_blog_index_html():
    return f"""
    <section class="hero" style="min-height:50vh; background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('{hero_img_1}'); background-size: cover; background-attachment: fixed;">
        <div class="container"><h1 id="blog-title">{blog_hero_title}</h1><p id="blog-sub">{blog_hero_sub}</p></div>
    </section>
    <section><div class="container"><div id="blog-grid" class="grid-3">Loading Articles...</div></div></section>
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
                if(r.length > 4) box.innerHTML += `<div class="card reveal"><img src="${{r[5]}}" class="prod-img"><div><span class="blog-badge">${{r[3]}}</span><h3><a href="post.html?id=${{r[0]}}" style="color:var(--txt);text-decoration:none">${{r[1]}}</a></h3><p style="opacity:0.7">${{r[2]}}</p></div></div>`;
            }}
        }} catch(e) {{}}
    }}
    loadBlog();
    </script>
    """

def gen_blog_post_html():
    return f"""
    <div id="post-container" style="padding-top:100px;">Loading Post...</div>
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
                        <div style="background:var(--p);padding:6rem 1rem;color:white;text-align:center;">
                            <div class="container"><span class="blog-badge">${{r[3]}}</span><h1>${{r[1]}}</h1><p style="opacity:0.8">${{r[2]}}</p></div>
                        </div>
                        <div class="container" style="max-width:800px;padding:4rem 1rem;">
                            <img src="${{r[5]}}" style="width:100%;border-radius:12px;margin-bottom:3rem;box-shadow:0 10px 30px rgba(0,0,0,0.1);">
                            <div style="line-height:1.8;font-size:1.15rem;">${{content}}</div>
                        </div>
                    `;
                    document.title = r[1] + " | Blog";
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
    <section style="padding:150px 0;"><div class="container" id="prod-box">Loading Product...</div></section>
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
                        <div class="about-grid">
                            <img src="${{col[3]}}" style="width:100%; border-radius:20px; box-shadow:0 10px 40px rgba(0,0,0,0.1);">
                            <div>
                                <span style="background:var(--s); color:white; padding:5px 10px; border-radius:5px; font-weight:bold;">${{col[1]}}</span>
                                <h1 style="font-size:3rem; margin:1rem 0;">${{col[0]}}</h1>
                                <p style="font-size:1.2rem; opacity:0.8; margin-bottom:2rem;">${{col[2]}}</p>
                                <button class="btn btn-primary" onclick="addToCart('${{col[0]}}','${{col[1]}}')" style="width:100%; padding:1.2rem;">Add to Cart</button>
                            </div>
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
    return f"""<section class="hero" style="min-height: 40vh; background:var(--p);"><div class="container reveal"><h1>{title}</h1></div></section>"""

# --- 4. THE MASTER BUILDER ---

def build_page(title, content):
    # Dynamic Navigation Construction
    nav_links_html = f"""<a href="index.html">Home</a>"""
    if show_gallery: nav_links_html += f"""<a href="about.html">About</a>"""
    if show_features: nav_links_html += f"""<a href="index.html#features">Features</a>"""
    if show_pricing: nav_links_html += f"""<a href="index.html#pricing">Pricing</a>"""
    if show_inventory: nav_links_html += f"""<a href="product.html">Store</a>"""
    if show_booking: nav_links_html += f"""<a href="booking.html">Book</a>"""
    if show_blog: nav_links_html += f"""<a href="blog.html">Blog</a>"""
    nav_links_html += f"""<a href="contact.html">Contact</a>"""
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} | {biz_name}</title>
        <meta name="description" content="{seo_d}">
        <meta property="og:title" content="{title} | {biz_name}">
        <meta property="og:description" content="{seo_d}">
        <meta property="og:image" content="{og_image if og_image else logo_url}">
        <link rel="icon" type="image/png" href="{pwa_icon}">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Lato&family=Montserrat:wght@400;700&family=Oswald&family=Open+Sans&family=Playfair+Display&family=Roboto&family=Space+Grotesk&display=swap" rel="stylesheet">
        <style>{get_theme_css()}</style>
        {gen_schema()}
    </head>
    <body>
        <nav>
            <div class="container nav-flex">
                <a href="index.html" style="display:flex; align-items:center; gap:10px; font-size:1.5rem; font-weight:bold; text-decoration:none; color:var(--txt);">
                    <img src="{logo_url}" style="height:40px;" onerror="this.style.display='none'"> {biz_name}
                </a>
                <div class="mobile-menu" onclick="toggleMenu()">☰</div>
                <div class="nav-links">
                    {nav_links_html}
                    <div style="display:inline-block; margin-left:2rem; cursor:pointer; position:relative;" onclick="toggleCart()">
                        🛒 <span id="cart-count" style="background:var(--s); color:white; padding:2px 6px; border-radius:50%; font-size:0.8rem; position:absolute; top:-10px; right:-10px;">0</span>
                    </div>
                </div>
            </div>
        </nav>
        
        <!-- Cart Overlay -->
        <div id="cart-overlay" onclick="toggleCart()"></div>
        <div id="cart-modal">
            <h3 style="border-bottom:1px solid rgba(0,0,0,0.1); padding-bottom:1rem; margin-bottom:1rem;">Your Cart</h3>
            <div id="cart-items" style="max-height:300px; overflow-y:auto; margin-bottom:1rem;"></div>
            <div style="margin-top:1rem; border-top:1px solid #eee; padding-top:1rem; display:flex; justify-content:space-between; font-weight:bold; font-size:1.2rem;">
                <span>Total</span>
                <span id="cart-total">0.00</span>
            </div>
            <button class="btn btn-accent" style="width:100%; margin-top:1.5rem;" onclick="checkoutWhatsApp()">Checkout via WhatsApp</button>
        </div>
        <div id="cart-float" onclick="checkoutWhatsApp()" style="display:none;">
            <span>Processing...</span>
        </div>

        {content}
        
        {gen_footer()}
        {gen_common_js()}
    </body>
    </html>
    """

# --- 5. PREVIEW & EXPORT ---
# Assemble Home Content based on Toggles
home_content = ""
if show_hero: home_content += gen_hero()
if show_stats: home_content += gen_stats()
if show_features: home_content += gen_features()
if show_pricing: home_content += gen_pricing()
if show_inventory: home_content += gen_inventory()
if show_gallery: home_content += gen_about_section()
if show_testimonials: 
    t_cards = "".join([f'<div class="card reveal" style="text-align:center;"><p style="font-size:1.2rem; font-style:italic; margin-bottom:1.5rem;">"{x.split("|")[1]}"</p><div style="font-weight:bold; color:var(--s);">- {x.split("|")[0]}</div></div>' for x in testi_data.split('\n') if "|" in x])
    home_content += f'<section style="background:#f8fafc"><div class="container"><div class="section-head reveal" style="text-align:center; margin-bottom:3rem;"><h2>Client Stories</h2></div><div class="grid-3">{t_cards}</div></div></section>'
if show_faq: home_content += gen_faq_section()
if show_cta: home_content += f'<section style="background:var(--s); color:white; text-align:center;"><div class="container reveal"><h2>Ready to Scale?</h2><p style="margin-bottom:2rem; font-size:1.2rem; opacity:0.9;">Join the future of web architecture today.</p><a href="contact.html" class="btn" style="background:white; color:var(--s);">Get Started Now</a></div></section>'

st.divider()
c1, c2 = st.columns([3, 1])
with c1:
    prev = st.radio("Live Preview Mode", ["Home", "Product Details", "Blog Index", "Blog Post", "Booking", "Privacy", "Terms", "Contact"], horizontal=True)
    
    if prev == "Home": st.components.v1.html(build_page("Home", home_content), height=700, scrolling=True)
    elif prev == "Product Details": st.components.v1.html(build_page("Product", gen_product_page_content(True)), height=700, scrolling=True)
    elif prev == "Blog Index": st.components.v1.html(build_page("Blog", gen_blog_index_html()), height=700, scrolling=True)
    elif prev == "Blog Post": st.components.v1.html(build_page("Article", gen_blog_post_html()), height=700, scrolling=True)
    elif prev == "Booking": st.components.v1.html(build_page("Book", gen_booking_content()), height=700, scrolling=True)
    elif prev == "Privacy": st.components.v1.html(build_page("Privacy", f"{gen_inner_header('Privacy Policy')}<div class='container' style='padding:4rem 1rem;'>{format_text(priv_txt)}</div>"), height=700, scrolling=True)
    elif prev == "Terms": st.components.v1.html(build_page("Terms", f"{gen_inner_header('Terms of Service')}<div class='container' style='padding:4rem 1rem;'>{format_text(term_txt)}</div>"), height=700, scrolling=True)
    elif prev == "Contact": 
        contact_html = f"""{gen_inner_header("Contact Us")}<section><div class="container"><div class="contact-grid"><div><div class="card"><h3>Get In Touch</h3><p>{biz_addr}</p><p><a href="tel:{biz_phone}" style="color:var(--s); font-weight:bold;">{biz_phone}</a></p><p>{biz_email}</p></div></div><div class="card"><h3>Send Message</h3><form action="https://formsubmit.co/{biz_email}" method="POST"><input type="hidden" name="_captcha" value="false"><label>Name</label><input type="text" name="name" required style="width:100%; padding:10px; margin-bottom:1rem; border:1px solid #ddd; border-radius:4px;"><label>Email</label><input type="email" name="email" required style="width:100%; padding:10px; margin-bottom:1rem; border:1px solid #ddd; border-radius:4px;"><label>Message</label><textarea name="msg" rows="4" required style="width:100%; padding:10px; margin-bottom:1rem; border:1px solid #ddd; border-radius:4px;"></textarea><button class="btn btn-primary" type="submit" style="width:100%;">Send Message</button></form></div></div><br><div style="border-radius:12px;overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.1);">{map_iframe}</div></div></section>"""
        st.components.v1.html(build_page("Contact", contact_html), height=700, scrolling=True)

with c2:
    st.markdown("### 🚀 Launch System")
    st.write("Ready to deploy? Download your source code.")
    if st.button("DOWNLOAD FULL SITE ZIP", type="primary"):
        z_b = io.BytesIO()
        with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as zf:
            # Core Pages
            zf.writestr("index.html", build_page("Home", home_content))
            zf.writestr("about.html", build_page("About Us", f"{gen_inner_header('About Us')}<div class='container' style='padding:4rem 1rem;'>{format_text(about_long)}</div>"))
            
            # Contact Logic
            contact_html = f"""{gen_inner_header("Contact Us")}<section><div class="container"><div class="contact-grid"><div><div class="card"><h3>Get In Touch</h3><p>{biz_addr}</p><p><a href="tel:{biz_phone}" style="color:var(--s); font-weight:bold;">{biz_phone}</a></p><p>{biz_email}</p></div></div><div class="card"><h3>Send Message</h3><form action="https://formsubmit.co/{biz_email}" method="POST"><input type="hidden" name="_captcha" value="false"><label>Name</label><input type="text" name="name" required style="width:100%; padding:10px; margin-bottom:1rem; border:1px solid #ddd; border-radius:4px;"><label>Email</label><input type="email" name="email" required style="width:100%; padding:10px; margin-bottom:1rem; border:1px solid #ddd; border-radius:4px;"><label>Message</label><textarea name="msg" rows="4" required style="width:100%; padding:10px; margin-bottom:1rem; border:1px solid #ddd; border-radius:4px;"></textarea><button class="btn btn-primary" type="submit" style="width:100%;">Send Message</button></form></div></div><br><div style="border-radius:12px;overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.1);">{map_iframe}</div></div></section>"""
            zf.writestr("contact.html", build_page("Contact", contact_html))
            
            # Legal
            zf.writestr("privacy.html", build_page("Privacy Policy", f"{gen_inner_header('Privacy Policy')}<div class='container' style='padding:4rem 1rem;'>{format_text(priv_txt)}</div>"))
            zf.writestr("terms.html", build_page("Terms of Service", f"{gen_inner_header('Terms of Service')}<div class='container' style='padding:4rem 1rem;'>{format_text(term_txt)}</div>"))
            
            # Functional
            if show_booking: zf.writestr("booking.html", build_page("Book Appointment", gen_booking_content()))
            if show_inventory: zf.writestr("product.html", build_page("Product Details", gen_product_page_content(is_demo=False)))
            if show_blog:
                zf.writestr("blog.html", build_page("Blog", gen_blog_index_html()))
                zf.writestr("post.html", build_page("Article", gen_blog_post_html()))
            
            # Technical
            zf.writestr("manifest.json", gen_pwa_manifest())
            zf.writestr("service-worker.js", gen_sw())
            zf.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {prod_url}/sitemap.xml")
            
        st.download_button("📥 Click to Save .ZIP", z_b.getvalue(), "titan_site_v40.zip", "application/zip")
