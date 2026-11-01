
import streamlit as st
from PIL import Image
from config import SUPPORTED_CROPS, IMAGE_TYPES, MAX_IMAGE_SIZE_MB

st.set_page_config(page_title="Disease Detection", page_icon="🔬", layout="wide")

st.title("🔬 Crop Disease Detection")
st.write("Upload a crop leaf image for AI-based analysis.")

st.info(
    "AI prediction is not available yet. "
    "The trained model will be connected in a later development stage."
)

crop = st.selectbox("Select Crop", SUPPORTED_CROPS)

uploaded_file = st.file_uploader(
    "Upload Leaf Image",
    type=IMAGE_TYPES
)

if uploaded_file:
    file_size_mb = uploaded_file.size / (1024 * 1024)

    if file_size_mb > MAX_IMAGE_SIZE_MB:
        st.error(f"Image size must not exceed {MAX_IMAGE_SIZE_MB} MB.")
    else:
        try:
            image = Image.open(uploaded_file).convert("RGB")

            st.subheader("Image Preview")
            st.image(image, caption=f"Selected Crop: {crop}", width=400)

            st.success("Image uploaded and validated successfully.")

            st.write(f"**Selected Crop:** {crop}")
            st.write(f"**Image Size:** {image.size[0]} × {image.size[1]} pixels")
            st.write(f"**File Size:** {file_size_mb:.2f} MB")

            st.warning(
                "Disease prediction will become available "
                "after the AI model is trained and connected."
            )

        except Exception:
            st.error("Invalid image. Please upload a valid JPG or PNG file.")
