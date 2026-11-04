
import streamlit as st
from pathlib import Path

from config import (
    APP_NAME,
    APP_TAGLINE,
    APP_VERSION,
    SUPPORTED_CROPS,
    MODEL_NAME,
    MODEL_TRAINED,
    PREDICTION_ENABLED,
)

# ==================================================
# 1. PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title=f"{APP_NAME} | Smart Agriculture",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==================================================
# 2. LOAD PROFESSIONAL CSS THEME
# ==================================================

css_path = Path(__file__).parent / "assets" / "style.css"

if css_path.exists():
    css = css_path.read_text(encoding="utf-8")
    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )
else:
    st.warning("Professional theme file was not found.")

# ==================================================
# 3. SIDEBAR
# ==================================================

with st.sidebar:
    st.title("🌱 AgriVision AI")
    st.caption("Smart Agriculture Intelligence")

    st.divider()

    st.subheader("Project Information")

    st.write(f"**Version:** {APP_VERSION}")
    st.write(f"**AI Model:** {MODEL_NAME}")

    if MODEL_TRAINED:
        st.success("Model: Trained")
    else:
        st.warning("Model: Not Trained")

    st.divider()

    st.subheader("Currently Trained Crops")

    for crop in SUPPORTED_CROPS:
        st.write(f"🌿 {crop}")

    st.divider()

    st.caption(
        "Additional crops will be supported after "
        "dataset preparation and model validation."
    )

# ==================================================
# 4. DASHBOARD HEADER
# ==================================================

st.markdown("# 🌱 AgriVision AI")

st.markdown(
    f"### {APP_TAGLINE}"
)

st.write(
    "An AI-powered agriculture platform designed to help "
    "farmers explore crop health through image-based analysis."
)

st.divider()

# ==================================================
# 5. PLATFORM OVERVIEW
# ==================================================

st.subheader("📊 Platform Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Currently Supported Crops",
        value=len(SUPPORTED_CROPS),
    )

with col2:
    st.metric(
        label="AI Model",
        value="Trained" if MODEL_TRAINED else "Not Trained",
    )

with col3:
    st.metric(
        label="Prediction System",
        value="Enabled" if PREDICTION_ENABLED else "Disabled",
    )

# ==================================================
# 6. CURRENTLY SUPPORTED CROPS
# ==================================================

st.divider()
st.subheader("🌿 Currently Supported Crops")

st.caption(
    "These crops are included in the currently trained "
    "21-class AI model."
)

crop_descriptions = {
    "Apple": "Apple leaf disease classification",
    "Tomato": "Tomato leaf disease classification",
    "Potato": "Potato leaf disease classification",
    "Corn": "Maize leaf disease classification",
}

crop_columns = st.columns(4)

for index, crop in enumerate(SUPPORTED_CROPS):
    with crop_columns[index % 4]:
        with st.container(border=True):
            st.markdown(f"### 🌱 {crop}")
            st.caption(
                crop_descriptions.get(
                    crop,
                    "Supported crop category"
                )
            )
            st.success("AI Model Available")

# ==================================================
# 7. FUTURE CROP EXPANSION
# ==================================================

st.divider()
st.subheader("🚜 Future Crop Expansion")

st.caption(
    "These crops are planned for future development. "
    "Disease prediction is not available for them yet."
)

future_crops = [
    ("Wheat", "Gandum"),
    ("Cotton", "Kapas"),
    ("Rice", "Chawal"),
    ("Sugarcane", "Ganna"),
    ("Mango", "Aam"),
    ("Sunflower", "Suraj Mukhi"),
]

future_columns = st.columns(3)

for index, (crop, local_name) in enumerate(future_crops):
    with future_columns[index % 3]:
        with st.container(border=True):
            st.markdown(f"### 🌾 {crop}")
            st.caption(local_name)
            st.warning("Coming Soon")

# ==================================================
# 8. AI MODEL STATUS
# ==================================================

st.divider()
st.subheader("🤖 Artificial Intelligence Status")

if MODEL_TRAINED and PREDICTION_ENABLED:
    st.success(
        "The trained AI model is enabled for predictions."
    )
elif MODEL_TRAINED:
    st.warning(
        "The AI model is trained, but prediction functionality "
        "is currently disabled."
    )
else:
    st.error("The AI model has not been trained yet.")

st.info(
    "Current model coverage is limited to the four trained "
    "crop categories. Other crops require separate dataset "
    "preparation, training and evaluation."
)

# ==================================================
# 9. PROJECT WORKFLOW
# ==================================================

st.divider()
st.subheader("⚙️ How AgriVision AI Works")

workflow_steps = [
    ("01", "Upload Image", "Upload a crop leaf image."),
    ("02", "Image Processing", "Validate and prepare the image."),
    ("03", "AI Analysis", "The trained model analyzes the leaf."),
    ("04", "Prediction", "View the predicted crop and disease."),
    ("05", "Review Result", "Check confidence and alternatives."),
]

workflow_columns = st.columns(5)

for column, (number, title, description) in zip(
    workflow_columns,
    workflow_steps
):
    with column:
        with st.container(border=True):
            st.markdown(f"**STEP {number}**")
            st.markdown(f"#### {title}")
            st.caption(description)

# ==================================================
# 10. MODEL EVALUATION
# ==================================================

st.divider()
st.subheader("📈 Model Evaluation")

performance_col1, performance_col2 = st.columns(2)

with performance_col1:
    st.metric(
        label="Test Accuracy",
        value="95.00%",
    )
    st.caption("Held-out PlantVillage test dataset")

with performance_col2:
    st.metric(
        label="Test Images",
        value="4,101",
    )
    st.caption("Images evaluated")

st.caption(
    "Reported results are from the selected PlantVillage "
    "test dataset. Real-world field performance has not yet "
    "been independently validated."
)

# ==================================================
# 11. RESPONSIBLE AI NOTICE
# ==================================================

st.divider()

st.info(
    "AgriVision AI provides AI-generated crop-health screening "
    "for educational and decision-support purposes. Predictions "
    "are not confirmed agricultural diagnoses. Consult a "
    "qualified agricultural expert before treatment."
)

# ==================================================
# 12. FOOTER
# ==================================================

st.divider()

st.markdown(
    f"### 🌱 {APP_NAME}"
)

st.caption(
    "Healthy Crops • Prosperous Farmers • Food Security"
)

st.caption(
    f"Version {APP_VERSION} | Smart Agriculture Intelligence Platform"
)
