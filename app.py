import streamlit as st
import hashlib
import datetime
import pandas as pd

st.set_page_config(page_title="Earth Aura dMRV Engine", layout="wide")

st.title("Earth Aura dMRV Platform")
st.subheader("Solar Telemetry & Carbon Offset Verification")

st.markdown("---")

# Input Section: Mini-grid / C&I Telemetry
col1, col2 = st.columns(2)

with col1:
    ("Facility / Site Name", value="")
    solar_kwh = st.number_input("Solar Energy Generated (kWh)", min_value=0.0, value=1250.0, step=10.0)

with col2:
    date_input = st.date_input("Telemetry Date", datetime.date.today())
    device_id = st.text_input("IoT Meter ID", value="METER-001")
# Core dMRV Calculations
diesel_displaced_liters = solar_kwh * 0.25
tco2e_offset = solar_kwh * 0.00067

# SHA-256 Cryptographic Hash Generation
raw_data = f"{facility_name}|{date_input}|{device_id}|{solar_kwh}|{tco2e_offset}"
hash_signature = hashlib.sha256(raw_data.encode()).hexdigest()

st.markdown("---")

# Dashboard Visual Metrics
st.markdown("### Telemetry & Impact Summary")
m1, m2, m3 = st.columns(3)
m1.metric("Solar Generation", f"{solar_kwh:,.2f} kWh")
m2.metric("Diesel Displaced", f"{diesel_displaced_liters:,.2f} L")
m3.metric("Carbon Offset", f"{tco2e_offset:,.4f} tCO2e")

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
