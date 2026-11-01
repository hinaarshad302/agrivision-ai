
import streamlit as st

st.set_page_config(page_title="Farm Management", page_icon="🚜", layout="wide")

st.title("🚜 Farm Management")
st.write("Add and manage basic information about your farm.")

st.info("Farm information is currently temporary and is not saved to a database.")

with st.form("farm_form"):
    st.subheader("Add Farm Details")

    farm_name = st.text_input("Farm Name")

    location = st.text_input(
        "Farm Location",
        placeholder="Example: Rahim Yar Khan, Pakistan"
    )

    farm_size = st.number_input(
        "Farm Size (Acres)",
        min_value=0.0,
        step=0.5
    )

    crop = st.selectbox(
        "Main Crop",
        ["Tomato", "Potato", "Corn", "Apple"]
    )

    soil_type = st.selectbox(
        "Soil Type",
        ["Sandy", "Clay", "Silt", "Loamy", "Unknown"]
    )

    submitted = st.form_submit_button("Submit Farm Details")

if submitted:
    if not farm_name.strip() or not location.strip() or farm_size <= 0:
        st.error("Please enter a farm name, location and valid farm size.")
    else:
        st.success("Farm details submitted successfully!")
        st.subheader("Farm Summary")
        st.write(f"**Farm Name:** {farm_name}")
        st.write(f"**Location:** {location}")
        st.write(f"**Farm Size:** {farm_size} acres")
        st.write(f"**Main Crop:** {crop}")
        st.write(f"**Soil Type:** {soil_type}")

st.divider()

st.caption("AgriVision AI | Farm Management")
