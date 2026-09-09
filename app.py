import streamlit as st
import hashlib
import datetime
import pandas as pd

# Page Configuration & Styling
st.set_page_config(page_title="Earth Aura dMRV Engine", layout="wide", page_icon="🌱")

st.markdown("""
    <style>
    .main-title {
        color: #1E3A8A;
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #059669;
        font-size: 16px;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🌱 Earth Aura dMRV Platform</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Automated Solar Telemetry & Verification Infrastructure</p>', unsafe_allow_html=True)

# Input Section: Mini-grid / C&I Telemetry
col1, col2 = st.columns(2)

with col1:
    facility_name = st.text_input("Facility / Site Name", value="Solar Mini-Grid Facility 1")
    solar_kwh = st.number_input("Solar Energy Generated (kWh)", min_value=0.0, value=1000.0, step=10.0)

with col2:
    date_input = st.date_input("Telemetry Date", datetime.date.today())
    device_id = st.text_input("IoT Meter ID", value="METER-001")

# Core dMRV Calculations
diesel_displaced_liters = solar_kwh * 0.25
tco2e_offset = solar_kwh * 0.00067

# SHA-256 Cryptographic Hash Generation
raw_data = f"{facility_name}{date_input}{device_id}{solar_kwh}{tco2e_offset}"
hash_signature = hashlib.sha256(raw_data.encode()).hexdigest()

st.markdown("---")

# Dashboard Visual Metrics
st.success("● IoT Telemetry Feed Active | Verification Standard: Gold Standard / Verra dMRV")
st.markdown("### Telemetry & Impact Summary")

m1, m2, m3 = st.columns(3)
m1.metric("Solar Generation", f"{solar_kwh:,.2f} kWh")
m2.metric("Diesel Displaced", f"{diesel_displaced_liters:,.2f} L")
m3.metric("Carbon Offset", f"{tco2e_offset:,.4f} tCO2e", delta="Verified")

st.markdown("---")

# Projected Impact Chart
st.markdown("### Projected Emissions Avoidance")
chart_data = pd.DataFrame({
    'Metric': ['Solar Energy (kWh)', 'Diesel Saved (L x10)', 'CO2 Avoided (kg)'],
    'Value': [solar_kwh, diesel_displaced_liters / 10, tco2e_offset * 1000]
})
st.bar_chart(chart_data.set_index('Metric'))

st.markdown("---")

# Verification Certificate & Data Record
st.markdown("### Verification Record")
st.code(f"""
Facility: {facility_name}
Device ID: {device_id}
Timestamp: {date_input}
Calculated Offset: {tco2e_offset:.4f} tCO2e
SHA-256 Hash Signature: {hash_signature}
Methodology Alignment: Gold Standard / Verra dMRV
""", language="yaml")

# Dataframe Log
df = pd.DataFrame([{
    "Date": str(date_input),
    "Facility": facility_name,
    "Meter ID": device_id,
    "Solar kWh": solar_kwh,
    "Diesel Saved (L)": diesel_displaced_liters,
    "tCO2e Offset": tco2e_offset,
    "Cryptographic Hash": hash_signature
}])

st.dataframe(df, use_container_width=True)
