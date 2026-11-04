
"""
AgriVision AI
Professional Smart Agriculture Intelligence Dashboard
"""

import streamlit as st
from pathlib import Path

from config import (
    APP_NAME,
    APP_TAGLINE,
    APP_VERSION,
    SUPPORTED_CROPS,
    MODEL_NAME,
    MODEL_TRAINED,
    PREDICTION_ENABLED
)


# ==================================================
# 1. PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title=f"{APP_NAME} | Smart Agriculture",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# 2. LOAD PROFESSIONAL DESIGN THEME
# ==================================================

CSS_PATH = Path(__file__).parent / "assets" / "style.css"

if CSS_PATH.exists():

    with open(CSS_PATH, "r", encoding="utf-8") as css_file:
        css = css_file.read()

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

    st.markdown(
        """
        <div style="padding: 10px 0 20px 0;">
            <h2 style="color:#16794b; margin-bottom:0;">
                🌱 AgriVision AI
            </h2>
            <p style="color:#718078; font-size:13px;">
                Smart Agriculture Intelligence
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### PROJECT INFORMATION")

    st.write(f"**Version:** {APP_VERSION}")

    st.write(f"**AI Architecture:** {MODEL_NAME}")

    st.write(
        f"**Model Status:** "
        f"{'Trained' if MODEL_TRAINED else 'Not Trained'}"
    )

    st.divider()

    st.markdown("### CURRENTLY TRAINED CROPS")

    for crop in SUPPORTED_CROPS:
        st.markdown(
            f"🌿 **{crop}**"
        )

    st.divider()

    st.caption(
        "Additional crop categories will be introduced "
        "after dataset preparation and model validation."
    )


# ==================================================
# 4. MAIN HERO SECTION
# ==================================================

st.markdown(
    f"""
    <div style="
        background: linear-gradient(120deg, #e5f4e9, #f7fbf7);
        border: 1px solid #d9eade;
        border-radius: 18px;
        padding: 30px;
        margin-bottom: 25px;
    ">

        <p style="
            color:#16794b;
            font-size:14px;
            font-weight:700;
            letter-spacing:2px;
            margin-bottom:8px;
        ">
            SMART AGRICULTURE PLATFORM
        </p>

        <h1 style="
            color:#145c39;
            font-size:38px;
            font-weight:800;
            margin:0;
        ">
            🌱 {APP_NAME}
        </h1>

        <p style="
            color:#52665a;
            font-size:17px;
            margin-top:12px;
            margin-bottom:15px;
        ">
            {APP_TAGLINE}
        </p>

        <p style="
            color:#52665a;
            font-size:14px;
            margin-bottom:0;
        ">
            Explore AI-powered crop health screening through
            intelligent image classification.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# 5. DASHBOARD OVERVIEW
# ==================================================

st.subheader("📊 Platform Overview")

metric1, metric2, metric3 = st.columns(3)

with metric1:

    st.metric(
        label="Currently Supported Crops",
        value=len(SUPPORTED_CROPS)
    )

with metric2:

    st.metric(
        label="AI Model",
        value="Trained" if MODEL_TRAINED else "Not Trained"
    )

with metric3:

    st.metric(
        label="Prediction System",
        value="Active" if PREDICTION_ENABLED else "Disabled"
    )


st.divider()


# ==================================================
# 6. CURRENTLY SUPPORTED CROPS
# ==================================================

st.subheader("🌿 Currently Supported Crops")

st.caption(
    "The current trained AI model supports the following "
    "four crop categories."
)

crop_columns = st.columns(len(SUPPORTED_CROPS))

crop_descriptions = {
    "Tomato": "Tomato leaf health classification",
    "Potato": "Potato leaf health classification",
    "Corn": "Corn leaf health classification",
    "Apple": "Apple leaf health classification"
}

for column, crop in zip(crop_columns, SUPPORTED_CROPS):

    with column:

        description = crop_descriptions.get(
            crop,
            "Crop classification"
        )

        st.markdown(
            f"""
            <div style="
                background:#ffffff;
                border:1px solid #e0ebe3;
                border-top:4px solid #23834e;
                border-radius:14px;
                padding:20px 15px;
                min-height:145px;
                box-shadow:0 3px 12px rgba(20,70,40,0.04);
            ">

                <h3 style="
                    color:#17653d;
                    font-size:20px;
                    margin:0 0 12px 0;
                ">
                    🌱 {crop}
                </h3>

                <p style="
                    color:#718078;
                    font-size:13px;
                    margin:0;
                ">
                    {description}
                </p>

                <p style="
                    color:#23834e;
                    font-size:12px;
                    font-weight:600;
                    margin-top:14px;
                ">
                    AI MODEL AVAILABLE
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ==================================================
# 7. FUTURE CROP EXPANSION
# ==================================================

st.subheader("🚜 Expanding Agricultural Coverage")

st.write(
    "Our long-term vision is to expand AgriVision AI "
    "to additional agricultural crops."
)

future_crops = [
    ("🌾", "Wheat", "Gandum"),
    ("☁️", "Cotton", "Kapas"),
    ("🌾", "Rice", "Chawal"),
    ("🎋", "Sugarcane", "Ganna"),
    ("🥭", "Mango", "Aam"),
    ("🌻", "Sunflower", "Suraj Mukhi")
]

future_columns = st.columns(3)

for index, (emoji, crop_name, local_name) in enumerate(future_crops):

    with future_columns[index % 3]:

        st.markdown(
            f"""
            <div style="
                background:#f0f6f1;
                border:1px solid #e0ebe3;
                border-radius:12px;
                padding:15px;
                margin-bottom:12px;
            ">

                <h4 style="
                    color:#17653d;
                    margin:0 0 5px 0;
                ">
                    {emoji} {crop_name}
                </h4>

                <p style="
                    color:#718078;
                    font-size:13px;
                    margin:0;
                ">
                    {local_name} — Planned expansion
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

st.info(
    "Additional crops will become available for AI disease "
    "prediction only after suitable datasets, model training, "
    "and evaluation."
)


# ==================================================
# 8. ARTIFICIAL INTELLIGENCE STATUS
# ==================================================

st.subheader("🤖 Artificial Intelligence Status")

if MODEL_TRAINED and PREDICTION_ENABLED:

    st.success(
        "The trained AI model is enabled for predictions."
    )

elif MODEL_TRAINED:

    st.warning(
        "Model training and evaluation are complete. "
        "Prediction functionality is currently disabled."
    )

else:

    st.error(
        "The AI model has not been trained yet."
    )


# ==================================================
# 9. HOW THE PLATFORM WORKS
# ==================================================

st.subheader("⚙️ How AgriVision AI Works")

workflow_steps = [
    ("01", "Upload Image", "Upload a crop leaf image."),
    ("02", "Image Processing", "Validate and prepare the image."),
    ("03", "AI Analysis", "The trained model analyzes the leaf."),
    ("04", "Prediction", "View the predicted crop and disease."),
    ("05", "Review Result", "Check confidence and alternative predictions.")
]

workflow_columns = st.columns(5)

for column, (number, title, description) in zip(
    workflow_columns,
    workflow_steps
):

    with column:

        st.markdown(
            f"""
            <div style="
                background:#ffffff;
                border:1px solid #e0ebe3;
                border-radius:12px;
                padding:15px;
                min-height:155px;
            ">

                <p style="
                    color:#23834e;
                    font-size:13px;
                    font-weight:800;
                ">
                    STEP {number}
                </p>

                <h4 style="
                    color:#173d29;
                    font-size:15px;
                ">
                    {title}
                </h4>

                <p style="
                    color:#718078;
                    font-size:12px;
                ">
                    {description}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ==================================================
# 10. MODEL PERFORMANCE INFORMATION
# ==================================================

st.subheader("📈 Model Evaluation")

performance_col1, performance_col2 = st.columns(2)

with performance_col1:

    st.metric(
        label="Test Accuracy",
        value="95.00%"
    )

with performance_col2:

    st.metric(
        label="Test Dataset",
        value="4,101 Images"
    )

st.caption(
    "Reported results are from the selected PlantVillage "
    "test dataset. Real-world field performance has not "
    "yet been independently validated."
)


# ==================================================
# 11. RESPONSIBLE AI NOTICE
# ==================================================

st.divider()

st.info(
    "AgriVision AI provides AI-generated crop-health screening "
    "results for educational and decision-support purposes. "
    "Predictions are not confirmed agricultural diagnoses. "
    "Consult a qualified agricultural expert before treatment."
)


# ==================================================
# 12. FOOTER
# ==================================================

st.markdown(
    f"""
    <div style="
        text-align:center;
        padding:25px 10px;
        border-top:1px solid #e0ebe3;
        margin-top:25px;
    ">

        <h4 style="color:#16794b; margin-bottom:5px;">
            🌱 {APP_NAME}
        </h4>

        <p style="
            color:#718078;
            font-size:12px;
            margin:0;
        ">
            Healthy Crops • Prosperous Farmers • Food Security
        </p>

        <p style="
            color:#9aa69e;
            font-size:11px;
            margin-top:10px;
        ">
            Version {APP_VERSION}
        </p>

    </div>
    """,
    unsafe_allow_html=True
)
