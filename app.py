import streamlit as st
import os
import sys

# =========================================================
# BACKEND PATH
# =========================================================

sys.path.append(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "backend"
    )
)

from feature_fusion import analyze_image
from interpretation import generate_interpretation
from recommendation import generate_recommendations
from recreation_guide import generate_recreation_guide


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Cinematic Scene Analysis",
    page_icon="🎬",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f7f4ee;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #252525;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #666666;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 650;
        color: #292929;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .analysis-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5e0d7;
        min-height: 130px;
    }

    .analysis-label {
        font-size: 13px;
        color: #777777;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .analysis-value {
        font-size: 22px;
        font-weight: 650;
        color: #292929;
    }

    .analysis-small {
        font-size: 14px;
        color: #777777;
        margin-top: 6px;
    }

    .explanation-box {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #e5e0d7;
        line-height: 1.7;
        color: #333333;
    }

    .recommendation-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5e0d7;
        margin-bottom: 15px;
        line-height: 1.6;
        color: #333333;
    }

    .recommendation-title {
        font-size: 18px;
        font-weight: 650;
        margin-bottom: 10px;
        color: #292929;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">Cinematic Scene Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-assisted analysis of camera, lighting, color and composition '
    'for filmmakers, photographers and visual creators.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# IMAGE UPLOAD
# =========================================================

uploaded_file = st.file_uploader(
    "Upload a cinematic frame or photograph",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    # =====================================================
    # SAVE UPLOADED IMAGE
    # =====================================================

    temp_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "sample_images"
    )

    os.makedirs(temp_dir, exist_ok=True)

    image_path = os.path.join(
        temp_dir,
        "uploaded_image.jpg"
    )

    with open(image_path, "wb") as file:
        file.write(uploaded_file.getbuffer())


    # =====================================================
    # DISPLAY IMAGE
    # =====================================================

    st.markdown(
        '<div class="section-title">Uploaded Scene</div>',
        unsafe_allow_html=True
    )

    st.image(
        uploaded_file,
        use_container_width=True
    )


    # =====================================================
    # ANALYZE BUTTON
    # =====================================================

    analyze_button = st.button(
        "Analyze Scene",
        type="primary",
        use_container_width=True
    )


    if analyze_button:

        try:

            # =================================================
            # COMPLETE ANALYSIS
            # =================================================

            with st.spinner(
                "Analyzing cinematic characteristics..."
            ):

                analysis = analyze_image(image_path)

                interpretation = generate_interpretation(
                    analysis
                )

                recommendations = generate_recommendations(
                    analysis
                )

                recreation_guide = generate_recreation_guide(
                    analysis
                )


            # Save results in session state
            st.session_state["analysis"] = analysis
            st.session_state["interpretation"] = interpretation
            st.session_state["recommendations"] = recommendations
            st.session_state["recreation_guide"] = recreation_guide


        except Exception as e:

            st.error(
                f"Analysis failed: {e}"
            )


# =========================================================
# DISPLAY RESULTS FROM SESSION STATE
# =========================================================

if "analysis" in st.session_state:

    analysis = st.session_state["analysis"]
    interpretation = st.session_state["interpretation"]
    recommendations = st.session_state["recommendations"]
    recreation_guide = st.session_state["recreation_guide"]

    cinematic = analysis["cinematic_analysis"]
    visual = analysis["visual_features"]
    lighting = analysis["lighting_color"]
    composition = analysis["composition"]


    # =====================================================
    # QUICK ANALYSIS
    # =====================================================

    st.markdown(
        '<div class="section-title">Quick Analysis</div>',
        unsafe_allow_html=True
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
            f"""
            <div class="analysis-box">

            <div class="analysis-label">
            Camera Angle
            </div>

            <div class="analysis-value">
            {cinematic["camera_angle"]}
            </div>

            <div class="analysis-small">
            Confidence:
            {cinematic["camera_angle_confidence"]:.2f}%
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            f"""
            <div class="analysis-box">

            <div class="analysis-label">
            Camera Level
            </div>

            <div class="analysis-value">
            {cinematic["camera_level"]}
            </div>

            <div class="analysis-small">
            Confidence:
            {cinematic["camera_level_confidence"]:.2f}%
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            f"""
            <div class="analysis-box">

            <div class="analysis-label">
            Lighting
            </div>

            <div class="analysis-value">
            {lighting["lighting_type"]}
            </div>

            <div class="analysis-small">
            Brightness: {lighting["brightness_level"]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # VISUAL FEATURES
    # =====================================================

    st.markdown(
        '<div class="section-title">Visual Features</div>',
        unsafe_allow_html=True
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            "Brightness",
            visual["brightness"]
        )

    with col2:
        st.metric(
            "Contrast",
            visual["contrast"]
        )

    with col3:
        st.metric(
            "Saturation",
            visual["saturation"]
        )

    with col4:
        st.metric(
            "Color Temperature",
            visual["color_temperature"]
        )


    # =====================================================
    # COMPOSITION
    # =====================================================

    st.markdown(
        '<div class="section-title">Composition</div>',
        unsafe_allow_html=True
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.markdown(
            f"""
            <div class="analysis-box">

            <div class="analysis-label">
            Subject Position
            </div>

            <div class="analysis-value">
            {composition["subject_position"]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            f"""
            <div class="analysis-box">

            <div class="analysis-label">
            Rule of Thirds
            </div>

            <div class="analysis-value">
            {composition["rule_of_thirds"]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            f"""
            <div class="analysis-box">

            <div class="analysis-label">
            Visual Balance
            </div>

            <div class="analysis-value">
            {composition["visual_balance"]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with col4:

        st.markdown(
            f"""
            <div class="analysis-box">

            <div class="analysis-label">
            Background Separation
            </div>

            <div class="analysis-value">
            {composition["background_separation"]}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # AI-ASSISTED EXPLANATION
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        'AI-Assisted Explanation'
        '</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        f"""
        <div class="explanation-box">

        <h4>Friendly Summary</h4>

        <p>
        {interpretation["friendly_summary"]}
        </p>

        <h4>Camera</h4>

        <p>
        {interpretation["camera_interpretation"]}
        </p>

        <h4>Lighting</h4>

        <p>
        {interpretation["lighting_interpretation"]}
        </p>

        <h4>Color</h4>

        <p>
        {interpretation["color_interpretation"]}
        </p>

        <h4>Composition</h4>

        <p>
        {interpretation["composition_interpretation"]}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # WHY CINEMATIC
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        'Why Does It Look Cinematic?'
        '</div>',
        unsafe_allow_html=True
    )


    cinematic_reasons = ""

    for reason in interpretation["why_cinematic"]:

        cinematic_reasons += (
            f"<li>{reason}</li>"
        )


    st.markdown(
        f"""
        <div class="explanation-box">

        <ul>
        {cinematic_reasons}
        </ul>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # KEY STRENGTHS
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        'Key Visual Strengths'
        '</div>',
        unsafe_allow_html=True
    )


    strengths = ""

    for strength in interpretation["strengths"]:

        strengths += (
            f"<li>{strength}</li>"
        )


    st.markdown(
        f"""
        <div class="explanation-box">

        <ul>
        {strengths}
        </ul>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # VISUAL RECOMMENDATIONS
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        'Visual Composition Recommendations'
        '</div>',
        unsafe_allow_html=True
    )


    # CAMERA

    camera_recommendations = ""

    for item in recommendations["camera_recommendations"]:

        camera_recommendations += (
            f"<li>{item}</li>"
        )


    st.markdown(
        f"""
        <div class="recommendation-box">

        <div class="recommendation-title">
        Camera
        </div>

        <ul>
        {camera_recommendations}
        </ul>

        </div>
        """,
        unsafe_allow_html=True
    )


    # LIGHTING

    lighting_recommendations = ""

    for item in recommendations["lighting_recommendations"]:

        lighting_recommendations += (
            f"<li>{item}</li>"
        )


    st.markdown(
        f"""
        <div class="recommendation-box">

        <div class="recommendation-title">
        Lighting
        </div>

        <ul>
        {lighting_recommendations}
        </ul>

        </div>
        """,
        unsafe_allow_html=True
    )


    # COMPOSITION

    composition_recommendations = ""

    for item in recommendations["composition_recommendations"]:

        composition_recommendations += (
            f"<li>{item}</li>"
        )


    st.markdown(
        f"""
        <div class="recommendation-box">

        <div class="recommendation-title">
        Composition
        </div>

        <ul>
        {composition_recommendations}
        </ul>

        </div>
        """,
        unsafe_allow_html=True
    )


    # CREATIVE DIRECTION

    creative_recommendations = ""

    for item in recommendations["creative_recommendations"]:

        creative_recommendations += (
            f"<li>{item}</li>"
        )


    st.markdown(
        f"""
        <div class="recommendation-box">

        <div class="recommendation-title">
        Creative Direction
        </div>

        <ul>
        {creative_recommendations}
        </ul>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # RECREATE BUTTON
    # =====================================================

    st.markdown("---")

    st.markdown(
        '<div class="section-title">'
        'Want to recreate this look?'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Use the detected camera, lighting, color and composition "
        "characteristics as a practical shooting guide."
    )


    recreate_button = st.button(
        "🎬 Recreate This Style",
        use_container_width=True
    )


    # =====================================================
    # RECREATION GUIDE
    # =====================================================

    if recreate_button:

        st.markdown(
            '<div class="section-title">'
            'Recreate This Visual Style'
            '</div>',
            unsafe_allow_html=True
        )


        # CAMERA

        st.markdown(
            '<div class="recommendation-title">'
            '01 — Camera Setup'
            '</div>',
            unsafe_allow_html=True
        )

        for item in recreation_guide["camera_setup"]:

            st.markdown(
                f"- {item}"
            )


        # LIGHTING

        st.markdown(
            '<div class="recommendation-title">'
            '02 — Lighting Setup'
            '</div>',
            unsafe_allow_html=True
        )

        for item in recreation_guide["lighting_setup"]:

            st.markdown(
                f"- {item}"
            )


        # COLOR

        st.markdown(
            '<div class="recommendation-title">'
            '03 — Color & Grading'
            '</div>',
            unsafe_allow_html=True
        )

        for item in recreation_guide["color_setup"]:

            st.markdown(
                f"- {item}"
            )


        # COMPOSITION

        st.markdown(
            '<div class="recommendation-title">'
            '04 — Composition'
            '</div>',
            unsafe_allow_html=True
        )

        for item in recreation_guide["composition_setup"]:

            st.markdown(
                f"- {item}"
            )


        # FINAL IDEA

        st.markdown(
            '<div class="recommendation-title">'
            '05 — Recreation Idea'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="explanation-box">

            {recreation_guide["recreation_idea"]}

            </div>
            """,
            unsafe_allow_html=True
        )
