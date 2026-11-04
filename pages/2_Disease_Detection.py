
"""
AgriVision AI
Crop Disease Detection Page
"""

import streamlit as st
from PIL import Image, UnidentifiedImageError

from config import (
    SUPPORTED_CROPS,
    IMAGE_TYPES,
    MAX_IMAGE_SIZE_MB,
    PREDICTION_ENABLED
)

from services.prediction_service import predict_disease


# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Disease Detection | AgriVision AI",
    page_icon="🔬",
    layout="wide"
)


# --------------------------------------------------
# 2. PAGE HEADER
# --------------------------------------------------

st.title("🔬 Crop Disease Detection")

st.write(
    "Upload a crop leaf image to analyze its possible disease "
    "using AgriVision AI."
)

st.info(
    "Supported crops: Tomato, Potato, Corn and Apple."
)


# --------------------------------------------------
# 3. CROP SELECTION
# --------------------------------------------------

crop = st.selectbox(
    "Select the crop",
    SUPPORTED_CROPS
)


# --------------------------------------------------
# 4. IMAGE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload crop leaf image",
    type=IMAGE_TYPES,
    help=f"Maximum image size: {MAX_IMAGE_SIZE_MB} MB"
)


if uploaded_file is not None:

    file_size_mb = uploaded_file.size / (1024 * 1024)

    if file_size_mb > MAX_IMAGE_SIZE_MB:

        st.error(
            f"Image size must not exceed {MAX_IMAGE_SIZE_MB} MB."
        )

    else:

        try:

            image = Image.open(uploaded_file).convert("RGB")

            # ----------------------------------------
            # 5. IMAGE PREVIEW
            # ----------------------------------------

            st.subheader("Uploaded Leaf Image")

            col1, col2 = st.columns([1, 1])

            with col1:

                st.image(
                    image,
                    caption=f"Selected crop: {crop}",
                    use_container_width=True
                )

            with col2:

                st.markdown("### Image Information")

                st.write(f"**Selected Crop:** {crop}")

                st.write(
                    f"**Image Dimensions:** "
                    f"{image.width} × {image.height} pixels"
                )

                st.write(
                    f"**File Size:** {file_size_mb:.2f} MB"
                )

                st.success("Image uploaded successfully.")

            st.divider()

            # ----------------------------------------
            # 6. MODEL STATUS
            # ----------------------------------------

            if not PREDICTION_ENABLED:

                st.warning(
                    "The AI prediction feature is currently disabled. "
                    "It will be enabled after successful model deployment "
                    "and testing."
                )

            else:

                # ------------------------------------
                # 7. RUN AI PREDICTION
                # ------------------------------------

                if st.button(
                    "🔍 Analyze Leaf Image",
                    type="primary",
                    use_container_width=True
                ):

                    with st.spinner(
                        "AgriVision AI is analyzing your leaf image..."
                    ):

                        result = predict_disease(image)

                    if result["status"] == "success":

                        predicted_crop = result["crop"]
                        predicted_disease = result["disease"]
                        confidence = result["confidence"]

                        # Do not display a disease result for a crop mismatch.
                        if predicted_crop.casefold() != crop.casefold():

                            st.warning(
                                f"The selected crop is {crop}, but the "
                                f"model predicted {predicted_crop}. "
                                "No disease result is shown because the crop "
                                "selection and model prediction do not match. "
                                "Please verify the uploaded image and selected crop."
                            )

                        else:

                            # --------------------------------
                            # 9. DISPLAY VERIFIED CROP MATCH
                            # --------------------------------

                            st.subheader("🤖 AI Prediction Result")

                            result_col1, result_col2 = st.columns(2)

                            with result_col1:
                                st.metric("Predicted Crop", predicted_crop)

                            with result_col2:
                                st.metric(
                                    "Model Confidence",
                                    f"{confidence * 100:.2f}%"
                                )

                            st.success(
                                f"Predicted Class: "
                                f"{predicted_disease.replace('_', ' ')}"
                            )

                            # --------------------------------
                            # 10. TOP 3 PREDICTIONS
                            # --------------------------------

                            st.subheader("Top 3 Model Predictions")

                            for index, prediction in enumerate(
                                result["top_predictions"],
                                start=1
                            ):
                                st.write(
                                    f"**{index}. "
                                    f"{prediction['crop']} — "
                                    f"{prediction['disease'].replace('_', ' ')}**"
                                )
                                st.progress(prediction["confidence"])
                                st.caption(
                                    f"Confidence: "
                                    f"{prediction['confidence'] * 100:.2f}%"
                                )

                            # --------------------------------
                            # 11. IMPORTANT NOTICE
                            # --------------------------------

                            st.info(
                                "This is an AI-generated prediction, not a "
                                "confirmed agricultural diagnosis. Image quality "
                                "and real-world field conditions can affect results. "
                                "Consult an agricultural expert before treatment."
                            )

                    else:

                        st.error(
                            result.get(
                                "message",
                                "Prediction could not be completed."
                            )
                        )

        except (UnidentifiedImageError, OSError, ValueError):

            st.error(
                "Invalid image. Please upload a valid JPG, JPEG or PNG file."
            )

        except Exception as error:

            st.error(
                "An unexpected error occurred while processing the image."
            )

            print(f"Disease detection page error: {error}")
