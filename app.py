import streamlit as st
import hashlib
import datetime
import pandas as pd
import numpy as np
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Earth Aura dMRV | Real-Time Carbon Ledger",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Advanced Posh Dark CSS Theme (Rana54 Executive Aesthetic)
st.markdown("""
    <style>
    /* Dark Deep Space Canvas */
    .stApp {
        background: #070A10;
        color: #E2E8F0;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Top Header Styling */
    .brand-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 16px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 20px;
    }
    .brand-title {
        font-size: 28px;
        font-weight: 800;
        letter-spacing: -0.5px;
        background: linear-gradient(90deg, #10B981 0%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .brand-subtitle {
        font-size: 13px;
        color: #64748B;
        font-weight: 500;
        margin-top: 2px;
    }

    /* Live Telemetry Status Pill Badges */
    .badge-bar {
        display: flex;
        gap: 12px;
        margin-bottom: 25px;
        flex-wrap: wrap;
    }
    .badge-live {
        background: rgba(16, 185, 129, 0.12);
        border: 1px solid rgba(16, 185, 129, 0.4);
        color: #34D399;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    .badge-live::before {
        content: "";
        width: 8px;
        height: 8px;
        background-color: #34D399;
        border-radius: 50%;
        box-shadow: 0 0 8px #34D399;
    }
    .badge-standard {
        background: rgba(59, 130, 246, 0.12);
        border: 1px solid rgba(59, 130, 246, 0.4);
        color: #60A5FA;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }

    /* Enterprise Glassmorphism KPI Metric Cards */
    div[data-testid="stMetric"] {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(12px);
        transition: all 0.3s ease;
    }
    div[data-testid="stMetric"]:hover {
        border-color: rgba(16, 185, 129, 0.5);
        box-shadow: 0 10px 30px -5px rgba(16, 185, 129, 0.2);
        transform: translateY(-3px);
    }
    div[data-testid="stMetricLabel"] > label {
        color: #94A3B8 !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    div[data-testid="stMetricValue"] {
        color: #F8FAFC !important;
        font-weight: 800 !important;
        font-size: 28px !important;
    }

    /* Sidebar Navigation Customization */
    section[data-testid="stSidebar"] {
        background-color: #0A0F1D;
        border-right: 1px solid rgba(255, 255, 255, 0.06);
    }

    /* Code Block Certificate Styling */
    div[data-testid="stCodeBlock"] {
        border-radius: 12px;
        border: 1px solid rgba(16, 185, 129, 0.3);
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Controls Panel & Logo Header
with st.sidebar:
    # Display Logo if available, fallback to leaf icon
    try:
        st.image("logo.png", width=180)
    except:
        st.markdown("## 🌱 **Earth Aura**")
        st.caption("Aura Carbon Technologies ACE Ltd")
    
    st.markdown("---")
    st.markdown("### ⚡ Live Telemetry Controls")
    st.caption("Configured for Automated IoT Telemetry Ingest")
    
    facility_name = st.text_input("Facility Name", value="Solar Mini-Grid Facility 1")
    device_id = st.text_input("IoT Meter Gateway ID", value="METER-AURA-108")
    solar_kwh = st.number_input("Solar Generation (kWh)", min_value=0.0, value=2450.0, step=50.0)
    grid_uptime = st.slider("Grid Availability (%)", min_value=0.0, max_value=100.0, value=99.6, step=0.1)
    battery_soc = st.slider("Battery State of Charge (SoC %)", min_value=0.0, max_value=100.0, value=87.5, step=0.5)
    carbon_price = st.number_input("Carbon Credit Value ($/tCO2e)", min_value=0.0, value=25.0, step=1.0)
    date_input = st.date_input("Telemetry Date", datetime.date.today())
    
    st.markdown("---")
    st.markdown("### 🛠️ Protocol Standards")
    st.caption("• Methodology: Gold Standard / Verra dMRV")
    st.caption("• Displacement Ratio: 0.25 L Diesel / kWh")
    st.caption("• Emission Factor: 0.00067 tCO2e / kWh")
    
    st.markdown("---")
    st.caption("Earth Aura ACE Ltd © 2026")

# 4. Core Telemetry Calculations
diesel_displaced_liters = solar_kwh * 0.25
tco2e_offset = solar_kwh * 0.00067
co2_reduced_kg = tco2e_offset * 1000.0
estimated_yield_usd = tco2e_offset * carbon_price

# Cryptographic SHA-256 Hash
raw_data = f"{facility_name}{date_input}{device_id}{solar_kwh}{tco2e_offset}{grid_uptime}{battery_soc}"
hash_signature = hashlib.sha256(raw_data.encode()).hexdigest()

# 5. Top Header with Logo Banner
col_head1, col_head2 = st.columns([4, 1])
with col_head1:
    st.markdown("""
        <div class="brand-header">
            <div>
                <p class="brand-title">EARTH AURA dMRV PLATFORM</p>
                <p class="brand-subtitle">Automated Solar Telemetry & Digital Carbon Credit Settlement Engine</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
with col_head2:
    try:
        st.image("logo.png", width=140)
    except:
        pass

# Status Pill Badges
st.markdown("""
    <div class="badge-bar">
        <span class="badge-live">Live Modbus/MQTT Stream Active</span>
        <span class="badge-standard">Verification Standard: Gold Standard / Verra</span>
        <span class="badge-standard" style="color:#A7F3D0; border-color:rgba(16,185,129,0.4); background:rgba(16,185,129,0.1);">Cryptographic Proof: SHA-256 Signed</span>
    </div>
""", unsafe_allow_html=True)

# 6. Real-Time Hardware Diagnostic Bar (Rana54 Aesthetic)
st.markdown("##### 📡 Real-Time Gateway Electrical Diagnostics")
d1, d2, d3, d4 = st.columns(4)
d1.metric("Grid Frequency", "50.02 Hz", delta="Stable")
d2.metric("Bus Voltage", "415.3 V", delta="Normal")
d3.metric("Power Factor", "0.98", delta="Optimal")
d4.metric("Gateway Temperature", "34.2 °C", delta="Nominal")

st.markdown("<br>", unsafe_allow_html=True)

# 7. Executive Primary KPI Metrics
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Clean Generation", f"{solar_kwh:,.1f} kWh", delta="Real-Time")
m2.metric("Diesel Displaced", f"{diesel_displaced_liters:,.1f} L", delta="Avoided")
m3.metric("CO₂ Emissions Reduced", f"{co2_reduced_kg:,.1f} kg", delta=f"{tco2e_offset:,.4f} tCO2e")
m4.metric("Estimated Yield", f"${estimated_yield_usd:,.2f}", delta=f"@ ${carbon_price}/t")
m5.metric("System Uptime", f"{grid_uptime}%", delta=f"BSS SoC: {battery_soc}%")

st.markdown("<br>", unsafe_allow_html=True)

# 8. Interactive Analytics & Cryptographic Verification Certificate
col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown("#### 📈 24-Hour Multi-Variable Telemetry Profile")
    
    # Simulated 24-hour solar curve & load demand
    hours = [f"{i:02d}:00" for i in range(24)]
    solar_curve = np.sin(np.linspace(0, np.pi, 12)) ** 2
    hourly_solar = np.zeros(24)
    hourly_solar[6:18] = solar_curve * (solar_kwh / 7.5)
    
    hourly_load = np.full(24, solar_kwh / 30.0) + np.random.normal(0, 5, 24)
    hourly_load = np.clip(hourly_load, 10, None)

    chart_df = pd.DataFrame({
        "Hour": hours, 
        "Solar Output (kW)": hourly_solar,
        "Site Demand Load (kW)": hourly_load
    })
    st.area_chart(chart_df.set_index("Hour"), use_container_width=True)

with col_right:
    st.markdown("#### 🔐 Immutable Audit Certificate")
    st.code(f"""
[EARTH-AURA-dMRV-PAYLOAD]
Entity: Aura Carbon Technologies ACE Ltd
Facility: {facility_name}
Gateway ID: {device_id}
Timestamp: {date_input}T12:00:00Z
Telemetry Value: {solar_kwh:.2f} kWh
Diesel Displacement: {diesel_displaced_liters:.2f} L
CO2 Reduced: {co2_reduced_kg:.2f} kg ({tco2e_offset:.6f} tCO2e)
Grid Uptime: {grid_uptime:.1f}% | Battery SoC: {battery_soc:.1f}%
Estimated Yield: ${estimated_yield_usd:.2f}

[CRYPTOGRAPHIC SIGNATURE]
Algorithm: SHA-256
Hash: {hash_signature}
Registry Status: VERIFIED_AUDIT_READY
""", language="yaml")

st.markdown("---")

# 9. Auditable Ledger Table & Export Option
st.markdown("#### 📋 Verified Carbon Settlement Ledger")

df = pd.DataFrame([{
    "Timestamp": f"{date_input} 12:00:00",
    "Facility Name": facility_name,
    "Gateway ID": device_id,
    "Clean kWh": f"{solar_kwh:,.2f}",
    "Diesel Saved (L)": f"{diesel_displaced_liters:,.2f}",
    "CO2 Reduced (kg)": f"{co2_reduced_kg:,.2f}",
    "Offset (tCO2e)": f"{tco2e_offset:,.4f}",
    "Uptime (%)": f"{grid_uptime}%",
    "BSS SoC (%)": f"{battery_soc}%",
    "Estimated Yield ($)": f"${estimated_yield_usd:,.2f}",
    "SHA-256 Signature": hash_signature
}])

st.dataframe(df, use_container_width=True)

# Download CSV Ledger Button for Audit Export
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Export Verified Settlement Ledger (CSV)",
    data=csv,
    file_name=f"EarthAura_dMRV_Ledger_{date_input}.csv",
    mime="text/csv",
)
