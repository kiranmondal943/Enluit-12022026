import streamlit as st
import zipfile
import io
import json
import datetime
import re
import requests

# --- 0. STATE MANAGEMENT (AI INTEGRATION) ---
def init_state(key, default_val):
    if key not in st.session_state:
        st.session_state[key] = default_val

init_state('hero_h', "Stop Paying Rent for Your Website.")
init_state('hero_sub', "The Titan Engine is the world’s first 0.1s website architecture that runs on $0 monthly fees. Pay once. Own it forever.")
init_state('about_h', "Control Your Empire")
init_state('about_short', "No WordPress dashboard. No plugins to update. Just open your private Google Sheet, change a text, and watch your site update globally in seconds.")
init_state('feat_data', "bolt | The Performance Pillar | **0.1s High-Velocity Loading**. While traditional sites take 3–5s, Titan loads instantly.\nwallet | The Economic Pillar | **$0 Monthly Fees**. We eliminated hosting subscriptions. You pay once and own the raw source code forever.\ntable | The Functional Pillar | **Google Sheets CMS**. Update prices and photos directly from a simple spreadsheet. If you can use Excel, you can manage your site.\nshield | The Authority Pillar | **Unhackable Security**. By removing the database (Zero-DB Architecture), we removed the hacker's primary entry point.\nlayers | The Reliability Pillar | **Global Edge Deployment**. Your site is distributed across 100+ servers worldwide (CDN), creating 99.9% uptime.\nstar | The Conversion Pillar | **One-Tap WhatsApp**. We embed 'Direct-to-Chat' technology. Customers tap one button to start a conversation.")

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Titan v40.1 | Final Stable", 
    layout="wide", 
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED UI SYSTEM (CSS) ---
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
    .stButton>button:hover { transform: translateY(-2px); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: THE CONTROL CENTER ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v40.1 | Fixed Inventory Logic")
    st.divider()
    
    # TITAN AI
    with st.expander("🤖 Titan AI Generator", expanded=False):
        groq_key = st.text_input("Groq API Key", type="password")
        biz_desc = st.text_input("Business Description")
        if st.button("✨ Generate Copy"):
            if not groq_key or not biz_desc:
                st.error("Key & Description required.")
            else:
                try:
                    url = "https://api.groq.com/openai/v1/chat/completions"
                    headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
                    prompt = f"Act as a copywriter. Return JSON for '{biz_desc}': hero_h, hero_sub, about_h, about_short, feat_data (icon|Title|Desc format)."
                    data = {"messages": [{"role": "user", "content": prompt}], "model": "llama3-8b-8192", "response_format": {"type": "json_object"}}
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
        theme_mode = st.selectbox("Base Theme", ["Clean Corporate", "Midnight SaaS", "Glassmorphism", "Cyberpunk Neon", "Luxury Gold", "Stark Minimalist"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#0F172A") 
        s_color = c2.color_picker("Action (CTA)", "#EF4444")  
        h_font = st.selectbox("Headings", ["Montserrat", "Space Grotesk", "Playfair Display", "Oswald"])
        b_font = st.selectbox("Body Text", ["Inter", "Open Sans", "Roboto", "Lora"])
        border_rad = st.select_slider("Corner Roundness", ["0px", "8px", "16px", "24px", "50px"], value="8px")
        anim_type = st.selectbox("Animation", ["Fade Up", "Zoom In", "None"])

    # MODULES
    with st.expander("🧩 Modules", expanded=False):
        show_hero = st.checkbox("Hero", True)
        show_stats = st.checkbox("Stats", True)
        show_features = st.checkbox("Features", True)
        show_pricing = st.checkbox("Pricing", True)
        show_inventory = st.checkbox("Store/Portfolio", True)
        show_blog = st.checkbox("Blog", True)
        show_gallery = st.checkbox("About", True)
        show_testimonials = st.checkbox("Testimonials", True)
        show_faq = st.checkbox("FAQ", True)
        show_cta = st.checkbox("CTA", True)
        show_booking = st.checkbox("Booking", True)

    # SEO
    with st.expander("⚙️ SEO & Analytics", expanded=False):
        seo_area = st.text_input("Service Area", "Global")
        seo_kw = st.text_input("SEO Keywords", "no monthly fee website, one time payment web design")
        gsc_tag = st.text_input("Google Verification ID")
        ga_tag = st.text_input("Google Analytics ID")
        og_image = st.text_input("Social Share Image URL")

# --- 4. INPUT TABS ---
st.title("🏗️ StopWebRent Site Builder v40.1")
tabs = st.tabs(["1. Identity", "2. Content", "3. Pricing", "4. Store", "5. Booking", "6. Blog", "7. Legal"])

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
        seo_d = st.text_area("Meta Desc", "Stop paying monthly fees for Wix or Shopify. The Titan Engine builds ultra-fast 0.1s websites.", height=100)
        logo_url = st.text_input("Logo URL (PNG/SVG)")

    st.subheader("📱 PWA & Social")
    pwa_short = st.text_input("App Name", biz_name[:12])
    pwa_icon = st.text_input("App Icon (512px)", logo_url)
    lang_sheet = st.text_input("Translation CSV URL")
    
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
    about_short_in = st.text_area("Short Summary", st.session_state.about_short, height=100)
    about_long = st.text_area("Full Content", "The Digital Landlord Trap...", height=200)

with tabs[2]:
    st.subheader("💰 Pricing")
    c1, c2, c3 = st.columns(3)
    titan_price = c1.text_input("Our Price", "$199")
    titan_mo = c1.text_input("Our Monthly", "$0")
    wix_name = c2.text_input("Comp. Name", "Wix")
    wix_mo = c2.text_input("Comp. Monthly", "$29/mo")
    save_val = c3.text_input("Total Savings", "$1,466")

with tabs[3]:
    st.subheader("🛒 Store Config")
    st.info("CSV Columns: Name, Price, Description, ImageURLs (use | to split), StripeLink")
    sheet_url = st.text_input("Store CSV", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Default Product Img", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800")
    c1, c2 = st.columns(2)
    paypal_link = c1.text_input("PayPal Link")
    upi_id = c2.text_input("UPI ID")

with tabs[4]:
    st.subheader("📅 Booking")
    booking_embed = st.text_area("Calendly Embed", height=100)
    booking_title = st.text_input("Book Title", "Book an Appointment")
    booking_desc = st.text_input("Book Subtext", "Select a slot.")

with tabs[5]:
    st.subheader("📰 Blog")
    blog_sheet_url = st.text_input("Blog CSV")
    blog_hero_title = st.text_input("Blog Title", "Insights")
    blog_hero_sub = st.text_input("Blog Subtext", "News & Updates")

with tabs[6]:
    st.subheader("Legal")
    testi_data = st.text_area("Testimonials", "Name | Quote", height=100)
    faq_data = st.text_area("FAQ", "Q? ? A", height=100)
    priv_txt = st.text_area("Privacy Policy", "Text...", height=100)
    term_txt = st.text_area("Terms", "Text...", height=100)

# --- 5. COMPILER FUNCTIONS (ORDER MATTERS) ---

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

# --- HELPER: CSV PARSER JS ---
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
    bg, txt, card, nav = "#ffffff", "#0f172a", "rgba(255,255,255,0.8)", "rgba(255,255,255,0.9)"
    if "Midnight" in theme_mode: bg, txt, card, nav = "#0f172a", "#f8fafc", "rgba(30,41,59,0.9)", "rgba(15,23,42,0.9)"
    if "Cyberpunk" in theme_mode: bg, txt, card, nav = "#050505", "#00ff9d", "rgba(10,10,10,0.9)", "rgba(0,0,0,0.9)"
    if "Luxury" in theme_mode: bg, txt, card, nav = "#101010", "#D4AF37", "rgba(20,20,20,0.9)", "rgba(0,0,0,0.9)"
    
    hero_align = "center"
    anim_css = ".reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s ease; } .reveal.active { opacity: 1; transform: translateY(0); }"
    if anim_type == "None": anim_css = ""

    return f"""
    :root {{ --p: {p_color}; --s: {s_color}; --bg: {bg}; --txt: {text_color}; --card: {card}; --nav: {nav}; --radius: {border_rad}; }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; font-size: 16px; }}
    body {{ background-color: var(--bg); color: var(--txt); font-family: var(--b-font); margin: 0; line-height: 1.6; overflow-x: hidden; }}
    h1, h2, h3 {{ font-family: var(--h-font); color: var(--txt); font-weight: 800; line-height: 1.2; margin-bottom: 0.5rem; }}
    h1 {{ font-size: clamp(2.5rem, 6vw, 5rem); }}
    
    .container {{ max-width: 1280px; margin: 0 auto; padding: 0 24px; }}
    .btn {{ display: inline-flex; align-items: center; justify-content: center; padding: 0.8rem 2rem; border-radius: {border_rad}; font-weight: 700; text-transform: uppercase; cursor: pointer; border: none; text-decoration: none; color: white; transition: 0.3s; min-height: 3rem; }}
    .btn-primary {{ background: var(--p); }} .btn-accent {{ background: var(--s); }}
    .btn:hover {{ transform: translateY(-3px); filter: brightness(1.1); }}
    
    nav {{ position: fixed; top: 0; width: 100%; z-index: 1000; padding: 1rem 0; background: var(--nav); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(128,128,128,0.1); }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links a {{ margin-left: 2rem; text-decoration: none; font-weight: 600; color: var(--txt); opacity: 0.8; transition:0.2s; }}
    .mobile-menu {{ display: none; font-size: 1.5rem; cursor: pointer; }}
    
    .hero {{ min-height: 90vh; display: flex; align-items: center; justify-content: center; position: relative; background: var(--p); padding-top: 80px; }}
    .hero-content {{ z-index: 2; width: 100%; text-align: center; }}
    .hero h1 {{ color: white !important; text-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
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
    
    /* Pricing Table */
    .pricing-wrapper {{ overflow-x: auto; margin: 2rem 0; }}
    .pricing-table {{ width: 100%; border-collapse: collapse; min-width: 600px; }}
    .pricing-table th {{ background: var(--p); color: white; padding: 1.5rem; }}
    .pricing-table td {{ padding: 1.5rem; border-bottom: 1px solid rgba(128,128,128,0.1); }}
    
    /* Blog */
    .blog-badge {{ background: var(--s); color: white; padding: 0.3rem 0.8rem; border-radius: 50px; font-size: 0.75rem; font-weight: bold; margin-bottom: 1rem; display:inline-block; }}
    .share-row {{ display: flex; gap: 10px; margin-top: 20px; flex-wrap: wrap; }}
    .share-btn {{ width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border-radius: 50%; background: #eee; }}
    .bg-wa {{ background: #25D366; fill: white; }}
    .bg-fb {{ background: #1877F2; fill: white; }}
    .bg-x {{ background: #000000; fill: white; }}
    .bg-li {{ background: #0A66C2; fill: white; }}
    
    /* Cart */
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
            <h1 id="hero-title">{hero_h}</h1>
            <p id="hero-sub">{hero_sub}</p>
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
        <div class="section-head reveal"><h2>The Cost of Ownership</h2><p>See how the "Monthly Trap" adds up over 5 years.</p></div>
        <div class="pricing-wrapper reveal">
            <table class="pricing-table">
                <thead><tr><th>Expense</th><th style="background:var(--s);">Titan Engine</th><th>{wix_name}</th></tr></thead>
                <tbody>
                    <tr><td>Setup Fee</td><td><strong>{titan_price}</strong></td><td>$0</td></tr>
                    <tr><td>Annual Costs</td><td><strong>{titan_mo}</strong></td><td>{wix_mo}</td></tr>
                    <tr><td><strong>5-Year Savings</strong></td><td style="color:var(--s); font-size:1.3rem;">You Save {save_val}</td><td>$0</td></tr>
                </tbody>
            </table>
        </div>
    </div></section>
    """

# --- INVENTORY GENERATOR (Corrected) ---
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
        <div class="section-head reveal"><h2>Portfolio & Store</h2><p>Secure Checkout available.</p></div>
        <div id="inv-grid" class="grid-3"><div style="text-align:center; padding:4rem;">Loading Store...</div></div>
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
                <a href="about.html" class="btn btn-primary">Read Full Story</a>
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
    icons = ""
    if fb_link: icons += f'<a href="{fb_link}" target="_blank"><svg class="social-icon" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>'
    if x_link: icons += f'<a href="{x_link}" target="_blank"><svg class="social-icon" viewBox="0 0 24 24"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584l-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"></path></svg></a>'
    
    return f"""
    <footer><div class="container">
        <div class="footer-grid">
            <div><h3>{biz_name}</h3><p>{biz_addr}</p><div style="display:flex;gap:1rem;margin-top:1rem;">{icons}</div></div>
            <div><h4>Links</h4><a href="index.html">Home</a><a href="blog.html">Blog</a><a href="booking.html">Book</a></div>
            <div><h4>Legal</h4><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a></div>
        </div>
        <div style="margin-top:3rem; padding-top:2rem; border-top:1px solid rgba(255,255,255,0.1); text-align:center; font-size:0.8rem; opacity:0.6;">&copy; {biz_name}. Powered by Titan Engine.</div>
    </div></footer>
    """

def gen_wa_widget():
    if not wa_num: return ""
    return f"""<a href="https://wa.me/{wa_num}" class="wa-float" target="_blank" style="position:fixed; bottom:30px; right:30px; background:#25d366; color:white; width:60px; height:60px; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 10px 30px rgba(37,211,102,0.4); z-index:9999;"><svg style="width:32px;height:32px" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.1-.8-.3-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.1-.45-1.08-.62-1.48c-.16-.4-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z"/></path></svg></a>"""

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

def gen_inner_header(title):
    return f"""<section class="hero" style="min-height: 40vh; background:var(--p);"><div class="container"><h1>{title}</h1></div></section>"""

# --- 6. PAGE ASSEMBLY ---
def build_page(title, content, extra_js=""):
    css = get_theme_css()
    meta = f'<link rel="manifest" href="manifest.json"><meta name="theme-color" content="{p_color}">'
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title} | {biz_name}</title>{meta}{gen_schema()}<link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ','+')}:wght@400;700;900&family={b_font.replace(' ','+')}:wght@300;400;600&display=swap" rel="stylesheet"><style>{css}</style></head><body>{gen_nav()}{content}{gen_footer()}{gen_wa_widget()}{gen_cart_system()}{gen_common_js()}{gen_sw()}{extra_js}</body></html>"""

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

# --- 7. DEPLOYMENT ---
c1, c2 = st.columns([3, 1])
with c1:
    st.info("Preview: Home Page")
    st.components.v1.html(build_page("Home", home_content), height=600, scrolling=True)

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
