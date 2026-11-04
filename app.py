workflow_steps = [
    ("01", "Upload Image", "Upload a crop leaf image."),
    ("02", "Image Processing", "Validate and prepare the image."),
    ("03", "AI Analysis", "The trained model analyzes the leaf."),
    ("04", "Prediction", "View the predicted crop and disease."),
    ("05", "Review Result", "Check confidence and alternatives."),
]

workflow_columns = st.columns(5)

for column, (number, title, description) in zip(workflow_columns, workflow_steps):
    with column:
        render_html(f"""
            <div style="
                background: #ffffff;
                border: 1px solid #e0ebe3;
                border-radius: 12px;
                padding: 14px;
                min-height: 145px;
            ">
                <div style="
                    color: #23834e;
                    font-size: 12px;
                    font-weight: 800;
                    margin-bottom: 9px;
                ">STEP {number}</div>
                <div style="
                    color: #173d29;
                    font-size: 14px;
                    font-weight: 700;
                    margin-bottom: 8px;
                ">{title}</div>
                <div style="color: #718078; font-size: 11px;">
                    {description}
                </div>
            </div>
        """)

# ==================================================
# 10. MODEL EVALUATION
# ==================================================

st.subheader("📈 Model Evaluation")

performance_columns = st.columns(2)
performance_items = [
    ("TEST ACCURACY", "95.00%", "Held-out test dataset"),
    ("TEST DATASET", "4,101", "Images evaluated"),
]

for column, (label, value, note) in zip(performance_columns, performance_items):
    with column:
        render_html(f"""
            <div style="
                background: #ffffff;
                border: 1px solid #e0ebe3;
                border-radius: 13px;
                padding: 18px;
                min-height: 100px;
            ">
                <div style="
                    color: #718078;
                    font-size: 11px;
                    font-weight: 700;
                    letter-spacing: 1px;
                ">{label}</div>
                <div style="
                    color: #17653d;
                    font-size: 26px;
                    font-weight: 800;
                    margin: 6px 0;
                ">{value}</div>
                <div style="color: #718078; font-size: 12px;">{note}</div>
            </div>
        """)

st.caption(
    "Reported results are from the selected PlantVillage test dataset. "
    "Real-world field performance has not yet been independently validated."
)

# ==================================================
# 11. RESPONSIBLE AI NOTICE
# ==================================================

st.divider()
st.info(
    "AgriVision AI provides AI-generated crop-health screening results "
    "for educational and decision-support purposes. Predictions are not "
    "confirmed agricultural diagnoses. Consult a qualified agricultural "
    "expert before treatment."
)

# ==================================================
# 12. FOOTER
# ==================================================

render_html(f"""
    <div style="
        text-align: center;
        padding: 24px 10px;
        border-top: 1px solid #e0ebe3;
        margin-top: 25px;
    ">
        <div style="
            color: #16794b;
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 6px;
        ">🌱 {APP_NAME}</div>
        <div style="color: #718078; font-size: 12px;">
            Healthy Crops • Prosperous Farmers • Food Security
        </div>
        <div style="color: #9aa69e; font-size: 11px; margin-top: 9px;">
            Version {APP_VERSION}
        </div>
    </div>
""")
