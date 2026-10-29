import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from feature_fusion import analyze_image


def generate_interpretation(analysis):

    cinematic = analysis["cinematic_analysis"]
    visual = analysis["visual_features"]
    lighting = analysis["lighting_color"]
    composition = analysis["composition"]

    camera_angle = cinematic["camera_angle"]
    angle_confidence = cinematic["camera_angle_confidence"]

    camera_level = cinematic["camera_level"]
    level_confidence = cinematic["camera_level_confidence"]

    brightness = visual["brightness"]
    contrast = visual["contrast"]
    saturation = visual["saturation"]
    temperature = visual["color_temperature"]

    lighting_type = lighting["lighting_type"]
    brightness_level = lighting["brightness_level"]
    contrast_level = lighting["contrast_level"]
    saturation_level = lighting["saturation_level"]

    subject_position = composition["subject_position"]
    rule_of_thirds = composition["rule_of_thirds"]
    visual_balance = composition["visual_balance"]
    background_separation = composition["background_separation"]

    # ---------------------------------------------------------
    # CAMERA INTERPRETATION
    # ---------------------------------------------------------

    if camera_angle == "Low":
        camera_text = (
            "The camera is positioned at a low angle, which can make "
            "the subject appear stronger, larger, or more dominant."
        )
    elif camera_angle == "High":
        camera_text = (
            "The camera is positioned at a high angle, which can make "
            "the subject appear smaller or more vulnerable within the scene."
        )
    elif camera_angle == "Overhead":
        camera_text = (
            "The camera looks down from a strongly elevated position, "
            "giving the scene an observational or spatial feeling."
        )
    elif camera_angle == "Dutch":
        camera_text = (
            "The camera is tilted diagonally, which can introduce "
            "tension, instability, or psychological unease."
        )
    else:
        camera_text = (
            "The camera uses a neutral angle, creating a natural and "
            "realistic perspective."
        )

    if camera_level == "Hip":
        level_text = (
            "The hip-level position adds a slightly lower perspective "
            "while keeping the subject relatively natural."
        )
    elif camera_level == "Knee":
        level_text = (
            "The knee-level position strengthens the low-perspective "
            "effect and can make the subject feel more imposing."
        )
    elif camera_level == "Ground":
        level_text = (
            "The ground-level camera creates a strong dramatic perspective "
            "and emphasizes the subject from below."
        )
    elif camera_level == "Shoulder":
        level_text = (
            "The shoulder-level camera creates a character-oriented and "
            "fairly intimate perspective."
        )
    elif camera_level == "Eye":
        level_text = (
            "The eye-level camera creates a direct and familiar perspective "
            "that feels natural to the viewer."
        )
    else:
        level_text = (
            "The elevated camera level provides a broader view of the scene."
        )

    # ---------------------------------------------------------
    # LIGHTING INTERPRETATION
    # ---------------------------------------------------------

    if lighting_type == "Low-key":
        lighting_text = (
            "The low-key lighting creates stronger shadows and a darker "
            "visual atmosphere, which can support dramatic or mysterious scenes."
        )
    elif lighting_type == "High-key":
        lighting_text = (
            "The high-key lighting produces a brighter and softer appearance, "
            "which can create an open, pleasant, or positive mood."
        )
    else:
        lighting_text = (
            "The balanced lighting keeps both bright and dark areas reasonably "
            "visible, creating a natural visual appearance."
        )

    # ---------------------------------------------------------
    # COLOR INTERPRETATION
    # ---------------------------------------------------------

    if temperature == "Warm":
        color_text = (
            "The warm color tendency gives the image a visually warmer feel "
            "and can support intimacy, energy, or nostalgia."
        )
    elif temperature == "Cool":
        color_text = (
            "The cool color tendency gives the image a cooler visual feeling "
            "that can support distance, calmness, or a more serious mood."
        )
    else:
        color_text = (
            "The color temperature is relatively neutral, so the image does "
            "not strongly lean toward either warm or cool tones."
        )

    if saturation_level == "High":
        saturation_text = (
            "The relatively high color saturation makes the colors more vivid "
            "and visually noticeable."
        )
    elif saturation_level == "Low":
        saturation_text = (
            "The lower saturation creates a more muted and restrained color appearance."
        )
    else:
        saturation_text = (
            "The saturation level is moderate, keeping the colors noticeable "
            "without becoming extremely intense."
        )

    # ---------------------------------------------------------
    # COMPOSITION INTERPRETATION
    # ---------------------------------------------------------

    if rule_of_thirds == "Strong tendency":
        thirds_text = (
            "The subject placement strongly follows the rule of thirds, "
            "which helps create a more dynamic composition."
        )
    elif rule_of_thirds == "Moderate tendency":
        thirds_text = (
            "The composition shows some tendency toward the rule of thirds, "
            "giving the frame a balance between structure and flexibility."
        )
    else:
        thirds_text = (
            "The subject does not strongly follow the rule of thirds and "
            "the composition is more centered or freely arranged."
        )

    if visual_balance == "Centered":
        balance_text = (
            "The visual weight is centered, giving the frame a stable and direct feeling."
        )
    elif visual_balance == "Balanced":
        balance_text = (
            "The visual elements are reasonably balanced across the frame."
        )
    else:
        balance_text = (
            "The visual weight is somewhat uneven, which can create visual tension "
            "or direct attention toward one side of the frame."
        )

    if background_separation == "High":
        separation_text = (
            "The subject is clearly separated from the background, helping it stand out."
        )
    elif background_separation == "Medium":
        separation_text = (
            "There is moderate separation between the subject and background."
        )
    else:
        separation_text = (
            "The subject has limited separation from the background, so some visual "
            "elements may blend together."
        )

    # ---------------------------------------------------------
    # FRIENDLY SUMMARY
    # ---------------------------------------------------------

    friendly_summary = (
        f"This image uses a {camera_angle.lower()} camera angle at "
        f"{camera_level.lower()} level. {camera_text} {level_text} "
        f"The scene uses {lighting_type.lower()} lighting with a "
        f"{temperature.lower()} color tendency. {balance_text}"
    )

    # ---------------------------------------------------------
    # WHY IT LOOKS CINEMATIC
    # ---------------------------------------------------------

    cinematic_reasons = []

    if camera_angle in ["Low", "High", "Dutch", "Overhead"]:
        cinematic_reasons.append(
            f"The {camera_angle.lower()} camera angle gives the frame a deliberate visual perspective."
        )

    if lighting_type in ["Low-key", "High-key"]:
        cinematic_reasons.append(
            f"The {lighting_type.lower()} lighting creates a noticeable visual mood."
        )

    if contrast_level == "High":
        cinematic_reasons.append(
            "The stronger contrast creates clear separation between light and shadow."
        )

    if saturation_level == "High":
        cinematic_reasons.append(
            "The vivid colors make important visual elements stand out."
        )

    if background_separation in ["Medium", "High"]:
        cinematic_reasons.append(
            "The subject has useful separation from the background."
        )

    if not cinematic_reasons:
        cinematic_reasons.append(
            "The combination of camera, lighting, color, and composition "
            "creates the overall visual character of the frame."
        )

    # ---------------------------------------------------------
    # KEY STRENGTHS
    # ---------------------------------------------------------

    strengths = []

    if camera_angle in ["Low", "Dutch", "Overhead"]:
        strengths.append(
            f"Distinctive {camera_angle.lower()} camera perspective"
        )

    if lighting_type != "Balanced":
        strengths.append(
            f"Strong {lighting_type.lower()} lighting character"
        )

    if contrast_level == "High":
        strengths.append("Strong light and shadow separation")

    if saturation_level == "High":
        strengths.append("Vivid and visually noticeable colors")

    if background_separation == "High":
        strengths.append("Clear subject-background separation")

    if visual_balance in ["Centered", "Balanced"]:
        strengths.append("Stable visual composition")

    if not strengths:
        strengths.append(
            "Balanced combination of visual characteristics"
        )

    return {
        "friendly_summary": friendly_summary,
        "camera_interpretation": f"{camera_text} {level_text}",
        "lighting_interpretation": lighting_text,
        "color_interpretation": f"{color_text} {saturation_text}",
        "composition_interpretation": (
            f"{thirds_text} {balance_text} {separation_text}"
        ),
        "why_cinematic": cinematic_reasons,
        "strengths": strengths
    }


