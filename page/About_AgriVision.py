
import streamlit as st

st.title("🌱 About AgriVision AI")

st.subheader("Smart Agriculture Intelligence Platform")

st.write(
    """
    AgriVision AI is an Artificial Intelligence and Machine Learning
    based agriculture project designed to help farmers understand
    possible crop diseases through leaf image analysis.

    Farmers will be able to upload a crop leaf image, and the AI model
    will analyze the image and predict a possible disease category.
    """
)

st.divider()

st.header("🎯 Project Objectives")

st.markdown(
    """
    - Identify possible crop diseases using leaf images.
    - Use Machine Learning and Deep Learning techniques.
    - Display prediction results and confidence scores.
    - Provide educational crop disease information.
    - Support farmers in understanding crop health.
    """
)

st.divider()

st.header("🌿 Initial Supported Crops")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🍅 Tomato")

with col2:
    st.info("🥔 Potato")

with col3:
    st.info("🌽 Corn")

with col4:
    st.info("🍎 Apple")

st.divider()

st.header("🤖 Technologies Used")

technologies = {
    "Python": "Main programming language",
    "Streamlit": "Web application interface",
    "TensorFlow / Keras": "Deep Learning model development",
    "MobileNetV2": "Planned image classification model",
    "Google Colab": "Model training environment",
    "GitHub": "Project code management",
    "Supabase": "Planned database service"
}

for technology, description in technologies.items():
    st.markdown(f"**{technology}:** {description}")

st.divider()

st.header("⚙️ How the System Will Work")

st.markdown(
    """
    **Step 1 — Image Upload**

    Farmer uploads a crop leaf image.

    **Step 2 — Image Processing**

    The application validates and prepares the image.

    **Step 3 — AI Analysis**

    The trained Deep Learning model analyzes the image.

    **Step 4 — Prediction**

    The system displays a possible disease category
    and its confidence score.

    **Step 5 — Information**

    The application provides relevant educational
    information about the predicted category.
    """
)

st.divider()

st.header("⚠️ Important Disclaimer")

st.warning(
    """
    AgriVision AI is a decision-support and educational project.
    Its predictions are not confirmed agricultural diagnoses.
    Results should be verified by an agriculture expert.
    The system does not replace professional agricultural advice.
    """
)

st.caption("AgriVision AI | Smart Agriculture Intelligence Platform")
