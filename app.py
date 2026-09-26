import streamlit as st

st.set_page_config(
    page_title="Weather AI Tracker",
    page_icon="🌦️",
    layout="wide"
)

st.title("🌦️ Weather AI Tracker")

st.write(
    "AI-Driven Spatio-Temporal Tracking of "
    "Extreme Weather Anomalies"
)

st.sidebar.header("Weather Controls")

event = st.sidebar.selectbox(
    "Select Weather Event",
    [
        "Cyclone",
        "Heatwave",
        "Heavy Rainfall",
        "Cold Wave"
    ]
)

threshold = st.sidebar.slider(
    "Anomaly Threshold",
    1.0,
    4.0,
    2.0
)

st.subheader("🌍 Weather Anomaly Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Weather Event", event)

with col2:
    st.metric("Anomaly Threshold", threshold)

with col3:
    st.metric("Status", "Monitoring")

st.subheader("📍 Anomaly Information")

st.write("Latitude: --")
st.write("Longitude: --")
st.write("Severity: --")
st.write("Forecast Window: 3–10 days")

st.info(
    "Weather AI Tracker prototype is ready. "
    "Data analysis and anomaly tracking will be added next."
)
