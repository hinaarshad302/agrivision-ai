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
    "Upload a clear crop leaf image and enter its crop name. "
    "AgriVision AI will check whether the current disease model "
    "supports that crop."
)

st.info(
    "You can upload an image of any crop. Current disease prediction "
    "is available only for: " + ", ".join(SUPPORTED_CROPS) + ". "
    "Other crops can be uploaded, but disease diagnosis is not enabled "
    "for them yet."
)


# --------------------------------------------------
# 3. CROP NAME INPUT
# --------------------------------------------------

crop_name = st.text_input(
    "Enter crop name",
    placeholder="e.g. Tomato, Wheat, Rice, Cotton, Mango",
    help=(
        "Enter the crop shown in the image. You may use a common English "
        "name or a supported local name such as Tamatar, Aloo or Makai."
    )
).strip()


# --------------------------------------------------
# 4. IMAGE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload any crop leaf image",
    type=IMAGE_TYPES,
    help=f"Accepted formats: JPG, JPEG, PNG. Maximum size: {MAX_IMAGE_SIZE_MB} MB."
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

            st.subheader("Uploaded Crop Image")

            col1, col2 = st.columns([1, 1])

            with col1:

                st.image(
                    image,
                    caption=f"Crop entered: {crop_name or 'Not entered'}",
                    use_container_width=True
                )

            with col2:

                st.markdown("### Image Information")
                st.write(f"**Crop Name:** {crop_name or 'Not entered'}")
                st.write(
                    f"**Image Dimensions:** {image.width} × {image.height} pixels"
                )
                st.write(f"**File Size:** {file_size_mb:.2f} MB")
                st.success("Image uploaded successfully.")

            st.divider()

            # ----------------------------------------
            # 6. MODEL STATUS AND PREDICTION
            # ----------------------------------------

            if not PREDICTION_ENABLED:

                st.warning(
                    "The AI prediction feature is currently disabled."
                )

            elif st.button(
                "🔍 Analyze Leaf Image",
                type="primary",
                use_container_width=True
            ):

                if not crop_name:

                    st.warning(
                        "Please enter the crop name before starting analysis."
                    )

                else:

                    with st.spinner(
                        "AgriVision AI is checking the image..."
                    ):

                        result = predict_disease(
                            image,
                            expected_crop=crop_name
                        )

                    if result["status"] == "success":

                        st.subheader("🤖 AI Prediction Result")

                        result_col1, result_col2 = st.columns(2)

                        with result_col1:
                            st.metric("Predicted Crop", result["crop"])

                        with result_col2:
                            st.metric(
                                "Model Confidence",
                                f"{result['confidence'] * 100:.2f}%"
                            )

                        st.success(
                            "Predicted Disease: "
                            + result["disease"].replace("_", " ")
                        )

                        st.subheader("Top 3 Model Predictions")

                        for index, prediction in enumerate(
                            result["top_predictions"],
                            start=1
                        ):

                            st.write(
                                f"**{index}. {prediction['crop']} — "
                                f"{prediction['disease'].replace('_', ' ')}**"
                            )

                            st.progress(prediction["confidence"])

                            st.caption(
                                f"Model score: {prediction['confidence'] * 100:.2f}%"
                            )

                        st.info(
                            "This is an AI-generated prediction, not a confirmed "
                            "agricultural diagnosis. Model confidence is not a "
                            "guarantee of correctness. Consult an agricultural "
                            "expert before applying treatment."
                        )

                    elif result["status"] == "unsupported":

                        st.warning(result["message"])

                    elif result["status"] == "mismatch":

                        st.warning(result["message"])
                        st.info(
                            "No disease result is shown because the model's "
                            "predicted crop did not match the crop name you entered."
                        )

                    elif result["status"] == "uncertain":

                        st.warning(result["message"])

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
