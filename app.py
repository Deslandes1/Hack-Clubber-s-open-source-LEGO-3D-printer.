import streamlit as st

st.set_page_config(
    page_title="The Future of Innovation | Studprint Story",
    page_icon="🧱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- LOGIN STATE ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ---------- CUSTOM CSS (dark theme with spinning globe, animations) ----------
st.markdown(r"""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0b1120, #1a2332);
    }
    /* Spinning globe animation */
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    .spinning-globe {
        display: inline-block;
        animation: spin 4s linear infinite;
        font-size: 3rem;
    }
    /* Powerful symbol (LEGO + 3D printer combo) */
    .power-symbol {
        font-size: 3rem;
        text-align: center;
        animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }
    /* Story text */
    .story-text {
        font-family: 'Georgia', serif;
        font-size: 1.2rem;
        line-height: 1.6;
        color: #e0e0e0;
        background: rgba(0,0,0,0.4);
        padding: 1.5rem;
        border-radius: 20px;
        border-left: 5px solid #ff6b6b;
    }
    /* Headings */
    h1, h2, h3 {
        color: #ffaa66 !important;
    }
    .stMarkdown, .stSidebar .stMarkdown {
        color: #ffffff !important;
    }
    /* Buttons */
    .stButton button {
        background-color: #ff6b6b !important;
        color: white !important;
        border-radius: 30px !important;
        font-weight: bold !important;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: #0a0f1a;
        border-right: 1px solid #2a3a4a;
    }
    .sidebar-brand {
        text-align: center;
        margin-bottom: 2rem;
    }
    .pricing-card {
        background: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        border: 1px solid #ffaa66;
    }
</style>
""", unsafe_allow_html=True)

# ---------- LOGIN PAGE ----------
def login_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="power-symbol">🧱🖨️🔥</div>', unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>Studprint Story</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>The future of innovation starts here.</p>", unsafe_allow_html=True)
        st.markdown("---")
        password = st.text_input("Enter Access Password", type="password", key="login_pass")
        if st.button("Enter the Workshop"):
            if password == "20082010":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password. Try again.")

# ---------- MAIN APP (after login) ----------
def main_app():
    # ----- SIDEBAR (spinning globe + contact + pricing) -----
    with st.sidebar:
        st.markdown('<div style="text-align: center;"><span class="spinning-globe">🌍</span></div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("### **GlobalInternet.py**")
        st.markdown("**Built by Gesner Deslandes**")
        st.markdown("📧 deslandes78@gmail.com")
        st.markdown("📞 (509)-47385663")
        st.markdown("---")
        st.markdown("### 💰 Competitive Pricing")
        st.markdown("""
        <div class="pricing-card">
        <strong>Innovation Starter</strong><br>
        $49 USD – Full app source code + one hour consultation
        </div>
        <div class="pricing-card">
        <strong>Pro Builder</strong><br>
        $199 USD – Custom storytelling platform + deployment support
        </div>
        <div class="pricing-card">
        <strong>Enterprise (annual)</strong><br>
        $999 USD – Unlimited projects, priority support, white‑label rights
        </div>
        *All plans include the Studprint story showcase, spinning globe, and full customization.
        """, unsafe_allow_html=True)
        st.markdown("---")
        st.caption("© 2026 GlobalInternet.py – Open Innovation")

    # ----- MAIN CONTENT (the story) -----
    # Powerful symbol at top
    st.markdown('<div class="power-symbol" style="display: flex; justify-content: center; gap: 20px;">🧱 🖨️ ⚡🔧</div>', unsafe_allow_html=True)
    st.title("Not every breakthrough starts in a lab.")
    st.markdown("### Some start with curiosity, creativity—and a box of bricks.")

    st.markdown("""
    <div class="story-text">
    An 18-year-old Hack Clubber just built an open-source 3D printer made from <strong>92% LEGO</strong> that actually works.  
    Meet <strong>Studprint</strong> — designed and rendered on a PC powered by AMD Ryzen 5 7600X from AMD.

    <br><br>

    Let that sink in.  
    This isn’t just a cool project.  
    It’s a signal of where innovation is heading:

    - Barriers to entry are collapsing  
    - Open-source is accelerating experimentation  
    - Hardware + creativity is becoming accessible to anyone, anywhere  

    <br>

    And maybe most important:  
    <strong>The next generation isn’t waiting for permission to build.</strong>  
    They’re already doing it.  

    When talent meets the right tools, age becomes irrelevant.  
    What matters is mindset, access, and the willingness to create.

    <br>

    We’re moving into a world where innovation doesn’t come top‑down.  
    It emerges from everywhere.  

    <br>

    🔥 The question is no longer <em>who will build the future?</em>  
    It’s <strong>how fast can we keep up with them?</strong>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🚀 Ready to build your own breakthrough?")
    st.markdown("Contact us for a free 15‑min consultation or explore the pricing plans on the sidebar.")

    # Logout button
    if st.button("Logout", key="logout_btn"):
        st.session_state.authenticated = False
        st.rerun()

# ---------- ROUTING ----------
if not st.session_state.authenticated:
    login_page()
else:
    main_app()
