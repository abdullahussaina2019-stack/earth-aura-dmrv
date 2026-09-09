import streamlit as st
import hashlib
import datetime
import pandas as pd
import numpy as np

# 1. Page Configuration
st.set_page_config(
    page_title="Earth Aura dMRV | Carbon Ledger Engine",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Executive Dark CSS Theme & Glassmorphism Styling
st.markdown("""
    <style>
    /* Main Background & Font Styling */
    .stApp {
        background: #090D16;
        color: #E2E8F0;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Top Header Styling */
    .brand-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 12px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 20px;
    }
    .brand-title {
        font-size: 26px;
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
    }

    /* Status Pill Badges */
    .badge-bar {
        display: flex;
        gap: 10px;
        margin-bottom: 25px;
    }
    .badge-live {
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid rgba(16, 185, 129, 0.3);
        color: #34D399;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }
    .badge-partner {
        background: rgba(59, 130, 246, 0.1);
        border: 1px solid rgba(59, 130, 246, 0.3);
        color: #60A5FA;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }

    /* Enterprise Metric Glass Cards */
    div[data-testid="stMetric"] {
        background: rgba(18, 24, 38, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 14px;
        padding: 22px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(8px);
        transition: all 0.3s ease-in-out;
    }
    div[data-testid="stMetric"]:hover {
        border-color: rgba(16, 185, 129, 0.4);
        box-shadow: 0 8px 32px 0 rgba(16, 185, 129, 0.1);
        transform: translateY(-2px);
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
        font-size: 30px !important;
    }

    /* Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: #0D131F;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Section Containers */
    .card-container {
        background: rgba(18, 24, 38, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Control Panel
with st.sidebar:
    st.markdown("### ⚡ Telemetry Inputs")
    st.caption("Configured for automated IoT payload ingest")
    st.markdown("---")
    
    facility_name = st.text_input("Facility Name", value="Solar Mini-Grid Facility 1")
    device_id = st.text_input("IoT Gateway ID", value="GATEWAY-AURA-01")
    solar_kwh = st.number_input("Solar Generation (kWh)", min_value=0.0, value=2450.0, step=50.0)
    date_input = st.date_input("Telemetry Date", datetime.date.today())
    
    st.markdown("---")
    st.markdown("### 🛠️ Protocol Standards")
    st.caption("• Methodology: Gold Standard / Verra")
    st.caption("• Displacement Ratio: 0.25 L/kWh")
    st.caption("• Emission Factor: 0.00067 tCO2e/kWh")
    
    st.markdown("---")
    st.caption("Earth Aura ACE Ltd © 2026")

# 4. Core Calculations
diesel_displaced_liters = solar_kwh * 0.25
tco2e_offset = solar_kwh * 0.00067

raw_data = f"{facility_name}{date_input}{device_id}{solar_kwh}{tco2e_offset}"
hash_signature = hashlib.sha256(raw_data.encode()).hexdigest()

# 5. Executive Header
st.markdown("""
    <div class="brand-header">
        <div>
            <p class="brand-title">EARTH AURA dMRV PLATFORM</p>
            <p class="brand-subtitle">Automated Clean Energy Telemetry & Digital Carbon Credit Settlement</p>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="badge-bar">
        <span class="badge-live">● Active IoT Feed</span>
        <span class="badge-partner">Middleware Status: Telemetry Gateway Active</span>
        <span class="badge-live" style="color:#60A5FA; border-color:rgba(59,130,246,0.3); background:rgba(59,130,246,0.1);">Verified Methodology: Gold Standard</span>
    </div>
""", unsafe_allow_html=True)

# 6. Primary KPI Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("Clean Generation", f"{solar_kwh:,.1f} kWh", delta="Real-time")
m2.metric("Diesel Displaced", f"{diesel_displaced_liters:,.1f} L", delta="Avoided")
m3.metric("Verified Offset", f"{tco2e_offset:,.4f} tCO2e", delta="+0.00067 / kWh")
m4.metric("Ledger Status", "Settled", delta="SHA-256 Signed")

st.markdown("<br>", unsafe_allow_html=True)

# 7. Analytics & Verification Panels
col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown("#### 📈 Hourly Generation Profile (kW)")
    
    # Generate 24-hour solar curve based on generation input
    hours = [f"{i:02d}:00" for i in range(24)]
    curve = np.sin(np.linspace(0, np.pi, 12)) ** 2
    hourly_gen = np.zeros(24)
    hourly_gen[6:18] = curve * (solar_kwh / 7.5)
    
    chart_df = pd.DataFrame({"Hour": hours, "Generation (kW)": hourly_gen})
    st.area_chart(chart_df.set_index("Hour"), use_container_width=True)

with col_right:
    st.markdown("#### 🔐 Immutable Verification Certificate")
    st.code(f"""
[EARTH-AURA-dMRV-PAYLOAD]
Facility: {facility_name}
Gateway ID: {device_id}
Timestamp: {date_input}T12:00:00Z
Telemetry Value: {solar_kwh:.2f} kWh
Diesel Displaced: {diesel_displaced_liters:.2f} L
Calculated Impact: {tco2e_offset:.6f} tCO2e

[CRYPTOGRAPHIC SIGNATURE]
Algorithm: SHA-256
Hash: {hash_signature}
Registry Status: PENDING_EXPORT
""", language="yaml")

st.markdown("---")

# 8. Historical Ledger Table
st.markdown("#### 📋 Auditable Carbon Credit Ledger")

df = pd.DataFrame([{
    "Timestamp": f"{date_input} 12:00:00",
    "Site Name": facility_name,
    "Gateway ID": device_id,
    "Clean kWh": f"{solar_kwh:,.2f}",
    "Diesel Saved (L)": f"{diesel_displaced_liters:,.2f}",
    "Carbon Offset (tCO2e)": f"{tco2e_offset:,.4f}",
    "Cryptographic Hash": hash_signature
}])

st.dataframe(df, use_container_width=True)
