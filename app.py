import streamlit as st
import streamlit.components.v1 as components
import random

VIDEO_URL = "https://raw.githubusercontent.com/Deslandes1/Hack-Clubber-s-open-source-LEGO-3D-printer./main/Demo1.mp4"

st.set_page_config(
    page_title="Studprint | Open‑Source LEGO 3D Printer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- LOGIN STATE ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "app_mode" not in st.session_state:
    st.session_state.app_mode = "Story & Demo"  # or "Real Software"

# ---------- STYLING ----------
st.markdown(r"""
<style>
    .stApp { background: linear-gradient(135deg, #0b1120, #1a2332); }
    .main .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    .spinning-globe { display: inline-block; animation: spin 4s linear infinite; font-size: 3rem; }
    .power-symbol { font-size: 2.5rem; text-align: center; animation: pulse 1.5s infinite; margin-bottom: 0.5rem; }
    @keyframes pulse { 0% { transform: scale(1); opacity: 0.8; } 50% { transform: scale(1.1); opacity: 1; } 100% { transform: scale(1); opacity: 0.8; } }
    .story-text {
        font-family: 'Georgia', serif; font-size: 1rem; line-height: 1.5; color: #e0e0e0;
        background: rgba(0,0,0,0.4); padding: 0.8rem; border-radius: 15px;
        border-left: 4px solid #ff6b6b; max-height: 200px; overflow-y: auto; margin-bottom: 0.5rem;
    }
    h1, h2, h3 { color: #ffaa66 !important; margin-top: 0 !important; margin-bottom: 0.2rem !important; }
    h1 { font-size: 2rem !important; }
    h2 { font-size: 1.3rem !important; }
    .stMarkdown, .stSidebar .stMarkdown { color: #fff !important; }
    .stButton button { background-color: #ff6b6b !important; color: white !important; border-radius: 30px !important; font-weight: bold !important; padding: 0.2rem 1rem !important; }
    [data-testid="stSidebar"] { background: #0a0f1a; border-right: 1px solid #2a3a4a; }
    .pricing-card, .real-software-card { background: rgba(255,255,255,0.05); border-radius: 15px; padding: 0.6rem; margin: 0.5rem 0; border: 1px solid #ffaa66; font-size: 0.9rem; }
    .real-software-card a { color: #ffaa66; text-decoration: none; font-weight: bold; }
    .stVideo { margin: 0.5rem 0; }
    footer { display: none; }
    /* Real software dashboard styling */
    .printer-status { background: #0f172a; border-radius: 15px; padding: 1rem; margin: 1rem 0; border: 1px solid #ffaa66; }
    .temp-bar { height: 8px; background: #ffaa66; border-radius: 5px; transition: width 0.3s; }
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

# ---------- REAL SOFTWARE (interactive printer controller) ----------
def real_software():
    st.markdown("## 🖨️ Studprint Controller")
    st.markdown("Control your LEGO 3D printer, monitor temperatures, and run test prints.")

    # Simulated printer state
    if "print_running" not in st.session_state:
        st.session_state.print_running = False
        st.session_state.progress = 0
        st.session_state.temp_nozzle = 210.0
        st.session_state.temp_bed = 60.0

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🔥 Nozzle")
        st.metric("Temperature", f"{st.session_state.temp_nozzle:.1f} °C", delta="▲")
        st.progress(min(st.session_state.temp_nozzle / 300, 1.0), text="Heating")
    with col2:
        st.markdown("### 🧊 Bed")
        st.metric("Temperature", f"{st.session_state.temp_bed:.1f} °C", delta="▲")
        st.progress(min(st.session_state.temp_bed / 100, 1.0), text="Heating")

    # Print control
    st.markdown("### 📁 Print Job")
    gcode_file = st.selectbox("Select test file", ["Calibration Cube.gcode", "LEGO Brick.stl", "Benchy.gcode"])
    if st.button("Start Print"):
        st.session_state.print_running = True
        st.session_state.progress = 0
        st.success("Print started. Simulating...")
    if st.button("Stop / Cancel"):
        st.session_state.print_running = False
        st.session_state.progress = 0
        st.warning("Print cancelled.")

    if st.session_state.print_running:
        # Simulate progress
        if st.session_state.progress < 100:
            st.session_state.progress += random.randint(2, 5)
            if st.session_state.progress > 100:
                st.session_state.progress = 100
        progress_bar = st.progress(st.session_state.progress / 100)
        st.markdown(f"**Progress:** {st.session_state.progress}%")
        if st.session_state.progress >= 100:
            st.success("Print completed! 🎉")
            st.session_state.print_running = False
            st.balloons()
        # Simulate temperature changes
        st.session_state.temp_nozzle = 210 + random.uniform(-2, 2)
        st.session_state.temp_bed = 60 + random.uniform(-1, 1)
        st.rerun()

    # Manual controls
    st.markdown("### 🔧 Manual Commands")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        if st.button("Home All"):
            st.info("Homing axes...")
    with col_b:
        if st.button("Fan On"):
            st.info("Part cooling fan ON")
    with col_c:
        if st.button("Fan Off"):
            st.info("Fan OFF")

    # Status display
    st.markdown("---")
    st.markdown("### 📡 Live Webcam Feed (simulated)")
    st.image("https://via.placeholder.com/640x360?text=Studprint+Camera+Feed", caption="Camera Preview", use_container_width=True)
    st.caption("Real software: This controller communicates with the actual Studprint printer via USB. All commands are simulated in this demo.")

# ---------- DEMO MODE (original story + video + chip) ----------
def demo_mode():
    st.markdown('<div class="power-symbol" style="display: flex; justify-content: center; gap: 20px;">🧠 🖨️ ⚡ 🔧</div>', unsafe_allow_html=True)
    st.title("Not every breakthrough starts in a lab.")
    st.markdown("### Some start with curiosity, creativity—and a box of bricks.")

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
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🎬 Demo: Studprint in Action")
    try:
        st.video(VIDEO_URL)
    except Exception:
        st.markdown(f"[Watch the demo video here]({VIDEO_URL})")

    st.markdown("### 🧠 The Brain of Studprint – Interactive 3D Chip")
    chip_3d_html = """
    <div id="chip-viewer" style="height: 360px; width: 100%; border-radius: 20px; overflow: hidden;"></div>
    <script type="importmap">
        { "imports": { "three": "https://unpkg.com/three@0.128.0/build/three.module.js", "three/addons/": "https://unpkg.com/three@0.128.0/examples/jsm/" } }
    </script>
    <script type="module">
        import * as THREE from 'three';
        import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
        import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';
        const container = document.getElementById('chip-viewer');
        const scene = new THREE.Scene(); scene.background = new THREE.Color(0x0a0f1a);
        const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
        camera.position.set(3, 2, 4);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, container.clientHeight); renderer.shadowMap.enabled = true;
        container.appendChild(renderer.domElement);
        const labelRenderer = new CSS2DRenderer(); labelRenderer.setSize(container.clientWidth, container.clientHeight);
        labelRenderer.domElement.style.position = 'absolute'; labelRenderer.domElement.style.top = '0px';
        labelRenderer.domElement.style.left = '0px'; container.appendChild(labelRenderer.domElement);
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true; controls.autoRotate = true; controls.autoRotateSpeed = 1.0;
        const bodyMat = new THREE.MeshStandardMaterial({ color: 0x2a2a2a, roughness: 0.3 });
        const chipBase = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.3, 2.0), bodyMat);
        chipBase.castShadow = true; scene.add(chipBase);
        const topMat = new THREE.MeshStandardMaterial({ color: 0x333333, roughness: 0.2, metalness: 0.4 });
        const chipTop = new THREE.Mesh(new THREE.BoxGeometry(1.8, 0.05, 1.8), topMat);
        chipTop.position.y = 0.18; scene.add(chipTop);
        const pinMat = new THREE.MeshStandardMaterial({ color: 0xccaa33, metalness: 0.9 });
        const pinPositions = [[[-1.05,0,-0.7],[-1.05,0,-0.3],[-1.05,0,0.1],[-1.05,0,0.5],[-1.05,0,0.9]],
                              [[ 1.05,0,-0.7],[ 1.05,0,-0.3],[ 1.05,0,0.1],[ 1.05,0,0.5],[ 1.05,0,0.9]],
                              [[-0.7,0,-1.05],[-0.3,0,-1.05],[0.1,0,-1.05],[0.5,0,-1.05],[0.9,0,-1.05]],
                              [[-0.7,0, 1.05],[-0.3,0, 1.05],[0.1,0, 1.05],[0.5,0, 1.05],[0.9,0, 1.05]]];
        pinPositions.forEach(side => { side.forEach(pos => { const pin = new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.08, 0.4), pinMat);
        pin.position.set(pos[0], pos[1]-0.12, pos[2]); pin.castShadow = true; scene.add(pin); }); });
        function makeLabel(text, x, y, z, size='14px') { const div = document.createElement('div'); div.textContent = text;
        div.style.cssText = 'color:#ffaa66; font-size:'+size+'; font-weight:bold; font-family:monospace; background:rgba(0,0,0,0.6); padding:2px 6px; border-radius:8px; border:1px solid #ffaa66;';
        const label = new CSS2DObject(div); label.position.set(x, y, z); scene.add(label); }
        makeLabel('Studprint', 0, 0.35, 0, '16px'); makeLabel('ARM Cortex-M4', 0, -0.15, 1.2, '12px');
        const ambient = new THREE.AmbientLight(0x404060); scene.add(ambient);
        const mainLight = new THREE.DirectionalLight(0xffffff, 1.2); mainLight.position.set(2,3,4); mainLight.castShadow = true; scene.add(mainLight);
        const ground = new THREE.Mesh(new THREE.PlaneGeometry(6,6), new THREE.ShadowMaterial({ opacity: 0.3, transparent: true }));
        ground.rotation.x = -Math.PI/2; ground.position.y = -0.4; ground.receiveShadow = true; scene.add(ground);
        function animate() { requestAnimationFrame(animate); controls.update(); renderer.render(scene, camera); labelRenderer.render(scene, camera); }
        animate();
        window.addEventListener('resize', () => { const w = container.clientWidth, h = container.clientHeight;
        renderer.setSize(w, h); labelRenderer.setSize(w, h); camera.aspect = w/h; camera.updateProjectionMatrix(); });
    </script>
    """
    components.html(chip_3d_html, height=380)
    st.markdown("---")
    st.markdown("### 🚀 Ready to build your own breakthrough?")
    st.markdown("Contact us for a free consultation or see sidebar for pricing.")

# ---------- MAIN APP ----------
def main_app():
    # ========== SIDEBAR (shared) ==========
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
        
        # ---- APP MODE SELECTOR ----
        st.markdown("### 🧪 Select Experience")
        app_mode = st.radio("", ["Story & Demo", "Real Software"], index=0 if st.session_state.app_mode == "Story & Demo" else 1)
        if app_mode != st.session_state.app_mode:
            st.session_state.app_mode = app_mode
            st.rerun()
        
        # ---- Logout button ----
        if st.button("Logout", key="logout_btn"):
            st.session_state.authenticated = False
            st.rerun()

    # ========== MAIN CONTENT ==========
    if st.session_state.app_mode == "Story & Demo":
        demo_mode()
    else:
        real_software()

# ---------- ROUTING ----------
if not st.session_state.authenticated:
    login_page()
else:
    main_app()
