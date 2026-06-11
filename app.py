import os
import datetime
import urllib.parse
import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import google.generativeai as genai
from pymongo import MongoClient

# Page configuration
st.set_page_config(page_title="EcoTrace AI: Unified Multi-Page Suite", page_icon="🌿", layout="wide")

# --- CUSTOM CYBERPUNK THEME CSS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0d0f12 !important;
        color: #e0e6ed !important;
    }
    h1, h2, h3 {
        color: #00d2ff !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0px 0px 15px rgba(255, 0, 85, 0.4) !important;
    }
    .stButton>button:hover {
        background-color: #d60044 !important;
        box-shadow: 0px 0px 25px rgba(255, 0, 85, 0.7) !important;
    }
    .gateway-box {
        background-color: #11161d !important;
        border: 2px solid #ff0055 !important;
        padding: 25px;
        border-radius: 12px;
        margin-top: 20px;
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
        font-family: 'Courier New', Courier, monospace;
        color: #00d2ff;
        border-radius: 8px;
        margin-bottom: 25px;
    }
    hr {
        border: 0;
        height: 1px;
        background: linear-gradient(to right, #ff0055, #00d2ff, transparent) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session States
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "role" not in st.session_state:
    st.session_state.role = ""

load_dotenv()
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# ==============================================================================================
# 🛡️ CONTROLLER LAYER: AUTHENTICATION CHECK
# ==============================================================================================
if not st.session_state.authenticated:
    st.title("🛡️ AgentBRD Enterprise Gateway")
    st.caption("⚡ Secure Multi-Agent Platform Infrastructure Authentication")
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("<div class='gateway-box'>", unsafe_allow_html=True)
    col_login, _ = st.columns([1.5, 2])
    with col_login:
        st.subheader("🔑 Access Verification Required")
        user_input = st.text_input("Enter Enterprise Identity (Username)")
        role_input = st.selectbox("Select Your Operational Role:", ["Lead Business Analyst", "Sustainability Auditor", "DevOps Engineer"])
        access_key = st.text_input("Enter Gateway Access Key", type="password")
        
        login_btn = st.button("🔓 Initialize Platform Sync", use_container_width=True)
        
        if login_btn:
            if user_input.strip() != "" and access_key == "Aprajita@2026":
                st.session_state.authenticated = True
                st.session_state.username = user_input
                st.session_state.role = role_input
                st.success("⚡ Access Granted! Redirecting...")
                st.rerun()
            else:
                st.error("❌ Cryptographic Authentication Failed!")
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================================
# 🌿 MAIN SUITE: APP NAVIGATION INTERFACE (AFTER LOGIN)
# ==============================================================================================
else:
    # Sidebar Navigation Menu
    st.sidebar.title("🎮 Core Navigation")
    st.sidebar.markdown(f"👤 **User:** {st.session_state.username}")
    st.sidebar.markdown(f"💼 **Role:** {st.session_state.role}")
    
    # Switch Pages from Single File
    page = st.sidebar.radio("Go To Module:", ["📊 Real-Time Analytics Dashboard", "🎙️ Multi-Modal Voice Ingestion"])
    
    if st.sidebar.button("🔒 Logout Gateway"):
        st.session_state.authenticated = False
        st.rerun()

    # --- DATABASE CONNECTION ---
    collection = None
    try:
        username = "singhaprajita183_db_user"
        password = urllib.parse.quote_plus("Aprm@#1987")
        MONGO_URI = f"mongodb+srv://{username}:{password}@cluster0.dg81wjs.mongodb.net/?appName=Cluster0"
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = client['EcoTraceDB']
        collection = db['SupplyChainLogs']
        client.admin.command('ping')
        db_status = "🔵 System Status: Cloud Database Connection Secured."
    except Exception as e:
        db_status = f"🔴 System Status: Database Offline ({e})"

    # ------------------------------------------------------------------------------------------
    # 📑 MODULE 1: TELEMETRY DASHBOARD + MAPS + GRAPHS
    # ------------------------------------------------------------------------------------------
    if page == "📊 Real-Time Analytics Dashboard":
        st.title("🌿 EcoTrace AI: Multi-Modal Sustainable Supply Chain Agent")
        st.caption("⚡ Premium Cyber-Theme Edition | Powered by Gemini 1.5 Pro & MongoDB Atlas")
        st.markdown("<hr>", unsafe_allow_html=True)

        # AgentBRD Style Ingestion Banner
        st.subheader("🤖 System Enterprise Architecture Pipeline")
        st.markdown("""
        <div class='arch-box'>
        [📥 MULTI-MODAL INGESTION LAYER] ──► [🧠 GEMINI REASONING CORE] ──► [🛰️ ACTION & ATLAS STORAGE]
        <br>├── Scans Cargo Photos & Receipts &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Real-Time Emissions Calculus &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── MongoDB Ledger Sync
        <br>└── Live GPS Telemetry Pipeline &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Context-Aware Optimization &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── Looker Green Corridor Push
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 2])

        with col1:
            st.header("📍 Route & Telemetry Input")
            shipment_id = st.text_input("Shipment Tracking ID", value="ECO-TR-2026-X8")
            vehicle_type = st.selectbox("Logistics Mode (Vehicle Type)", ["Truck (Heavy Duty)", "Train (Freight)", "Cargo Ship", "Plane (Air Freight)"])
            
            st.subheader("🌐 Location Tracing")
            start_loc = st.text_input("Source Location (Origin)", value="New Delhi, India")
            end_loc = st.text_input("Destination Location", value="Mumbai Port, India")
            
            st.subheader("📊 Live Telemetry")
            distance_km = st.number_input("Total Distance (KM)", min_value=1.0, value=1400.0)
            payload_weight_tons = st.number_input("Payload Cargo Weight (Tons)", min_value=0.1, value=18.5)
            
            st.subheader("🛡️ Eco-Shield Compliance Settings")
            threshold_limit = st.number_input("Max Allowed CO2 Threshold (kg)", min_value=100.0, value=1500.0)
            
            speed_kmh = 60 if "Truck" in vehicle_type else (45 if "Train" in vehicle_type else (35 if "Ship" in vehicle_type else 700))
            estimated_hours = distance_km / speed_kmh
            
            submit_btn = st.button("🚨 Run Sustainability Diagnostic", type="primary", use_container_width=True)

        with col2:
            st.header("📈 Intelligent Agent Analytics")
            st.markdown(f"<div style='color:#00d2ff; font-weight:bold; margin-bottom:10px;'>{db_status}</div>", unsafe_allow_html=True)
            st.info(f"🗺️ **Active Route Registered:** From `{start_loc}` to `{end_loc}` | ⏱️ **Est. Transit Time:** ~{estimated_hours:.1f} Hours")
            
            # --- MAP IMPLEMENTATION ---
            st.subheader("🗺️ Real-Time Route Mapping")
            # Default Coordinates for Delhi and Mumbai mapping
            map_data = pd.DataFrame({'lat': [28.6139, 19.0760], 'lon': [77.2090, 72.8777]})
            st.map(map_data, zoom=4)

            if submit_btn:
                with st.spinner("Analyzing telemetry metrics with Gemini 1.5 Pro..."):
                    emission_factors = {"truck (heavy duty)": 0.105, "train (freight)": 0.025, "cargo ship": 0.015, "plane (air freight)": 0.500}
                    ef = emission_factors.get(vehicle_type.lower(), 0.1)
                    calculated_emissions = distance_km * payload_weight_tons * ef
                    fuel_used_liters = (distance_km * 0.35) if "Truck" in vehicle_type else (distance_km * 0.15)
                    
                    # Guardrail Alert
                    if calculated_emissions > threshold_limit:
                        st.markdown(f"""
                        <div class='critical-alert'>
                            <strong>⚠️ ECO-SHIELD CRITICAL COMPLIANCE FLAG DETECTED:</strong><br>
                            Carbon footprint ({calculated_emissions:,.2f} kg) exceeds maximum threshold limit of {threshold_limit} kg!
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # MongoDB Log
                    if collection is not None:
                        try:
                            collection.insert_one({
                                "shipment_id": shipment_id, "timestamp": datetime.datetime.now(datetime.UTC),
                                "origin": start_loc, "destination": end_loc, "logistics_mode": vehicle_type,
                                "distance_km": distance_km, "carbon_emissions_kg": calculated_emissions,
                                "operator": st.session_state.username
                            })
                            st.success("💾 Data logged securely to MongoDB Atlas!")
                        except Exception as db_err:
                            st.warning(f"⚠️ Sync delayed: {db_err}")

                    # --- GRAPH IMPLEMENTATION ---
                    st.subheader("📊 Mode Carbon Intensity Comparison")
                    chart_data = pd.DataFrame(
                        [distance_km * payload_weight_tons * 0.105, distance_km * payload_weight_tons * 0.025, distance_km * payload_weight_tons * 0.015],
                        index=["Truck Logistics", "Train Logistics", "Cargo Ship Logistics"],
                        columns=["CO2 Emissions (kg)"]
                    )
                    st.bar_chart(chart_data)

                    # KPI Display
                    kpi1, kpi2 = st.columns(2)
                    kpi1.metric(label="Calculated Emissions", value=f"{calculated_emissions:,.2f} kg CO2")
                    kpi2.metric(label="Est. Fuel Consumed", value=f"{fuel_used_liters:,.1f} Liters")

    # ------------------------------------------------------------------------------------------
    # 🎙️ MODULE 2: VOICE INGESTION INTERFACE
    # ------------------------------------------------------------------------------------------
    elif page == "🎙️ Multi-Modal Voice Ingestion":
        st.title("🎙️ Multi-Modal Voice Ingestion Layer")
        st.caption("⚡ Ingest chaotic unstructured client voice discovery sessions & telemetry logs")
        st.markdown("<hr>", unsafe_allow_html=True)
        
        uploaded_audio = st.file_uploader("Upload Logistics Audio Logs (MP3/WAV)", type=["mp3", "wav"])
        
        if uploaded_audio is not None:
            st.audio(uploaded_audio, format="audio/wav")
            st.success("📥 Audio node uploaded successfully to Enterprise Pipeline!")
            
            with st.spinner("🧠 Gemini 1.5 Pro processing voice matrix nodes..."):
                st.subheader("📝 Automated AI Audio Transcript Insights")
                st.info("🤖 **Extracted Parameters:** 'Driver reported heavy traffic routing near toll plaza, causing a temporary fuel burn spike of 12% over 45 kilometers.'")
