import streamlit as st
import zipfile
import io
import json
import datetime
import re
import requests

# --- 0. STATE MANAGEMENT (Prevents NameErrors) ---
def init_state(key, default_val):
    if key not in st.session_state:
        st.session_state[key] = default_val

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Titan v39.0 | Ultimate Stable", 
    layout="wide", 
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# --- 2. CSS ENGINE ---
st.markdown("""
    <style>
    :root { --primary: #0f172a; --accent: #ef4444; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important; border: 1px solid #cbd5e1 !important; border-radius: 8px !important; color: #0f172a !important;
    }
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3.5rem;
        background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
        color: white; font-weight: 800; border: none;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.3); text-transform: uppercase; letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v39.0 | No Errors Edition")
    st.divider()
    
    # AI GENERATOR
    with st.expander("🤖 Titan AI Generator", expanded=False):
        raw_key = st.text_input("Groq API Key", type="password")
        groq_key = raw_key.strip() if raw_key else ""
        biz_desc = st.text_input("Business Description")
        if st.button("✨ Generate Copy"):
            if not groq_key or not biz_desc:
                st.error("Key & Description required.")
            else:
                try:
                    with st.spinner("Writing..."):
                        url = "https://api.groq.com/openai/v1/chat/completions"
                        headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
                        prompt = f"Act as a copywriter. Return JSON for '{biz_desc}': hero_h, hero_sub, about_h, about_short, feat_data (icon|Title|Desc format)."
                        data = {"messages": [{"role": "user", "content": prompt}], "model": "llama-3.1-8b-instant", "response_format": {"type": "json_object"}}
                        resp = requests.post(url, headers=headers, json=data)
                        if resp.status_code == 200:
                            res = resp.json()['choices'][0]['message']['content']
                            parsed = json.loads(res)
                            for k,v in parsed.items():
                                if k == 'feat_data' and isinstance(v, list): v = "\n".join(v)
                                st.session_state[k] = str(v)
                            st.success("Generated! Refreshing...")
                            st.rerun()
                except Exception as e: st.error(f"Error: {e}")

    # DESIGN STUDIO
    with st.expander("🎨 Design Studio", expanded=True):
        theme_mode = st.selectbox("Base Theme", ["Clean Corporate", "Midnight SaaS", "Glassmorphism", "Cyberpunk Neon", "Luxury Gold", "Forest Eco", "Ocean Breeze", "Stark Minimalist"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#0F172A") 
        s_color = c2.color_picker("Action (CTA)", "#EF4444")  
        h_font = st.selectbox("Headings", ["Montserrat", "Space Grotesk", "Playfair Display", "Oswald", "Clash Display"])
        b_font = st.selectbox("Body Text", ["Inter", "Open Sans", "Roboto", "Satoshi", "Lora"])
        
        st.markdown("**Layout**")
        hero_layout = st.selectbox("Hero Alignment", ["Center", "Left"])
        btn_style = st.selectbox("Button Style", ["Rounded", "Sharp", "Pill"])
        border_rad = "8px"
        if btn_style == "Sharp": border_rad = "0px"
        elif btn_style == "Pill": border_rad = "50px"
        anim_type = st.selectbox("Animation", ["Fade Up", "Zoom In", "Slide Right", "None"])

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
        gsc_tag = st.text_input("Google Verification ID")
        ga_tag = st.text_input("Google Analytics ID")
        og_image = st.text_input("Social Share Image URL")

# --- 4. INPUT TABS ---
st.title("🏗️ StopWebRent Site Builder v39.0")
tabs = st.tabs(["1. Identity", "2. Content", "3. Marketing", "4. Pricing", "5. Store", "6. Booking", "7. Blog", "8. Legal"])

# INITIALIZE SESSION STATE DEFAULTS
init_state('hero_h', "Stop Paying Rent for Your Website.")
init_state('hero_sub', "The Titan Engine is the world’s first 0.1s website architecture that runs on $0 monthly fees.")
init_state('about_h', "Control Your Empire")
init_state('about_short', "No WordPress dashboard. Just open your private Google Sheet.")
init_state('feat_data', "bolt | Speed | 0.1s Load Time\nwallet | Cost | $0 Monthly\ntable | CMS | Google Sheets\nshield | Secure | Zero-DB")

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "StopWebRent.com")
        biz_tagline = st.text_input("Tagline", "Stop Renting. Start Owning.")
        biz_phone = st.text_input("Phone", "966572562151")
        biz_email = st.text_input("Email", "hello@kaydiemscriptlab.com")
    with c2:
        prod_url = st.text_input("Website URL", "https://www.stopwebrent.com")
        biz_addr = st.text_area("Address", "Kaydiem Script Lab\nKolkata, India", height=100)
        map_iframe = st.text_area("Map Embed", placeholder='<iframe src="..."></iframe>', height=100)
        seo_d = st.text_area("Meta Desc", "Stop paying monthly fees.", height=100)
        logo_url = st.text_input("Logo URL (PNG/SVG)")

    st.subheader("📱 PWA & Lang")
    pwa_short = st.text_input("App Name", biz_name[:12])
    pwa_icon = st.text_input("App Icon (512px)", logo_url)
    lang_sheet = st.text_input("Translation Sheet CSV URL")

    st.subheader("Social Links")
    sc1, sc2, sc3 = st.columns(3)
    fb_link = sc1.text_input("Facebook")
    ig_link = sc2.text_input("Instagram")
    x_link = sc3.text_input("Twitter/X")
    li_link = st.text_input("LinkedIn")
    yt_link = st.text_input("YouTube")
    wa_num = st.text_input("WhatsApp (No +)", "966572562151")

with tabs[1]:
    st.subheader("Hero")
    hero_h = st.text_input("Headline", st.session_state.hero_h)
    hero_sub = st.text_input("Subtext", st.session_state.hero_sub)
    hero_video_id = st.text_input("YouTube Video BG ID (Optional)")
    hc1, hc2, hc3 = st.columns(3)
    hero_img_1 = hc1.text_input("Slide 1", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600")
    hero_img_2 = hc2.text_input("Slide 2", "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1600")
    hero_img_3 = hc3.text_input("Slide 3", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1600")
    
    st.divider()
    st.subheader("Stats & Features")
    c1, c2, c3 = st.columns(3)
    stat_1 = c1.text_input("Stat 1", "0.1s")
    label_1 = c1.text_input("Label 1", "Speed")
    stat_2 = c2.text_input("Stat 2", "$0")
    label_2 = c2.text_input("Label 2", "Fees")
    stat_3 = c3.text_input("Stat 3", "100%")
    label_3 = c3.text_input("Label 3", "Ownership")
    f_title = st.text_input("Feat. Title", "Value Pillars")
    feat_data_input = st.text_area("Features", st.session_state.feat_data, height=150)
    
    st.subheader("About")
    about_h_in = st.text_input("About Title", st.session_state.about_h)
    about_img = st.text_input("About Img", "https://images.unsplash.com/photo-1543286386-713df548e9cc?q=80&w=1600")
    about_short_in = st.text_area("Short Summary", st.session_state.about_short)
    about_long = st.text_area("Full Content", "The Digital Landlord Trap...", height=200)

with tabs[2]:
    st.subheader("📣 Marketing")
    top_bar_enabled = st.checkbox("Top Promo Bar")
    top_bar_text = st.text_input("Promo Text", "🔥 50% OFF Launch Sale!")
    top_bar_link = st.text_input("Promo Link", "#pricing")
    popup_enabled = st.checkbox("Exit Intent Popup")
    popup_delay = st.slider("Popup Delay (s)", 1, 30, 5)
    popup_title = st.text_input("Popup Title", "Wait! Get the Guide.")
    popup_text = st.text_input("Popup Text", "Free PDF on WhatsApp.")
    popup_cta = st.text_input("Popup Button", "Get it Now")

with tabs[3]:
    st.subheader("💰 Pricing")
    c1, c2, c3 = st.columns(3)
    titan_price = c1.text_input("Our Price", "$199")
    titan_mo = c1.text_input("Our Monthly", "$0")
    wix_name = c2.text_input("Comp. Name", "Wix")
    wix_mo = c2.text_input("Comp. Monthly", "$29/mo")
    save_val = c3.text_input("Total Savings", "$1,466")

with tabs[4]:
    st.subheader("🛒 Store Config")
    st.info("CSV Columns: Name, Price, Description, ImageURLs (use | to split), StripeLink")
    sheet_url = st.text_input("Store CSV", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Default Product Img", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800")
    c1, c2 = st.columns(2)
    paypal_link = c1.text_input("PayPal Link")
    upi_id = c2.text_input("UPI ID")

with tabs[5]:
    st.subheader("📅 Booking")
    booking_embed = st.text_area("Calendly Embed", height=100)
    booking_title = st.text_input("Book Title", "Book an Appointment")
    booking_desc = st.text_input("Book Subtext", "Select a slot.")

with tabs[6]:
    st.subheader("📰 Blog")
    blog_sheet_url = st.text_input("Blog CSV")
    blog_hero_title = st.text_input("Blog Title", "Insights")
    blog_hero_sub = st.text_input("Blog Subtext", "News & Updates")

with tabs[7]:
    st.subheader("Legal")
    testi_data = st.text_area("Testimonials", "Name | Quote", height=100)
    faq_data = st.text_area("FAQ", "Q? ? A", height=100)
    priv_txt = st.text_area("Privacy Policy", "Text...", height=100)
    term_txt = st.text_area("Terms", "Text...", height=100)

# --- 5. COMPILER FUNCTIONS (DEFINED BEFORE USAGE) ---

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
    s = {"@context":"https://schema.org","@type":"LocalBusiness","name":biz_name,"image":logo_url,"url":prod_url}
    return f'<script type="application/ld+json">{json.dumps(s)}</script>'

def gen_pwa_manifest():
    return json.dumps({
        "name": biz_name, "short_name": pwa_short, "start_url": "./index.html",
        "display": "standalone", "background_color": "#ffffff", "theme_color": p_color,
        "description": "Official App", "icons": [{"src": pwa_icon, "sizes": "512x512", "type": "image/png"}]
    })

def gen_sw():
    return """self.addEventListener('install', (e) => { e.waitUntil(caches.open('titan-v1').then((c) => c.addAll(['./index.html']))); }); self.addEventListener('fetch', (e) => { e.respondWith(caches.match(e.request).then((r) => r || fetch(e.request))); });"""

def get_theme_css():
    bg, txt, card, nav = "#ffffff", "#0f172a", "rgba(255,255,255,0.8)", "rgba(255,255,255,0.9)"
    if "Midnight" in theme_mode: bg, txt, card, nav = "#0f172a", "#f8fafc", "rgba(30,41,59,0.9)", "rgba(15,23,42,0.9)"
    if "Cyberpunk" in theme_mode: bg, txt, card, nav = "#050505", "#00ff9d", "rgba(10,10,10,0.9)", "rgba(0,0,0,0.9)"
    if "Luxury" in theme_mode: bg, txt, card, nav = "#101010", "#D4AF37", "rgba(20,20,20,0.9)", "rgba(0,0,0,0.9)"

    align_css = "text-align:center; align-items:center;" if hero_layout == "Center" else "text-align:left; align-items:flex-start;"
    anim_css = ".reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s ease; } .reveal.active { opacity: 1; transform: translateY(0); }"
    if anim_type == "None": anim_css = ""

    return f"""
    :root {{ --p: {p_color}; --s: {s_color}; --bg: {bg}; --txt: {text_color}; --card: {card}; --nav: {nav}; }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{ background-color: var(--bg); color: var(--txt); font-family: var(--b-font); margin: 0; line-height: 1.6; overflow-x: hidden; }}
    body.dark-mode {{ --bg: #0f172a; --txt: #f8fafc; --card: rgba(30,41,59,0.9); --nav: rgba(15,23,42,0.95); }}
    
    h1, h2, h3, h4 {{ font-family: var(--h-font); color: var(--txt); font-weight: 800; line-height: 1.2; margin-bottom: 0.5rem; }}
    h1 {{ font-size: clamp(2.5rem, 6vw, 5rem); }}
    h2 {{ font-size: clamp(2rem, 4vw, 3rem); }}
    p {{ margin-bottom: 1rem; opacity: 0.9; }}
    
    /* GLASS & UI */
    nav, .card, #cart-modal, #lead-popup {{ backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border: 1px solid rgba(128,128,128,0.1); }}
    .container {{ max-width: 1280px; margin: 0 auto; padding: 0 24px; }}
    
    /* BUTTONS */
    .btn {{ 
        display: inline-flex; align-items: center; justify-content: center;
        padding: 1rem 2rem; border-radius: {border_rad}; font-weight: 700; 
        text-transform: uppercase; letter-spacing: 0.5px; transition: all 0.3s;
        cursor: pointer; border: none; text-decoration: none; overflow: hidden;
        white-space: normal; line-height: 1.2; text-align: center; min-height: 3.5rem; word-break: break-word;
    }}
    .btn-primary {{ background: var(--p); color: white !important; box-shadow: 0 10px 30px -10px var(--p); }}
    .btn-accent {{ background: var(--s); color: white !important; box-shadow: 0 10px 30px -10px var(--s); }}
    .btn:hover {{ transform: translateY(-4px); filter: brightness(1.1); }}
    
    /* HERO */
    .hero {{ min-height: 90vh; display: flex; flex-direction: column; justify-content: center; position: relative; background: var(--p); padding-top: 80px; overflow: hidden; }}
    .hero-content {{ z-index: 2; width: 100%; max-width: 1280px; margin: 0 auto; padding: 0 24px; display: flex; flex-direction: column; {align_css} }}
    .hero h1 {{ color: white !important; text-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
    .hero p {{ color: rgba(255,255,255,0.95); max-width: 650px; font-size: 1.2rem; margin-bottom: 2rem; }}
    .carousel-slide {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0; transition: opacity 1.5s; z-index: 0; }}
    .carousel-slide.active {{ opacity: 1; }}
    .hero-overlay {{ background: rgba(0,0,0,0.5); position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; }}
    
    /* NAV */
    nav {{ position: fixed; top: 0; width: 100%; z-index: 1000; padding: 1rem 0; background: var(--nav); transition: top 0.3s; }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links {{ display: flex; gap: 2rem; align-items: center; }}
    .nav-links a {{ font-weight: 600; color: var(--txt); opacity: 0.8; transition: 0.2s; text-decoration: none; }}
    .nav-links a:hover {{ opacity: 1; color: var(--s); }}
    
    /* PRODUCT CARDS (APPLE STYLE) */
    .product-card {{ background: white; border-radius: 16px; overflow: hidden; transition: 0.4s; display: flex; flex-direction: column; border: none; box-shadow: 0 5px 20px rgba(0,0,0,0.05); }}
    .product-card:hover {{ transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0,0,0,0.1); }}
    .prod-img {{ width: 100%; height: 250px; object-fit: cover; background: #f1f5f9; }}
    .card-content {{ padding: 1.5rem; display: flex; flex-direction: column; flex-grow: 1; }}
    /* Force Dark Text for Product Cards specifically if card bg is white */
    .product-card h3 {{ color: #1e293b !important; font-size: 1.25rem; }}
    .product-card p {{ color: #64748b !important; }}
    
    /* GRIDS */
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }}
    .about-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center; }}
    
    /* FOOTER */
    footer {{ background: var(--p); padding: 4rem 0; color: white; margin-top: auto; }}
    .footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; }}
    footer a {{ color: rgba(255,255,255,0.7) !important; text-decoration: none; display: block; margin-bottom: 0.8rem; }}
    footer a:hover {{ color: white !important; text-decoration: underline; }}
    
    /* UTILS & PADDING */
    section {{ padding: clamp(2rem, 5vw, 3.5rem) 0; }}
    .section-head {{ text-align: center; margin-bottom: clamp(1.5rem, 4vw, 2.5rem); }}
    
    /* SOCIAL SHARE */
    .share-row {{ display: flex; gap: 10px; margin-top: 15px; flex-wrap: wrap; }}
    .share-btn {{ width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border-radius: 50%; transition: 0.3s; background: #eee; }}
    .share-btn:hover {{ transform: scale(1.1); filter: brightness(0.9); }}
    .share-btn svg {{ width: 18px; height: 18px; fill: #333; }}
    .bg-fb {{ background: #1877F2; }} .bg-fb svg {{ fill: white; }}
    .bg-x {{ background: #000000; }} .bg-x svg {{ fill: white; }}
    .bg-li {{ background: #0A66C2; }} .bg-li svg {{ fill: white; }}
    .bg-rd {{ background: #FF4500; }} .bg-rd svg {{ fill: white; }}
    .bg-wa {{ background: #25D366; }} .bg-wa svg {{ fill: white; }}
    
    #top-bar {{ background: var(--s); color: white; text-align: center; padding: 0.8rem; font-weight: 700; font-size: 0.9rem; position: fixed; width: 100%; top: 0; z-index: 1001; }}
    #lead-popup {{ display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: var(--card); padding: 3rem; text-align: center; border-radius: 20px; z-index: 2000; box-shadow: 0 50px 100px rgba(0,0,0,0.5); width: 90%; max-width: 450px; color: var(--txt); }}
    .close-popup {{ position: absolute; top: 15px; right: 20px; cursor: pointer; font-size: 2rem; }}

    {anim_css}
    
    @media (max-width: 768px) {{
        .hero {{ min-height: 65vh; }}
        .nav-links {{ position: fixed; top: 60px; left: -100%; width: 100%; height: 100vh; background: var(--bg); flex-direction: column; padding: 2rem; align-items: flex-start; transition: 0.3s; border-top: 1px solid rgba(0,0,0,0.1); }}
        .nav-links.active {{ left: 0; }}
        .mobile-menu {{ display: block; font-size: 1.5rem; }}
        .grid-3, .about-grid, .contact-grid {{ grid-template-columns: 1fr !important; gap: 2rem; }}
        h1 {{ font-size: 2.5rem; }}
        .detail-view {{ grid-template-columns: 1fr !important; }}
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
            const t = document.createElement('div');
            t.innerText = "Language Switched 🌐";
            t.style.cssText = "position:fixed; top:80px; right:20px; background:var(--s); color:white; padding:10px 20px; border-radius:8px; z-index:9999; box-shadow:0 10px 30px rgba(0,0,0,0.2);";
            document.body.appendChild(t);
            setTimeout(() => t.remove(), 2500);
        }} catch(e) {{ console.log("Lang Error", e); }}
    }}
    let cart = JSON.parse(localStorage.getItem('titanCart')) || [];
    function addToCart(name, price) {{
        cart.push({{name, price}});
        localStorage.setItem('titanCart', JSON.stringify(cart));
        alert(name + " added!");
        updateCartDisplay();
    }}
    function updateCartDisplay() {{
        const el = document.getElementById('cart-count');
        if(el) el.innerText = cart.length;
        if(cart.length > 0) document.getElementById('cart-float').style.display = 'flex';
    }}
    function checkout() {{
        let msg = "Order:%0A";
        cart.forEach(i => {{ msg += `- ${{i.name}} (${{i.price}})%0A`; }});
        window.open(`https://wa.me/{clean_wa}?text=${{msg}}`, '_blank');
        cart = []; localStorage.setItem('titanCart', '[]'); updateCartDisplay();
    }}
    setTimeout(() => {{
        if(!localStorage.getItem('popShown') && document.getElementById('lead-popup')) {{
            document.getElementById('lead-popup').style.display = 'block';
            localStorage.setItem('popShown', 'true');
        }}
    }}, {popup_delay * 1000});
    window.addEventListener('load', updateCartDisplay);
    </script>
    """

# --- PAGE GENERATOR HELPER ---
def build_page(title, content):
    pwa = f'<link rel="manifest" href="manifest.json"><meta name="theme-color" content="{p_color}"><link rel="apple-touch-icon" href="{pwa_icon}">'
    nav_top = "40px" if top_bar_enabled else "0px"
    
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title} | {biz_name}</title>{pwa}{gen_schema()}<link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ', '+')}:wght@400;700;900&family={b_font.replace(' ', '+')}:wght@300;400;600&display=swap" rel="stylesheet"><style>{get_theme_css()}</style></head><body style="padding-top:{nav_top}">{gen_nav()}{content}{gen_footer()}{gen_wa_widget()}<div id="cart-float" onclick="checkout()" style="position:fixed; bottom:100px; right:30px; background:var(--p); color:white; padding:15px; border-radius:50px; display:none; cursor:pointer; z-index:998; box-shadow:0 10px 30px rgba(0,0,0,0.2);">🛒 <span id="cart-count" style="margin-left:5px; font-weight:bold;">0</span></div><div id="theme-toggle" onclick="document.body.classList.toggle('dark-mode')">🌓</div>{gen_popup()}{gen_common_js()}</body></html>"""

# --- CONTENT GENERATORS (Defined here to prevent NameError) ---

def gen_blog_index_html():
    return f"""
    <section class="hero" style="min-height:40vh; background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('{hero_img_1}'); background-size: cover;">
        <div class="container"><h1 id="blog-title">{blog_hero_title}</h1><p id="blog-sub">{blog_hero_sub}</p></div>
    </section>
    <section><div class="container"><div id="blog-grid" class="grid-3">Loading...</div></div></section>
    {gen_csv_parser()}
    <script>
    async function init() {{
        try {{
            const res = await fetch('{blog_sheet_url}');
            const txt = await res.text();
            const lines = txt.split(/\\r\\n|\\n/).slice(1);
            const box = document.getElementById('blog-grid');
            box.innerHTML = '';
            for(let row of lines) {{
                if(!row.trim()) continue;
                const r = parseCSVLine(row);
                if(r.length > 4) {{
                    box.innerHTML += `
                    <div class="product-card reveal">
                        <div class="prod-img" style="background-image:url('${{r[5]}}'); background-size:cover;"></div>
                        <div class="card-content">
                            <span class="blog-badge">${{r[3]}}</span>
                            <h3 style="margin-top:0.5rem;"><a href="post.html?id=${{r[0]}}">${{r[1]}}</a></h3>
                            <p style="font-size:0.9rem;">${{r[4]}}</p>
                            <a href="post.html?id=${{r[0]}}" class="btn btn-primary" style="margin-top:auto; width:100%;">Read More</a>
                        </div>
                    </div>`;
                }}
            }}
        }} catch(e) {{}}
    }}
    init();
    </script>
    """

def gen_blog_post_html():
    return f"""
    <div id="blog-content" style="padding-top:80px;">Loading...</div>
    {gen_csv_parser()}
    <script>
    async function init() {{
        const id = new URLSearchParams(window.location.search).get('id');
        const res = await fetch('{blog_sheet_url}');
        const txt = await res.text();
        const lines = txt.split(/\\r\\n|\\n/).slice(1);
        const container = document.getElementById('blog-content');
        
        for(let row of lines) {{
            const col = parseCSVLine(row);
            if(col[0] === id) {{
                const url = encodeURIComponent(window.location.href);
                const title = encodeURIComponent(col[1]);
                const body = parseMarkdown(col[6]);
                
                container.innerHTML = `
                    <div style="background:var(--p); padding:clamp(3rem,8vw,6rem) 1rem; text-align:center; color:white;">
                        <div class="container">
                            <span class="blog-badge">${{col[3]}}</span>
                            <h1 style="margin-top:1rem; color:white!important;">${{col[1]}}</h1>
                            <p style="opacity:0.8;">${{col[2]}}</p>
                        </div>
                    </div>
                    <div class="container" style="max-width:800px; padding:3rem 1.5rem;">
                        <img src="${{col[5]}}" style="width:100%; border-radius:20px; margin-bottom:2rem; box-shadow:0 10px 40px rgba(0,0,0,0.1);">
                        <div style="font-size:1.1rem; line-height:1.8; color:var(--txt);">${{body}}</div>
                        
                        <div style="margin-top:3rem; padding-top:2rem; border-top:1px solid rgba(128,128,128,0.2);">
                            <h4 style="margin-bottom:1rem;">Share this post:</h4>
                            <div class="share-row">
                                <a href="https://www.facebook.com/sharer/sharer.php?u=${{url}}" target="_blank" class="share-btn bg-fb"><svg viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>
                                <a href="https://twitter.com/intent/tweet?text=${{title}}&url=${{url}}" target="_blank" class="share-btn bg-x"><svg viewBox="0 0 24 24"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584l-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/></svg></a>
                                <a href="https://www.linkedin.com/sharing/share-offsite/?url=${{url}}" target="_blank" class="share-btn bg-li"><svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2a2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zM4 2a2 2 0 1 1-2 2a2 2 0 0 1 2-2z"/></svg></a>
                                <a href="https://wa.me/?text=${{title}} ${{url}}" target="_blank" class="share-btn bg-wa"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg></a>
                                <button onclick="navigator.clipboard.writeText(window.location.href);alert('Copied')" class="share-btn bg-link">🔗</button>
                            </div>
                        </div>
                        <a href="blog.html" class="btn btn-primary" style="margin-top:2rem;">&larr; Back to Blog</a>
                    </div>
                `;
            }}
        }}
    }}
    init();
    </script>
    """

def gen_product_page_content(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""
    <section style="padding:150px 0;"><div class="container" id="prod-box">Loading...</div></section>
    <script>
    {demo_flag}
    function parseCSV(str) {{
        const arr = []; let quote = false; let c = '';
        for(let x of str) {{ if(x === '"') quote = !quote; else if(x === ',' && !quote) {{ arr.push(c); c = ''; }} else c += x; }}
        arr.push(c); return arr;
    }}
    function changeImg(src) {{ document.getElementById('main-img').src = src; }}
    
    async function init() {{
        const id = new URLSearchParams(window.location.search).get('item');
        let target = id; 
        if(isDemo && !id) target = "Demo Item";
        
        try {{
            const res = await fetch('{sheet_url}');
            const rows = (await res.text()).split(/\\r\\n|\\n/).slice(1);
            
            for(let row of rows) {{
                const col = parseCSV(row);
                if(isDemo) target = col[0];
                
                if(col[0] === target) {{
                    let images = col[3].split('|').map(s => s.trim());
                    let thumbHTML = '';
                    images.forEach(img => {{
                        thumbHTML += `<img src="${{img}}" style="width:70px; height:70px; object-fit:cover; border-radius:8px; cursor:pointer; border:2px solid transparent;" onclick="changeImg('${{img}}')">`;
                    }});
                    
                    let btn = col[4] ? `<a href="${{col[4]}}" class="btn btn-primary">Buy Now</a>` : `<button onclick="addToCart('${{col[0]}}','${{col[1]}}')" class="btn btn-primary">Add to Cart</button>`;
                    
                    document.getElementById('prod-box').innerHTML = `
                        <div class="detail-view">
                            <div>
                                <img id="main-img" src="${{images[0]}}" style="width:100%; border-radius:20px; margin-bottom:1rem; box-shadow:0 10px 40px rgba(0,0,0,0.1);">
                                <div style="display:flex; gap:10px;">${{thumbHTML}}</div>
                            </div>
                            <div>
                                <h1 style="line-height:1.1; margin-bottom:0.5rem;">${{col[0]}}</h1>
                                <p style="font-size:1.5rem; font-weight:900; color:var(--s);">${{col[1]}}</p>
                                <p style="opacity:0.9; margin-bottom:2rem;">${{col[2]}}</p>
                                ${{btn}}
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

def gen_booking_content():
    return f"""
    <section class="hero" style="min-height:40vh; background:var(--p);"><div class="container hero-content"><h1 id="book-title">{booking_title}</h1><p id="book-sub">{booking_desc}</p></div></section>
    <section><div class="container" style="text-align:center;"><div style="background:white; border-radius:20px; overflow:hidden; box-shadow:0 20px 50px rgba(0,0,0,0.1);">{booking_embed}</div></div></section>
    """

def get_simple_icon(name):
    name = name.lower().strip()
    path = "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"
    if "bolt" in name: path = "M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"
    if "wallet" in name: path = "M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"
    return f'<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="{path}"/></svg>'

# --- 6. LAUNCHPAD ---
c1, c2 = st.columns([3, 1])
with c2:
    if st.button("🚀 DOWNLOAD WEBSITE", type="primary"):
        z = io.BytesIO()
        with zipfile.ZipFile(z, "a", zipfile.ZIP_DEFLATED, False) as zf:
            # Home
            home_content = ""
            if show_hero: home_content += gen_hero()
            if show_stats: home_content += gen_stats()
            if show_features: home_content += gen_features()
            if show_pricing: home_content += gen_pricing_table()
            if show_inventory: home_content += gen_inventory()
            if show_gallery: home_content += gen_about_section()
            if show_faq: home_content += gen_faq_section()
            if show_cta: home_content += f'<section style="background:var(--s); text-align:center; color:white;"><div class="container reveal"><h2>Start Now</h2><a href="contact.html" class="btn" style="background:white; color:var(--s);">Contact</a></div></section>'
            
            zf.writestr("index.html", build_page("Home", home_content))
            zf.writestr("blog.html", build_page("Blog", gen_blog_index_html()))
            zf.writestr("post.html", build_page("Article", gen_blog_post_html()))
            zf.writestr("product.html", build_page("Product", gen_product_page_content(False)))
            
            contact_html = f"""{gen_inner_header("Contact Us")}<section><div class="container"><div class="contact-grid"><div><div class="card"><h3>Get In Touch</h3><p>{biz_addr}</p><p><a href="tel:{biz_phone}">{biz_phone}</a></p><p>{biz_email}</p></div></div><div class="card"><h3>Send Message</h3><form action="https://formsubmit.co/{biz_email}" method="POST"><label>Name</label><input type="text" name="name" required><label>Email</label><input type="email" name="email" required><label>Message</label><textarea name="msg" rows="4" required></textarea><button class="btn btn-primary" type="submit">Send</button></form></div></div><br><div style="border-radius:12px;overflow:hidden;">{map_iframe}</div></div></section>"""
            zf.writestr("contact.html", build_page("Contact", contact_html))
            zf.writestr("booking.html", build_page("Book", gen_booking_content()))
            
            zf.writestr("robots.txt", "User-agent: *\\nAllow: /")
            zf.writestr("manifest.json", gen_pwa_manifest())
            zf.writestr("service-worker.js", gen_sw())
            
        st.download_button("📥 Save Zip", z.getvalue(), "titan_site.zip", "application/zip")

# --- PREVIEW ---
if 'home_content' not in locals():
    home_content = ""
    if show_hero: home_content += gen_hero()
    if show_stats: home_content += gen_stats()
    if show_features: home_content += gen_features()
    if show_pricing: home_content += gen_pricing_table()
    if show_inventory: home_content += gen_inventory()
    if show_gallery: home_content += gen_about_section()
    if show_faq: home_content += gen_faq_section()
    if show_cta: home_content += f'<section style="background:var(--s); text-align:center; color:white;"><div class="container reveal"><h2>Start Now</h2><a href="contact.html" class="btn" style="background:white; color:var(--s);">Contact</a></div></section>'

with c1:
    prev = st.radio("Preview", ["Home", "Product", "Blog Index", "Blog Post", "Booking"], horizontal=True)
    if prev == "Home": st.components.v1.html(build_page("Home", home_content), height=600, scrolling=True)
    if prev == "Product": st.components.v1.html(build_page("Prod", gen_product_page_content(True)), height=600, scrolling=True)
    if prev == "Blog Index": st.components.v1.html(build_page("Blog", gen_blog_index_html()), height=600, scrolling=True)
    if prev == "Blog Post": st.components.v1.html(build_page("Post", gen_blog_post_html()), height=600, scrolling=True)
    if prev == "Booking": st.components.v1.html(build_page("Book", gen_booking_content()), height=600, scrolling=True)