def display_quick_analysis(analysis):

    cinematic = analysis["cinematic_analysis"]
    visual = analysis["visual_features"]
    lighting = analysis["lighting_color"]
    composition = analysis["composition"]

    print("\n=======================================================")
    print("              COMPLETE CINEMATIC SCENE ANALYSIS")
    print("=======================================================")

    print("\n[QUICK ANALYSIS]")

    print("\n[CINEMATIC CAMERA]")
    print("Camera Angle:", cinematic["camera_angle"])
    print(
        "Angle Confidence:",
        str(cinematic["camera_angle_confidence"]) + "%"
    )
    print("Camera Level:", cinematic["camera_level"])
    print(
        "Level Confidence:",
        str(cinematic["camera_level_confidence"]) + "%"
    )

    print("\n[VISUAL FEATURES]")
    print("Brightness:", visual["brightness"])
    print("Contrast:", visual["contrast"])
    print("Saturation:", visual["saturation"])
    print("Color Temperature:", visual["color_temperature"])

    print("\n[LIGHTING & COLOR]")
    print("Lighting Type:", lighting["lighting_type"])
    print("Brightness Level:", lighting["brightness_level"])
    print("Contrast Level:", lighting["contrast_level"])
    print("Saturation Level:", lighting["saturation_level"])

    print("\n[COMPOSITION]")
    print("Subject Position:", composition["subject_position"])
    print("Rule of Thirds:", composition["rule_of_thirds"])
    print("Visual Balance:", composition["visual_balance"])
    print("Background Separation:", composition["background_separation"])

    print("\n=======================================================")


def display_interpretation(interpretation):

    print("\n\n=======================================================")
    print("              AI-ASSISTED EXPLANATION")
    print("=======================================================")

    print("\n[FRIENDLY SUMMARY]")
    print(interpretation["friendly_summary"])

    print("\n[CAMERA]")
    print(interpretation["camera_interpretation"])

    print("\n[LIGHTING]")
    print(interpretation["lighting_interpretation"])

    print("\n[COLOR]")
    print(interpretation["color_interpretation"])

    print("\n[COMPOSITION]")
    print(interpretation["composition_interpretation"])

    print("\n[WHY DOES IT LOOK CINEMATIC?]")
    for reason in interpretation["why_cinematic"]:
        print("-", reason)

    print("\n[KEY STRENGTHS]")
    for strength in interpretation["strengths"]:
        print("-", strength)

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

        print("\nRunning complete cinematic analysis...\n")

        analysis = analyze_image(image_path)

        # FIRST: QUICK ANALYSIS
        display_quick_analysis(analysis)

        # SECOND: AI-ASSISTED EXPLANATION
        interpretation = generate_interpretation(analysis)

        display_interpretation(interpretation)

    except Exception as e:
        print("Error:", e)