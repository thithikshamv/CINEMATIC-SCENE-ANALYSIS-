import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from feature_fusion import analyze_image


def generate_recommendations(analysis):

    cinematic = analysis["cinematic_analysis"]
    visual = analysis["visual_features"]
    lighting = analysis["lighting_color"]
    composition = analysis["composition"]

    camera_angle = cinematic["camera_angle"]
    camera_level = cinematic["camera_level"]

    brightness_level = lighting["brightness_level"]
    contrast_level = lighting["contrast_level"]
    saturation_level = lighting["saturation_level"]
    lighting_type = lighting["lighting_type"]

    color_temperature = visual["color_temperature"]

    subject_position = composition["subject_position"]
    rule_of_thirds = composition["rule_of_thirds"]
    visual_balance = composition["visual_balance"]
    background_separation = composition["background_separation"]

    camera_recommendations = []
    lighting_recommendations = []
    composition_recommendations = []
    creative_recommendations = []

    # =========================================================
    # CAMERA RECOMMENDATIONS
    # =========================================================

    if camera_angle == "Low":
        camera_recommendations.append(
            "The low angle already creates a strong and dominant perspective. "
            "Keep the camera below the subject's eye line when you want the "
            "subject to appear powerful or imposing."
        )

    elif camera_angle == "High":
        camera_recommendations.append(
            "The high angle can make the subject appear smaller or vulnerable. "
            "For a stronger character presence, try moving closer to eye level "
            "or slightly below the subject."
        )

    elif camera_angle == "Overhead":
        camera_recommendations.append(
            "The overhead perspective emphasizes the subject's relationship "
            "with the surrounding environment. Use it when spatial storytelling "
            "is important."
        )

    elif camera_angle == "Dutch":
        camera_recommendations.append(
            "The tilted camera creates visual tension and instability. "
            "Keep the diagonal framing when you want an unsettling or intense mood."
        )

    else:
        camera_recommendations.append(
            "The neutral camera angle provides a natural perspective. "
            "For a more dramatic result, experiment with a slightly lower "
            "or higher camera position."
        )

    # Camera level
    if camera_level == "Eye":
        camera_recommendations.append(
            "Eye-level framing feels natural and direct. For a more dramatic "
            "perspective, experiment with hip, knee, or ground level."
        )

    elif camera_level == "Shoulder":
        camera_recommendations.append(
            "Shoulder-level framing works well for character-focused scenes. "
            "Move slightly lower for a stronger sense of power."
        )

    elif camera_level == "Hip":
        camera_recommendations.append(
            "Hip-level framing adds subtle visual drama without becoming extreme. "
            "It can work well for dynamic character shots."
        )

    elif camera_level == "Knee":
        camera_recommendations.append(
            "Knee-level framing emphasizes the subject from below. "
            "Use it when you want stronger visual dominance."
        )

    elif camera_level == "Ground":
        camera_recommendations.append(
            "Ground-level framing creates an extreme perspective. "
            "Use it selectively for dramatic or visually striking moments."
        )

    elif camera_level == "Aerial":
        camera_recommendations.append(
            "Aerial framing is useful for establishing environments and showing "
            "the subject's relationship with the surrounding space."
        )

    # =========================================================
    # LIGHTING RECOMMENDATIONS
    # =========================================================

    if lighting_type == "Low-key":
        lighting_recommendations.append(
            "Keep the strong light-and-shadow relationship if you want a "
            "dramatic, mysterious, or tense atmosphere."
        )

        if brightness_level == "Low":
            lighting_recommendations.append(
                "The scene is quite dark. Add a subtle fill light if important "
                "facial or subject details are getting lost."
            )

    elif lighting_type == "High-key":
        lighting_recommendations.append(
            "The bright lighting creates a clean and open appearance. "
            "Use soft, diffused light if you want to maintain this feeling."
        )

        if contrast_level == "Low":
            lighting_recommendations.append(
                "For more cinematic depth, introduce controlled side lighting "
                "to create slightly stronger shadows."
            )

    else:
        lighting_recommendations.append(
            "The lighting is relatively balanced. For a more dramatic cinematic "
            "look, introduce directional lighting from one side of the subject."
        )

    if contrast_level == "High":
        lighting_recommendations.append(
            "The contrast is already strong. Avoid excessive additional contrast "
            "unless you intentionally want a harsher visual style."
        )

    elif contrast_level == "Low":
        lighting_recommendations.append(
            "Consider increasing directional lighting slightly to create more "
            "depth between highlights and shadows."
        )

    # =========================================================
    # COLOR RECOMMENDATIONS
    # =========================================================

    if color_temperature == "Warm":
        creative_recommendations.append(
            "The warm color palette can support intimate, nostalgic, or energetic "
            "visuals. Keep warm highlights if that mood is intentional."
        )

    elif color_temperature == "Cool":
        creative_recommendations.append(
            "The cool color palette can support distant, calm, serious, or "
            "melancholic visuals. Maintain cooler shadows for consistency."
        )

    else:
        creative_recommendations.append(
            "The color temperature is neutral. A controlled warm or cool color "
            "direction could make the visual mood more distinctive."
        )

    if saturation_level == "High":
        creative_recommendations.append(
            "The colors are vivid. Keep the strongest colors focused on important "
            "visual elements so the frame does not become visually overwhelming."
        )

    elif saturation_level == "Low":
        creative_recommendations.append(
            "The muted colors create a restrained appearance. Selectively increasing "
            "the saturation of important colors can create stronger visual emphasis."
        )

    else:
        creative_recommendations.append(
            "The moderate saturation provides flexibility for color grading. "
            "Use a controlled color palette to maintain visual consistency."
        )

    # =========================================================
    # COMPOSITION RECOMMENDATIONS
    # =========================================================

    if subject_position == "Center / Middle":
        composition_recommendations.append(
            "The subject is centered. This gives stability and direct attention. "
            "For a more dynamic frame, try moving the subject toward one of the "
            "rule-of-thirds points."
        )

    else:
        composition_recommendations.append(
            "The subject is not strongly centered, which can create a more dynamic "
            "composition. Maintain enough negative space around the subject when needed."
        )

    if rule_of_thirds == "Moderate tendency":
        composition_recommendations.append(
            "The frame shows some rule-of-thirds tendency. You can strengthen it "
            "by placing the subject's face or main point of interest closer to a "
            "third-line intersection."
        )

    elif rule_of_thirds == "Strong tendency":
        composition_recommendations.append(
            "The composition already uses the rule of thirds effectively. "
            "Maintain the placement while adjusting negative space according "
            "to the subject's direction of attention."
        )

    else:
        composition_recommendations.append(
            "The composition does not strongly follow the rule of thirds. "
            "Try positioning the main subject near a third-line intersection "
            "for a more dynamic alternative."
        )

    if background_separation == "Low":
        composition_recommendations.append(
            "The subject blends with the background. Increase separation by "
            "changing the camera angle, using a wider aperture, increasing "
            "distance from the background, or introducing directional light."
        )

    elif background_separation == "Medium":
        composition_recommendations.append(
            "The subject has moderate background separation. A slightly wider "
            "aperture or greater subject-background distance could make the "
            "subject stand out more."
        )

    else:
        composition_recommendations.append(
            "The subject already separates clearly from the background. "
            "Maintain this separation to preserve visual focus."
        )

    # =========================================================
    # COMBINED CREATIVE RECOMMENDATION
    # =========================================================

    if camera_angle == "Low" and lighting_type == "Low-key":
        creative_recommendations.append(
            "For a powerful cinematic character look, combine the low camera "
            "perspective with directional low-key lighting and controlled shadows."
        )

    elif camera_angle == "Dutch":
        creative_recommendations.append(
            "For a tense or unsettling visual, maintain the diagonal camera "
            "angle and support it with directional lighting and stronger contrast."
        )

    elif camera_angle == "High":
        creative_recommendations.append(
            "For a vulnerable or isolated character feeling, maintain the elevated "
            "camera perspective and leave sufficient negative space around the subject."
        )

    elif lighting_type == "High-key":
        creative_recommendations.append(
            "For a softer and more approachable cinematic look, maintain the bright "
            "lighting and combine it with balanced framing and gentle colors."
        )

    else:
        creative_recommendations.append(
            "To increase the cinematic impact, coordinate the camera perspective, "
            "lighting direction, color palette, and subject placement instead of "
            "changing only one visual element."
        )

    return {
        "camera_recommendations": camera_recommendations,
        "lighting_recommendations": lighting_recommendations,
        "composition_recommendations": composition_recommendations,
        "creative_recommendations": creative_recommendations
    }


def display_recommendations(recommendations):

    print("\n\n=======================================================")
    print("            VISUAL COMPOSITION RECOMMENDATIONS")
    print("=======================================================")

    print("\n[CAMERA]")
    for recommendation in recommendations["camera_recommendations"]:
        print("-", recommendation)

    print("\n[LIGHTING]")
    for recommendation in recommendations["lighting_recommendations"]:
        print("-", recommendation)

    print("\n[COMPOSITION]")
    for recommendation in recommendations["composition_recommendations"]:
        print("-", recommendation)

    print("\n[CREATIVE DIRECTION]")
    for recommendation in recommendations["creative_recommendations"]:
        print("-", recommendation)

    print("\n=======================================================")


if __name__ == "__main__":

    project_root = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    image_path = os.path.join(
        project_root,
        "sample_images",
        "sample.jpg"
    )

    try:

        print("\nGenerating visual recommendations...")

        analysis = analyze_image(image_path)

        recommendations = generate_recommendations(analysis)

        display_recommendations(recommendations)

    except Exception as e:
        print("Error:", e)