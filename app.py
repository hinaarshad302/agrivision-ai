
import streamlit as st

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AgriVision AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# 2. PROJECT INFORMATION
# --------------------------------------------------

APP_NAME = "AgriVision AI"

SUPPORTED_CROPS = [
    "Tomato",
    "Potato",
    "Corn",
    "Apple"
]

# --------------------------------------------------
# 3. CUSTOM CSS DESIGN
# --------------------------------------------------

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
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
# 4. SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🌱 AgriVision AI")

    st.caption("Smart Agriculture Intelligence")

    st.divider()

    st.markdown("### Project Menu")

    st.write("🏠 Dashboard")
    st.write("🔬 Disease Detection")
    st.write("🌿 Crop Library")
    st.write("🚜 My Farms")
    st.write("🌦️ Weather Insights")
    st.write("🕘 Scan History")
    st.write("📊 Analytics")

    st.divider()

    st.caption("Version 1.0 — Development Stage")

# --------------------------------------------------
# 5. MAIN DASHBOARD
# --------------------------------------------------

st.markdown(
    f'<div class="main-title">🌱 {APP_NAME}</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-Powered Smart Agriculture Intelligence Platform'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    Welcome to AgriVision AI!

    Our goal is to help farmers explore crop health using
    Artificial Intelligence and Machine Learning.
    """
)

# --------------------------------------------------
# 6. PROJECT STATUS
# --------------------------------------------------

st.subheader("📊 Project Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Supported Crop Groups",
        value=len(SUPPORTED_CROPS)
    )

with col2:
    st.metric(
        label="AI Model Status",
        value="Not Trained"
    )

with col3:
    st.metric(
        label="Project Status",
        value="Development"
    )

# --------------------------------------------------
# 7. SUPPORTED CROPS
# --------------------------------------------------

st.subheader("🌿 Initial Supported Crops")

crop_columns = st.columns(4)

for column, crop in zip(crop_columns, SUPPORTED_CROPS):

    with column:
        st.markdown(
            f"""
            <div class="info-card">
                <h4>{crop}</h4>
                <p>Planned crop category</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# --------------------------------------------------
# 8. AI MODEL INFORMATION
# --------------------------------------------------

st.subheader("🤖 Artificial Intelligence Status")

st.warning(
    "The machine learning model has not been trained yet. "
    "Disease predictions will become available after dataset "
    "preparation, model training and evaluation."
)

# --------------------------------------------------
# 9. PROJECT WORKFLOW
# --------------------------------------------------

st.subheader("⚙️ How AgriVision AI Will Work")

st.markdown(
    """
    1. Farmer uploads a crop leaf image.
    2. The application validates the image.
    3. The trained AI model analyzes the image.
    4. The application displays the predicted class and confidence.
    5. The result can be saved for future reference.
    """
)

# --------------------------------------------------
# 10. FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "AgriVision AI | Smart Agriculture Intelligence Platform"
)

st.caption(
    "Educational decision-support system. "
    "AI predictions are not confirmed agricultural diagnoses."
)
