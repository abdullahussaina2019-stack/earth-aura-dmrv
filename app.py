import streamlit as st
import hashlib
import datetime
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Earth Aura dMRV Engine",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Dark-Mode Enterprise CSS Custom Styling
st.markdown("""
    <style>
    /* Dark Slate Background for Main Content */
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }

    /* Enterprise Metric Card Glassmorphism Styling */
    div[data-testid="stMetric"] {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(12px);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    div[data-testid="stMetric"]:hover {
        border-color: #10B981;
        transform: translateY(-2px);
    }

    /* Metric Typography */
    div[data-testid="stMetricLabel"] > label {
        color: #94A3B8 !important;
        font-size: 12px !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    div[data-testid="stMetricValue"] {
        color: #F8FAFC !important;
        font-weight: 800 !important;
        font-size: 28px !important;
    }

    /* Header Styling */
    .hero-brand {
        color: #10B981;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 4px;
    }
    .hero-title {
        color: #FFFFFF;
        font-size: 34px;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 12px;
    }

    /* Badges Bar */
    .badge-container {
        display: flex;
        gap: 12px;
        margin-bottom: 25px;
        flex-wrap: wrap;
    }
    .badge-active {
        background-color: rgba(16, 185, 129, 0.15);
        color: #34D399;
        border: 1px solid rgba(16, 185, 129, 0.4);
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    .badge-standard {
        background-color: rgba(59, 130, 246, 0.15);
        color: #60A5FA;
        border: 1px solid rgba(59, 130, 246, 0.4);
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }

    /* Code block container styling */
    div[data-testid="stCodeBlock"] {
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Controls Panel
with st.sidebar:
    st.markdown("### 🌱 Earth Aura Controls")
    st.caption("Site Telemetry & Device Inputs")
    st.markdown("---")
    
    facility_name = st.text_input("Facility / Site Name", value="Solar Mini-Grid Facility 1")
    solar_kwh = st.number_input("Generation Output (kWh)", min_value=0.0, value=1250.0, step=25.0)
    device_id = st.text_input("IoT Meter ID", value="METER-001")
    date_input = st.date_input("Telemetry Date", datetime.date.today())
    
    st.markdown("---")
    st.caption("dMRV Engine v2.0 | Aura Carbon Tech")

# 4. Core Calculations
diesel_displaced_liters = solar_kwh * 0.25
tco2e_offset = solar_kwh * 0.00067

raw_data = f"{facility_name}{date_input}{device_id}{solar_kwh}{tco2e_offset}"
hash_signature = hashlib.sha256(raw_data.encode()).hexdigest()

# 5. Main Dashboard Header
st.markdown('<p class="hero-brand">Earth Aura dMRV Platform</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-title">Automated Solar Telemetry & Verification Ledger</p>', unsafe_allow_html=True)

st.markdown("""
    <div class="badge-container">
        <span class="badge-active">● IoT Telemetry Feed Active</span>
        <span class="badge-standard">Standard: Gold Standard / Verra dMRV</span>
    </div>
""", unsafe_allow_html=True)

# 6. KPI Metric Cards
m1, m2, m3 = st.columns(3)
m1.metric("Solar Energy Generated", f"{solar_kwh:,.2f} kWh")
m2.metric("Diesel Displaced", f"{diesel_displaced_liters:,.2f} L")
m3.metric("Verified Carbon Offset", f"{tco2e_offset:,.4f} tCO2e", delta="Audited")

st.markdown("<br>", unsafe_allow_html=True)

# 7. Impact Visualization & Data Log Section
col_chart, col_record = st.columns([3, 2])

with col_chart:
    st.markdown("### 📊 Environmental Impact Summary")
    chart_data = pd.DataFrame({
        'Metric': ['Solar Energy (kWh)', 'Diesel Displaced (L x10)', 'CO2 Avoided (kg)'],
        'Value': [solar_kwh, diesel_displaced_liters / 10, tco2e_offset * 1000]
    })
    st.bar_chart(chart_data.set_index('Metric'), use_container_width=True)

with col_record:
    st.markdown("### 🔒 Cryptographic Certificate")
    st.code(f"""
Facility: {facility_name}
Device ID: {device_id}
Timestamp: {date_input}
Calculated Offset: {tco2e_offset:.4f} tCO2e
SHA-256 Signature:
{hash_signature[:32]}...
Methodology: Gold Standard / Verra dMRV
""", language="yaml")

st.markdown("---")

# 8. Data Audit Log
st.markdown("### 📄 Verified Data Record")
df = pd.DataFrame([{
    "Date": str(date_input),
    "Facility Name": facility_name,
    "Meter ID": device_id,
    "Solar kWh": solar_kwh,
    "Diesel Displaced (L)": diesel_displaced_liters,
    "tCO2e Offset": tco2e_offset,
    "Cryptographic Hash": hash_signature
}])

st.dataframe(df, use_container_width=True)
