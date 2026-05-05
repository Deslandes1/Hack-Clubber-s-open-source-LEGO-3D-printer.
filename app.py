import streamlit as st
import streamlit.components.v1 as components

# Direct video URL
VIDEO_URL = "https://raw.githubusercontent.com/Deslandes1/Hack-Clubber-s-open-source-LEGO-3D-printer./main/Demo1.mp4"

st.set_page_config(
    page_title="The Future of Innovation | Studprint Story",
    page_icon="🧱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- LOGIN STATE ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "demo_mode" not in st.session_state:
    st.session_state.demo_mode = False

# ---------- CUSTOM CSS ----------
st.markdown(r"""
<style>
    .stApp { background: linear-gradient(135deg, #0b1120, #1a2332); }
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    .spinning-globe { display: inline-block; animation: spin 4s linear infinite; font-size: 3rem; }
    .power-symbol { font-size: 3rem; text-align: center; animation: pulse 1.5s infinite; }
    @keyframes pulse { 0% { transform: scale(1); opacity: 0.8; } 50% { transform: scale(1.1); opacity: 1; } 100% { transform: scale(1); opacity: 0.8; } }
    .story-text { font-family: 'Georgia', serif; font-size: 1.2rem; line-height: 1.6; color: #e0e0e0; background: rgba(0,0,0,0.4); padding: 1.5rem; border-radius: 20px; border-left: 5px solid #ff6b6b; }
    h1, h2, h3 { color: #ffaa66 !important; }
    .stMarkdown, .stSidebar .stMarkdown { color: #ffffff !important; }
    .stButton button { background-color: #ff6b6b !important; color: white !important; border-radius: 30px !important; font-weight: bold !important; }
    [data-testid="stSidebar"] { background: #0a0f1a; border-right: 1px solid #2a3a4a; }
    .pricing-card { background: rgba(255,255,255,0.05); border-radius: 15px; padding: 1rem; margin: 1rem 0; border: 1px solid #ffaa66; }
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

# ---------- MAIN APP ----------
def main_app():
    # ----- SIDEBAR -----
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

        # ---- DEMO MODE TOGGLE ----
        st.markdown("### 🧪 Demo Mode")
        demo_mode = st.checkbox("Show Demo Video & 3D Model", value=st.session_state.demo_mode)
        if demo_mode != st.session_state.demo_mode:
            st.session_state.demo_mode = demo_mode
            st.rerun()

    # ----- MAIN CONTENT (story) -----
    st.markdown('<div class="power-symbol" style="display: flex; justify-content: center; gap: 20px;">🧱 🖨️ ⚡🔧</div>', unsafe_allow_html=True)
    st.title("Not every breakthrough starts in a lab.")
    st.markdown("### Some start with curiosity, creativity—and a box of bricks.")

    st.markdown("""
    <div class="story-text">
    An 18-year-old Hack Clubber just built an open-source 3D printer made from <strong>92% LEGO</strong> that actually works.  
    Meet <strong>Studprint</strong> — designed and rendered on a PC powered by AMD Ryzen 5 7600X.

    <br><br>

    Let that sink in.  
    This isn't just a cool project.  
    It's a signal of where innovation is heading:

    - Barriers to entry are collapsing  
    - Open-source is accelerating experimentation  
    - Hardware + creativity is becoming accessible to anyone, anywhere  

    <br>

    And maybe most important:  
    <strong>The next generation isn't waiting for permission to build.</strong>  
    They're already doing it.  

    When talent meets the right tools, age becomes irrelevant.  
    What matters is mindset, access, and the willingness to create.

    <br>

    We're moving into a world where innovation doesn't come top‑down.  
    It emerges from everywhere.  

    <br>

    🔥 The question is no longer <em>who will build the future?</em>  
    It's <strong>how fast can we keep up with them?</strong>
    </div>
    """, unsafe_allow_html=True)

    # ----- DEMO SECTION -----
    if st.session_state.demo_mode:
        st.markdown("---")
        st.markdown("## 🎬 Demo: Studprint in Action")
        
        # Video embed
        try:
            st.video(VIDEO_URL)
        except Exception as e:
            st.error(f"Could not load video: {e}")
            st.markdown(f"[Watch the demo video here]({VIDEO_URL})")
        
        # 3D Model
        st.markdown("### 🧱 Interactive 3D LEGO Model")
        st.markdown("_(Rotate and zoom to explore)_")
        
        lego_3d_html = """
        <div id="lego-viewer" style="height: 400px; width: 100%; border-radius: 20px; overflow: hidden;"></div>
        <script type="importmap">
            {
                "imports": {
                    "three": "https://unpkg.com/three@0.128.0/build/three.module.js",
                    "three/addons/": "https://unpkg.com/three@0.128.0/examples/jsm/"
                }
            }
        </script>
        <script type="module">
            import * as THREE from 'three';
            import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

            const container = document.getElementById('lego-viewer');
            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x111122);
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
            camera.position.set(2, 2, 3);
            camera.lookAt(0, 0, 0);
            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);
            const controls = new OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;

            // LEGO brick group
            const group = new THREE.Group();
            const redMat = new THREE.MeshStandardMaterial({ color: 0xcc0000 });
            const base = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.4, 0.8), redMat);
            base.position.y = 0;
            group.add(base);
            const studMat = new THREE.MeshStandardMaterial({ color: 0xcc0000 });
            for (let x = -0.6; x <= 0.6; x+=0.6) {
                for (let z = -0.3; z <= 0.3; z+=0.3) {
                    const stud = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 0.1, 16), studMat);
                    stud.position.set(x, 0.25, z);
                    group.add(stud);
                }
            }
            scene.add(group);

            const light = new THREE.DirectionalLight(0xffffff, 1);
            light.position.set(1, 2, 1);
            scene.add(light);
            const ambient = new THREE.AmbientLight(0x404060);
            scene.add(ambient);
            const grid = new THREE.GridHelper(5, 10, 0x88aaff, 0x335588);
            scene.add(grid);

            function animate() {
                requestAnimationFrame(animate);
                controls.update();
                renderer.render(scene, camera);
            }
            animate();

            window.addEventListener('resize', () => {
                const w = container.clientWidth;
                const h = container.clientHeight;
                renderer.setSize(w, h);
                camera.aspect = w / h;
                camera.updateProjectionMatrix();
            });
        </script>
        """
        components.html(lego_3d_html, height=400)

    st.markdown("---")
    st.markdown("### 🚀 Ready to build your own breakthrough?")
    st.markdown("Contact us for a free 15‑min consultation or explore the pricing plans on the sidebar.")

    if st.button("Logout", key="logout_btn"):
        st.session_state.authenticated = False
        st.session_state.demo_mode = False
        st.rerun()

# ---------- ROUTING ----------
if not st.session_state.authenticated:
    login_page()
else:
    main_app()
