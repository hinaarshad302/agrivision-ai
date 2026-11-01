
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Scan History", page_icon="📋", layout="wide")

st.title("📋 Scan History")
st.write("Review previous crop image scans and their results.")

scan_data = [
    {
        "Scan ID": "SCAN-001",
        "Crop": "Tomato",
        "Prediction": "Early Blight",
        "Confidence": "92%",
        "Status": "Demo Data"
    },
    {
        "Scan ID": "SCAN-002",
        "Crop": "Potato",
        "Prediction": "Late Blight",
        "Confidence": "88%",
        "Status": "Demo Data"
    },
    {
        "Scan ID": "SCAN-003",
        "Crop": "Apple",
        "Prediction": "Apple Scab",
        "Confidence": "95%",
        "Status": "Demo Data"
    }
]

st.info("These are sample records, not actual AI predictions.")

df = pd.DataFrame(scan_data)

col1, col2 = st.columns(2)

with col1:
    st.metric("Sample Scans", len(df))

with col2:
    st.metric("Crop Categories", df["Crop"].nunique())

st.subheader("Previous Scans")
st.dataframe(df, use_container_width=True, hide_index=True)

selected_scan = st.selectbox(
    "Select a Scan",
    df["Scan ID"].tolist()
)

record = df[df["Scan ID"] == selected_scan].iloc[0]

st.subheader("Scan Details")
st.write(f"**Scan ID:** {record['Scan ID']}")
st.write(f"**Crop:** {record['Crop']}")
st.write(f"**Sample Prediction:** {record['Prediction']}")
st.write(f"**Sample Confidence:** {record['Confidence']}")
st.warning("Demo information only. No real scan history is saved yet.")

st.caption("AgriVision AI | Scan History")
