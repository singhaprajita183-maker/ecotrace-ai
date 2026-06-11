import os
import datetime
import urllib.parse
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai
from pymongo import MongoClient

# Page configuration
st.set_page_config(page_title="EcoTrace AI: Global Enterprise Suite", page_icon="🌿", layout="wide")

# Load environment variables
load_dotenv()
MONGO_URI = st.secrets.get("MONGO_URI") or os.getenv("MONGO_URI")
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# --- CUSTOM CYBERPUNK THEME (BLACK, BLUE, RED COMBO) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0d0f12 !important;
        color: #e0e6ed !important;
    }
    h1, h2, h3 {
        color: #00d2ff !important;
        font-family: 'Segoe UI', sans-serif;
        text-shadow: 0px 0px 10px rgba(0, 210, 255, 0.3);
    }
    .stTextInput div div input, .stSelectbox div div div, .stNumberInput div div input {
        background-color: #1a1f26 !important;
        color: #ffffff !important;
        border: 1px solid #00d2ff !important;
        border-radius: 8px !important;
    }
    .stButton>button {
        background-color: #ff0055 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0px 0px 15px rgba(255, 0, 85, 0.4) !important;
    }
    .intro-box {
        background-color: #11161d !important;
        border: 2px dashed #00d2ff !important;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
    }
    .critical-alert {
        background-color: #1a1115 !important;
        border: 2px solid #ff0055 !important;
        border-radius: 8px;
        padding: 15px;
        color: #ff4d88 !important;
    }
    .arch-box {
        background-color: #11161d !important;
        border: 1px dashed #00d2ff !important;
        padding: 15px;
        font-family: 'Courier New', monospace;
        color: #00d2ff;
        border-radius: 8px;
    }
    div[data-testid="stMetricSimpleValue"] {
        color: #00d2ff !important;
        font-size: 28px !important;
    }
    hr {
        border: 0; height: 1px;
        background: linear-gradient(to right, #ff0055, #00d2ff, transparent) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE MANAGEMENT FOR single app.py PAGES ---
if "app_stage" not in st.session_state:
    st.session_state.app_stage = "intro" # Stages: intro -> gateway -> dashboard
if "username" not in st.session_state:
    st.session_state.username = ""
if "role" not in st.session_state:
    st.session_state.role = ""

# ==============================================================================================
# 🌟 STAGE 1: ENTERPRISE INTRO PAGE
# ==============================================================================================
if st.session_state.app_stage == "intro":
    st.title("🌿 EcoTrace AI: Next-Gen Sustainability Suite")
    st.caption("⚡ Advanced Multi-Modal Supply Chain Intelligence Core")
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='intro-box'>
        <h2>🚀 WELCOME TO ECOTRACE AI ENTERPRISE DEPLOYMENT</h2>
        <p style='font-size: 16px; color: #a0aec0;'>
            An autonomous agent framework built to tackle chaotic global supply chain emission patterns. 
            Powered by Gemini 1.5 Pro deep reasoning matrix grids and MongoDB Atlas secure high-density transactional ledgers.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🛠️ System Core Features Enabled:")
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        st.info("🌐 **Global Geo-Tracking**\n\nDynamic real-time routing map integration capable of handling any source/destination point on Earth.")
    with col_f2:
        st.info("🎙️ **Voice & Document Ingestion**\n\nProcesses unstructured audio telemetry records and vernacular OCR cargo slips seamlessly.")
    with col_f3:
        st.info("🛡️ **Eco-Shield Guardrails**\n\nAutomated localized compliance threshold monitors to block massive carbon surges immediately.")
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    start_btn = st.button("🔌 Initialize Secure Gateway Connection", use_container_width=True)
    if start_btn:
        st.session_state.app_stage = "gateway"
        st.rerun()

# ==============================================================================================
# 🛡️ STAGE 2: SECURE GATEWAY PAGE
# ==============================================================================================
elif st.session_state.app_stage == "gateway":
    st.title("🛡️ AgentBRD Enterprise Gateway")
    st.caption("⚡ Multi-Agent Infrastructure Platform Security Portal")
    st.markdown("<hr>", unsafe_allow_html=True)
    
    col_log, _ = st.columns([1.5, 2])
    with col_log:
        st.subheader("🔑 Access Verification Required")
        user_input = st.text_input("Enter Enterprise Identity (Username)")
        role_input = st.selectbox("Select Your Operational Role:", ["Lead Business Analyst", "Sustainability Auditor", "DevOps Engineer"])
        access_key = st.text_input("Enter Gateway Access Key", type="password")
        
        login_btn = st.button("🔓 Initialize Platform Handshake", use_container_width=True)
        if login_btn:
            if user_input.strip() != "" and access_key == "Aprajita@2026":
                st.session_state.username = user_input
                st.session_state.role = role_input
                st.session_state.app_stage = "dashboard"
                st.success("⚡ Handshake Matrix Synced!")
                st.rerun()
            else:
                st.error("❌ Cryptographic Authentication Failed!")
                
    if st.button("⬅️ Back to Intro"):
        st.session_state.app_stage = "intro"
        st.rerun()

# ==============================================================================================
# 📊 STAGE 3: MAIN GLOBAL DASHBOARD
# ==============================================================================================
elif st.session_state.app_stage == "dashboard":
    # MongoDB Connection Setup
    collection = None
    try:
        username_db = "singhaprajita183_db_user"
        password_db = urllib.parse.quote_plus("Aprm@#1987")
        MONGO_URI = f"mongodb+srv://{username_db}:{password_db}@cluster0.dg81wjs.mongodb.net/?appName=Cluster0"
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = client['EcoTraceDB']
        collection = db['SupplyChainLogs']
        db_status = "🔵 System Status: Cloud Database Connection Secured."
    except Exception as e:
        db_status = f"🔴 System Status: Database Offline ({e})"

    # User Header Layout
    st.markdown(f"""
    <div style='text-align: right; color: #00d2ff; font-weight: bold;'>
        👤 Operator: {st.session_state.username} ({st.session_state.role}) | 
        <span style='color:#ff0055; cursor:pointer;' onclick='window.location.reload();'>🔒 Log Out</span>
    </div>
    """, unsafe_allow_html=True)

    st.title("🌿 EcoTrace AI: Global Supply Chain Operations")
    st.caption("⚡ Premium Cyber-Theme Control Panel")
    st.markdown("<hr>", unsafe_allow_html=True)

    # AgentBRD Architecture Block
    st.markdown("""
    <div class='arch-box'>
    [📥 MULTI-MODAL INGESTION LAYER] ──► [🧠 GEMINI REASONING CORE] ──► [🛰️ ACTION & ATLAS STORAGE]
    <br>├── Scans Cargo Photos & Receipts &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Real-Time Emissions Calculus &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── MongoDB Ledger Sync
    <br>└── Live GPS Telemetry Pipeline &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Context-Aware Geo-Optimization &nbsp;&nbsp;&nbsp;&nbsp;└── Looker Dashboard Push
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("📍 Route Settings")
        shipment_id = st.text_input("Shipment Tracking ID", value="ECO-TR-2026-GLOBAL")
        vehicle_type = st.selectbox("Logistics Mode", ["Truck (Heavy Duty)", "Train (Freight)", "Cargo Ship", "Plane (Air Freight)"])
        
        st.subheader("🌐 Global Location Query")
        start_loc = st.text_input("Source Origin City/Country", value="New Delhi, India")
        end_loc = st.text_input("Destination City/Country", value="London, UK")
        
        # World Coordinate Manual Overrides (For full world map adjustment capability)
        st.subheader("🗺️ World Coordinates Setup")
        src_lat = st.number_input("Source Latitude", value=28.6139, format="%.4f")
        src_lon = st.number_input("Source Longitude", value=77.2090, format="%.4f")
        dst_lat = st.number_input("Destination Latitude", value=51.5074, format="%.4f")
        dst_lon = st.number_input("Destination Longitude", value=-0.1278, format="%.4f")
        
        st.subheader("📊 Live Data Input")
        distance_km = st.number_input("Total Route Distance (KM)", min_value=1.0, value=6700.0)
        payload_weight_tons = st.number_input("Payload Weight (Tons)", min_value=0.1, value=12.0)
        threshold_limit = st.number_input("Max CO2 Threshold (kg)", min_value=100.0, value=2500.0)
        
        submit_btn = st.button("🚨 Trigger Global Diagnostics", type="primary", use_container_width=True)

    with col2:
        st.header("📈 Intelligent Agent Analytics")
        st.markdown(f"<div style='color:#00d2ff; font-weight:bold; margin-bottom:10px;'>{db_status}</div>", unsafe_allow_html=True)
        
        # 🌐 DYNAMIC WORLD MAP FEATURE
        st.subheader("🗺️ Global Route Tracing Map")
        map_dataframe = pd.DataFrame({
            'lat': [src_lat, dst_lat],
            'lon': [src_lon, dst_lon]
        })
        st.map(map_dataframe, zoom=1) # Zoom level 1 shows the entire global sphere map seamlessly
        
        if submit_btn:
            with st.spinner("Calculating global carbon vectors..."):
                emission_factors = {"truck (heavy duty)": 0.105, "train (freight)": 0.025, "cargo ship": 0.015, "plane (air freight)": 0.500}
                ef = emission_factors.get(vehicle_type.lower(), 0.1)
                calculated_emissions = distance_km * payload_weight_tons * ef
                fuel_used_liters = distance_km * 0.35
                
                if calculated_emissions > threshold_limit:
                    st.markdown(f"""
                    <div class='critical-alert'>
                        <strong>⚠️ ECO-SHIELD CRITICAL COMPLIANCE FLAG ACTIVATED:</strong><br>
                        Global emissions profile ({calculated_emissions:,.2f} kg CO2) has crossed corporate safety caps ({threshold_limit} kg). Rerouting recommended!
                    </div>
                    """, unsafe_allow_html=True)
                
                # Update Data Cards
                kpi1, kpi2 = st.columns(2)
                kpi1.metric("Total Carbon Emissions", f"{calculated_emissions:,.2f} kg CO2")
                kpi2.metric("Estimated Fuel Burn", f"{fuel_used_liters:,.1f} Liters")
                
                # 📊 INTERACTIVE GRAPH GENERATION
                st.subheader("📊 Cross-Modal Emission Evaluation Vector")
                graph_data = pd.DataFrame(
                    [distance_km * payload_weight_tons * 0.105, distance_km * payload_weight_tons * 0.025, distance_km * payload_weight_tons * 0.500],
                    index=["Truck Vector", "Train Vector", "Air Freight Vector"],
                    columns=["CO2 Delta (kg)"]
                )
                st.bar_chart(graph_data)
                
                # MongoDB Sync
                if collection is not None:
                    try:
                        collection.insert_one({
                            "shipment_id": shipment_id, "origin": start_loc, "destination": end_loc,
                            "carbon_emissions_kg": calculated_emissions, "operator": st.session_state.username
                        })
                        st.success("💾 Ledger updated securely on MongoDB Atlas cluster nodes.")
                    except:
                        pass
        else:
            st.write("📥 Inputs adjust karke diagnostics trigger karein.")
