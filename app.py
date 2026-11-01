
import streamlit as st

# Import project settings from config.py
from config import (
    APP_NAME,
    APP_TAGLINE,
    APP_VERSION,
    SUPPORTED_CROPS,
    MODEL_NAME,
    MODEL_TRAINED,
    PREDICTION_ENABLED
)


# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# 2. CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 40px;
        font-weight: 800;
        color: #237A45;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #64748b;
        margin-bottom: 25px;
    }

    .info-card {
        background-color: #f0f8f1;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #237A45;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# 3. SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🌱 AgriVision AI")

    st.caption("Smart Agriculture Intelligence")

    st.divider()

    st.markdown("### Project Information")

    st.write(f"Version: {APP_VERSION}")

    st.write(f"AI Model: {MODEL_NAME}")

    st.divider()

    st.markdown("### Initial Crop Groups")

    for crop in SUPPORTED_CROPS:
        st.write(f"🌿 {crop}")


# --------------------------------------------------
# 4. MAIN DASHBOARD HEADER
# --------------------------------------------------

st.markdown(
    f'<div class="main-title">🌱 {APP_NAME}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="subtitle">{APP_TAGLINE}</div>',
    unsafe_allow_html=True
)

st.write(
    """
    Welcome to AgriVision AI!

    Our goal is to help farmers explore crop health using
    Artificial Intelligence and Machine Learning.
    """
)


# --------------------------------------------------
# 5. PROJECT OVERVIEW
# --------------------------------------------------

st.subheader("📊 Project Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Supported Crops",
        value=len(SUPPORTED_CROPS)
    )

with col2:
    st.metric(
        label="AI Model",
        value="Trained" if MODEL_TRAINED else "Not Trained"
    )

with col3:
    st.metric(
        label="Prediction System",
        value="Enabled" if PREDICTION_ENABLED else "Disabled"
    )


# --------------------------------------------------
# 6. SUPPORTED CROPS
# --------------------------------------------------

st.subheader("🌿 Initial Supported Crops")

crop_columns = st.columns(len(SUPPORTED_CROPS))

for column, crop in zip(crop_columns, SUPPORTED_CROPS):

    with column:

        st.markdown(
            f"""
            <div class="info-card">
                <h4>🌱 {crop}</h4>
                <p>Planned crop category</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# --------------------------------------------------
# 7. AI MODEL STATUS
# --------------------------------------------------

st.subheader("🤖 Artificial Intelligence Status")

if MODEL_TRAINED and PREDICTION_ENABLED:

    st.success("AI model is configured for predictions.")

else:

    st.warning(
        "The AI model is not ready yet. "
        "Dataset preparation, training and evaluation are required."
    )


# --------------------------------------------------
# 8. PROJECT WORKFLOW
# --------------------------------------------------

st.subheader("⚙️ How AgriVision AI Will Work")

st.markdown(
    """
    **Step 1:** Farmer uploads a crop leaf image.

    **Step 2:** Application validates the uploaded image.

    **Step 3:** Trained AI model analyzes the image.

    **Step 4:** Application displays the predicted class and confidence.

    **Step 5:** Prediction record can be saved for future reference.
    """
)


# --------------------------------------------------
# 9. IMPORTANT NOTICE
# --------------------------------------------------

st.info(
    "AgriVision AI is an educational decision-support project. "
    "AI predictions are not confirmed agricultural diagnoses."
)


# --------------------------------------------------
# 10. FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    f"{APP_NAME} | Version {APP_VERSION}"
)

st.caption(
    "Smart Agriculture Intelligence Platform"
)
