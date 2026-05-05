import streamlit as st
import streamlit.components.v1 as components

VIDEO_URL = "https://raw.githubusercontent.com/Deslandes1/Hack-Clubber-s-open-source-LEGO-3D-printer./main/Demo1.mp4"

st.set_page_config(
    page_title="Studprint Story | Open‑Source LEGO 3D Printer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- LOGIN STATE ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "demo_mode" not in st.session_state:
    st.session_state.demo_mode = False

# ---------- STYLING (compact, scrollable story, reduced margins) ----------
st.markdown(r"""
<style>
    .stApp { background: linear-gradient(135deg, #0b1120, #1a2332); }
    /* Reduce top padding of main container */
    .main .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
    }
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    .spinning-globe { display: inline-block; animation: spin 4s linear infinite; font-size: 3rem; }
    .power-symbol { font-size: 2.5rem; text-align: center; animation: pulse 1.5s infinite; margin-bottom: 0.5rem; }
    @keyframes pulse { 0% { transform: scale(1); opacity: 0.8; } 50% { transform: scale(1.1); opacity: 1; } 100% { transform: scale(1); opacity: 0.8; } }
    /* Scrollable story text */
    .story-text {
        font-family: 'Georgia', serif;
        font-size: 1rem;
        line-height: 1.5;
        color: #e0e0e0;
        background: rgba(0,0,0,0.4);
        padding: 0.8rem;
        border-radius: 15px;
        border-left: 4px solid #ff6b6b;
        max-height: 200px;
        overflow-y: auto;
        margin-bottom: 0.5rem;
    }
    /* Smaller headings */
    h1, h2, h3 { color: #ffaa66 !important; margin-top: 0 !important; margin-bottom: 0.2rem !important; }
    h1 { font-size: 2rem !important; }
    h2 { font-size: 1.3rem !important; }
    .stMarkdown, .stSidebar .stMarkdown { color: #fff !important; }
    .stButton button { background-color: #ff6b6b !important; color: white !important; border-radius: 30px !important; font-weight: bold !important; padding: 0.2rem 1rem !important; }
    [data-testid="stSidebar"] { background: #0a0f1a; border-right: 1px solid #2a3a4a; }
    .pricing-card, .real-software-card { background: rgba(255,255,255,0.05); border-radius: 15px; padding: 0.6rem; margin: 0.5rem 0; border: 1px solid #ffaa66; font-size: 0.9rem; }
    .real-software-card a { color: #ffaa66; text-decoration: none; font-weight: bold; }
    /* Video container compact */
    .stVideo { margin: 0.5rem 0; }
    /* Hide Streamlit footer bar (optional) */
    footer { display: none; }
</style>
""", unsafe_allow_html=True)

# ---------- LOGIN PAGE ----------
def login_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="power-symbol">🧠🖨️⚡</div>', unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>Studprint</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>The open‑source LEGO 3D printer</p>", unsafe_allow_html=True)
        st.markdown("---")
        password = st.text_input("Enter Access Password", type="password", key="login_pass")
        if st.button("Enter the Workshop"):
            if password == "20082010":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password.")

# ---------- MAIN APP (compact layout, no scroll) ----------
def main_app():
    # ========== SIDEBAR ==========
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
        
        # ---------- REAL SOFTWARE ACCESS ----------
        st.markdown("### 🔧 Real Software Access")
        st.markdown("""
        <div class="real-software-card">
        ✅ **Studprint open‑source project**<br>
        Get the complete 3D printer design, firmware, and build instructions.<br><br>
        <a href="https://github.com/Deslandes1/Hack-Clubber-s-open-source-LEGO-3D-printer." target="_blank">
        📦 Download from GitHub →
        </a>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("*Use the hardware, contribute, and build your own.*")
        
        st.markdown("---")
        st.caption("© 2026 GlobalInternet.py – Open Innovation")
        
        # ---- DEMO MODE TOGGLE ----
        st.markdown("### 🧪 Demo Mode")
        demo_mode = st.checkbox("Show Demo Video & 3D Chip", value=st.session_state.demo_mode)
        if demo_mode != st.session_state.demo_mode:
            st.session_state.demo_mode = demo_mode
            st.rerun()
        
        # ---- Logout button moved here ----
        if st.button("Logout", key="logout_btn"):
            st.session_state.authenticated = False
            st.session_state.demo_mode = False
            st.rerun()

    # ========== MAIN CONTENT (compact) ==========
    st.markdown('<div class="power-symbol" style="display: flex; justify-content: center; gap: 20px;">🧠 🖨️ ⚡ 🔧</div>', unsafe_allow_html=True)
    st.title("Not every breakthrough starts in a lab.")
    st.markdown("### Some start with curiosity, creativity—and a box of bricks.")

    # Scrollable story text
    st.markdown("""
    <div class="story-text">
    An 18-year-old Hack Clubber built an open-source 3D printer made from <strong>92% LEGO</strong> that actually works.  
    Meet <strong>Studprint</strong> — designed and rendered on a PC powered by AMD Ryzen 5 7600X.

    <br><br>

    This isn’t just a cool project.  
    It’s a signal of where innovation is heading:

    - Barriers to entry are collapsing  
    - Open-source is accelerating experimentation  
    - Hardware + creativity is accessible to anyone, anywhere  

    <br>

    The next generation isn’t waiting for permission to build.  
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

    # ========== DEMO SECTION ==========
    if st.session_state.demo_mode:
        st.markdown("## 🎬 Demo: Studprint in Action")
        # Video (compact)
        try:
            st.video(VIDEO_URL)
        except Exception:
            st.markdown(f"[Watch the demo video here]({VIDEO_URL})")
        
        # Realistic 3D chip (compact height)
        st.markdown("### 🧠 The Brain of Studprint – Interactive 3D Chip")
        chip_3d_html = """
        <div id="chip-viewer" style="height: 360px; width: 100%; border-radius: 20px; overflow: hidden;"></div>
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
            import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';

            const container = document.getElementById('chip-viewer');
            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x0a0f1a);
            
            const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
            camera.position.set(3, 2, 4);
            camera.lookAt(0, 0, 0);
            
            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(container.clientWidth, container.clientHeight);
            renderer.shadowMap.enabled = true;
            container.appendChild(renderer.domElement);
            
            const labelRenderer = new CSS2DRenderer();
            labelRenderer.setSize(container.clientWidth, container.clientHeight);
            labelRenderer.domElement.style.position = 'absolute';
            labelRenderer.domElement.style.top = '0px';
            labelRenderer.domElement.style.left = '0px';
            labelRenderer.domElement.style.pointerEvents = 'none';
            container.appendChild(labelRenderer.domElement);
            
            const controls = new OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.autoRotate = true;
            controls.autoRotateSpeed = 1.0;
            
            // Chip body
            const bodyMat = new THREE.MeshStandardMaterial({ color: 0x2a2a2a, roughness: 0.3, metalness: 0.1 });
            const chipBase = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.3, 2.0), bodyMat);
            chipBase.castShadow = true;
            scene.add(chipBase);
            
            const topMat = new THREE.MeshStandardMaterial({ color: 0x333333, roughness: 0.2, metalness: 0.4 });
            const chipTop = new THREE.Mesh(new THREE.BoxGeometry(1.8, 0.05, 1.8), topMat);
            chipTop.position.y = 0.18;
            scene.add(chipTop);
            
            // Pins
            const pinMat = new THREE.MeshStandardMaterial({ color: 0xccaa33, metalness: 0.9 });
            const pinPositions = [
                [[-1.05,0,-0.7],[-1.05,0,-0.3],[-1.05,0,0.1],[-1.05,0,0.5],[-1.05,0,0.9]],
                [[ 1.05,0,-0.7],[ 1.05,0,-0.3],[ 1.05,0,0.1],[ 1.05,0,0.5],[ 1.05,0,0.9]],
                [[-0.7,0,-1.05],[-0.3,0,-1.05],[0.1,0,-1.05],[0.5,0,-1.05],[0.9,0,-1.05]],
                [[-0.7,0, 1.05],[-0.3,0, 1.05],[0.1,0, 1.05],[0.5,0, 1.05],[0.9,0, 1.05]]
            ];
            pinPositions.forEach(side => {
                side.forEach(pos => {
                    const pin = new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.08, 0.4), pinMat);
                    pin.position.set(pos[0], pos[1]-0.12, pos[2]);
                    pin.castShadow = true;
                    scene.add(pin);
                });
            });
            
            function makeLabel(text, x, y, z, size='14px') {
                const div = document.createElement('div');
                div.textContent = text;
                div.style.color = '#ffaa66';
                div.style.fontSize = size;
                div.style.fontWeight = 'bold';
                div.style.fontFamily = 'monospace';
                div.style.background = 'rgba(0,0,0,0.6)';
                div.style.padding = '2px 6px';
                div.style.borderRadius = '8px';
                div.style.border = '1px solid #ffaa66';
                const label = new CSS2DObject(div);
                label.position.set(x, y, z);
                scene.add(label);
            }
            makeLabel('Studprint', 0, 0.35, 0, '16px');
            makeLabel('ARM Cortex-M4', 0, -0.15, 1.2, '12px');
            
            const ambientLight = new THREE.AmbientLight(0x404060);
            scene.add(ambientLight);
            const mainLight = new THREE.DirectionalLight(0xffffff, 1.2);
            mainLight.position.set(2, 3, 4);
            mainLight.castShadow = true;
            scene.add(mainLight);
            
            const groundPlane = new THREE.Mesh(new THREE.PlaneGeometry(6,6), new THREE.ShadowMaterial({ opacity: 0.3, transparent: true }));
            groundPlane.rotation.x = -Math.PI/2;
            groundPlane.position.y = -0.4;
            groundPlane.receiveShadow = true;
            scene.add(groundPlane);
            
            function animate() {
                requestAnimationFrame(animate);
                controls.update();
                renderer.render(scene, camera);
                labelRenderer.render(scene, camera);
            }
            animate();
            
            window.addEventListener('resize', () => {
                const w = container.clientWidth;
                const h = container.clientHeight;
                renderer.setSize(w, h);
                labelRenderer.setSize(w, h);
                camera.aspect = w / h;
                camera.updateProjectionMatrix();
            });
        </script>
        """
        components.html(chip_3d_html, height=380)

    # Compact call to action (small text)
    st.markdown("---")
    st.markdown("### 🚀 Ready to build your own breakthrough?")
    st.markdown("Contact us for a free consultation or see sidebar for pricing.")

# ---------- ROUTING ----------
if not st.session_state.authenticated:
    login_page()
else:
    main_app()
