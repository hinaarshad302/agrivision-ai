
import streamlit as st

st.set_page_config(page_title="Crop Library", page_icon="🌿", layout="wide")

st.title("🌿 Crop Knowledge Library")
st.write("Explore information about the crops supported by AgriVision AI.")

crops = {
    "Tomato": {
        "emoji": "🍅",
        "description": "Tomato is an important vegetable crop used in salads, cooking and food products.",
        "common_diseases": [
            "Early Blight",
            "Late Blight",
            "Bacterial Spot",
            "Leaf Mold"
        ]
    },
    "Potato": {
        "emoji": "🥔",
        "description": "Potato is a major food crop and an important source of carbohydrates.",
        "common_diseases": [
            "Early Blight",
            "Late Blight"
        ]
    },
    "Corn": {
        "emoji": "🌽",
        "description": "Corn is an important cereal crop used for food, animal feed and industrial products.",
        "common_diseases": [
            "Common Rust",
            "Northern Leaf Blight",
            "Gray Leaf Spot"
        ]
    },
    "Apple": {
        "emoji": "🍎",
        "description": "Apple is a widely cultivated fruit crop with high nutritional and commercial value.",
        "common_diseases": [
            "Apple Scab",
            "Black Rot",
            "Cedar Apple Rust"
        ]
    }
}

selected_crop = st.selectbox(
    "Choose a Crop",
    list(crops.keys())
)

crop_info = crops[selected_crop]

st.divider()

st.header(f"{crop_info['emoji']} {selected_crop}")

st.write(crop_info["description"])

st.subheader("Common Disease Categories")

for disease in crop_info["common_diseases"]:
    st.markdown(f"- {disease}")

st.divider()

st.info(
    "This library provides general educational information. "
    "Disease categories may vary by region and growing conditions."
)

st.caption("AgriVision AI | Crop Knowledge Library")
