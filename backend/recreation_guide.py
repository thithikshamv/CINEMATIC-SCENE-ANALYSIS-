import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from feature_fusion import analyze_image


def generate_recreation_guide(analysis):

    cinematic = analysis["cinematic_analysis"]
    visual = analysis["visual_features"]
    lighting = analysis["lighting_color"]
    composition = analysis["composition"]

    camera_angle = cinematic["camera_angle"]
    camera_level = cinematic["camera_level"]

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

    # =========================================================
    # CAMERA SETUP
    # =========================================================

    if camera_angle == "Low":

        camera_position = (
            "Place the camera below the subject's eye line. "
            "Keep the camera slightly tilted upward to preserve the "
            "low-angle perspective."
        )

        camera_effect = (
            "This helps reproduce the stronger and more dominant "
            "perspective detected in the reference."
        )

    elif camera_angle == "High":

        camera_position = (
            "Raise the camera above the subject's eye line and "
            "angle it slightly downward."
        )

        camera_effect = (
            "This recreates the elevated perspective and can make "
            "the subject appear smaller within the environment."
        )

    elif camera_angle == "Overhead":

        camera_position = (
            "Position the camera substantially above the subject "
            "and aim it downward toward the scene."
        )

        camera_effect = (
            "This emphasizes the spatial arrangement of the scene "
            "and the subject's relationship with the environment."
        )

    elif camera_angle == "Dutch":

        camera_position = (
            "Keep the camera tilted diagonally rather than perfectly level."
        )

        camera_effect = (
            "Maintain the diagonal horizon to reproduce the unstable "
            "and tense visual character."
        )

    else:

        camera_position = (
            "Keep the camera approximately at the subject's eye line "
            "for a natural perspective."
        )

        camera_effect = (
            "This preserves the neutral and realistic perspective "
            "detected in the reference."
        )

    # Camera height

    if camera_level == "Aerial":

        camera_height = (
            "Use an elevated or aerial camera position to capture "
            "a broad view of the environment."
        )

    elif camera_level == "Eye":

        camera_height = (
            "Position the camera approximately at the subject's eye level."
        )

    elif camera_level == "Shoulder":

        camera_height = (
            "Position the camera around the subject's shoulder height "
            "for a character-focused perspective."
        )

    elif camera_level == "Hip":

        camera_height = (
            "Position the camera approximately around hip height. "
            "Keep it slightly below the subject's eye line."
        )

    elif camera_level == "Knee":

        camera_height = (
            "Place the camera around knee height to strengthen the "
            "low-perspective effect."
        )

    else:

        camera_height = (
            "Place the camera close to ground level for an extreme "
            "low-perspective look."
        )

    # =========================================================
    # LENS / FRAMING
    # =========================================================

    if camera_angle in ["Low", "High", "Neutral"]:

        lens_suggestion = (
            "A normal or slightly wide lens can be a useful starting "
            "point. Around 35–50mm is a reasonable practical range "
            "for testing a similar perspective, but the exact focal "
            "length cannot be determined from a single image."
        )

    elif camera_angle == "Overhead":

        lens_suggestion = (
            "Use a lens that allows the required environment to fit "
            "comfortably into the frame. A wider lens may help when "
            "the surrounding space is important."
        )

    else:

        lens_suggestion = (
            "Use a normal focal length as a starting point and adjust "
            "according to the desired amount of environmental distortion."
        )

    # =========================================================
    # LIGHTING
    # =========================================================

    if lighting_type == "Low-key":

        lighting_setup = (
            "Use a directional key light from one side of the subject. "
            "Keep the opposite side darker and avoid filling all the shadows."
        )

    elif lighting_type == "High-key":

        lighting_setup = (
            "Use broad, soft lighting with gentle shadows. "
            "Keep the subject and background relatively bright."
        )

    else:

        lighting_setup = (
            "Start with balanced lighting and introduce a controlled "
            "directional key light to reproduce the visual depth."
        )

    if contrast_level == "High":

        contrast_setup = (
            "Maintain a noticeable difference between highlights and shadows. "
            "Avoid flattening the image with excessive fill light."
        )

    elif contrast_level == "Low":

        contrast_setup = (
            "Keep the lighting soft and gradually introduce slightly stronger "
            "directional shadows if more depth is required."
        )

    else:

        contrast_setup = (
            "Maintain moderate separation between highlights and shadows."
        )

    # =========================================================
    # COLOR
    # =========================================================

    if temperature == "Warm":

        color_setup = (
            "Use a warm color grade with slightly warmer highlights. "
            "Keep the overall palette controlled rather than heavily saturated."
        )

    elif temperature == "Cool":

        color_setup = (
            "Use a cooler color grade, particularly in shadows and "
            "background areas, while keeping important subject details visible."
        )

    else:

        color_setup = (
            "Keep the color temperature relatively neutral. "
            "If recreating the look creatively, introduce only a subtle "
            "warm or cool bias rather than an extreme color grade."
        )

    if saturation_level == "High":

        saturation_setup = (
            "Preserve the vivid colors of the reference, but concentrate "
            "strong colors on important visual elements."
        )

    elif saturation_level == "Low":

        saturation_setup = (
            "Keep the palette muted and restrained. Avoid excessive saturation."
        )

    else:

        saturation_setup = (
            "Maintain moderate saturation for a natural but controlled cinematic palette."
        )

    # =========================================================
    # COMPOSITION
    # =========================================================

    if subject_position == "Center / Middle":

        composition_setup = (
            "Keep the main subject close to the center of the frame "
            "to reproduce the reference's stable visual structure."
        )

    else:

        composition_setup = (
            "Maintain the subject's off-center placement and preserve "
            "the surrounding negative space."
        )

    if rule_of_thirds == "Strong tendency":

        framing_setup = (
            "Place the main subject or important facial feature near a "
            "rule-of-thirds intersection."
        )

    elif rule_of_thirds == "Moderate tendency":

        framing_setup = (
            "Use the current framing as a starting point, then position "
            "the main point of interest slightly closer to a third-line "
            "intersection if you want a stronger match."
        )

    else:

        framing_setup = (
            "Do not force the rule of thirds. Prioritize reproducing the "
            "reference's actual subject placement and visual balance."
        )

    # =========================================================
    # BACKGROUND
    # =========================================================

    if background_separation == "Low":

        background_setup = (
            "Keep the subject relatively connected to the environment. "
            "If you want more separation while preserving the same composition, "
            "increase subject-background distance or use a wider aperture."
        )

    elif background_separation == "Medium":

        background_setup = (
            "Create moderate subject-background separation using camera "
            "distance, aperture, or controlled background lighting."
        )

    else:

        background_setup = (
            "Maintain clear separation between the subject and background. "
            "Depth of field and directional lighting can help preserve this."
        )

    # =========================================================
    # RECREATION IDEA
    # =========================================================

    recreation_idea = (
        f"To recreate this visual style, start with a {camera_angle.lower()} "
        f"camera angle at {camera_level.lower()} level. "
        f"{lighting_setup} "
        f"Use the {temperature.lower()} color direction and maintain "
        f"{contrast_level.lower()} contrast with {saturation_level.lower()} saturation. "
        f"{composition_setup}"
    )

    # =========================================================
    # RETURN GUIDE
    # =========================================================

    return {

        "camera_setup": [
            camera_position,
            camera_height,
            camera_effect,
            lens_suggestion
        ],

        "lighting_setup": [
            lighting_setup,
            contrast_setup
        ],

        "color_setup": [
            color_setup,
            saturation_setup
        ],

        "composition_setup": [
            composition_setup,
            framing_setup,
            background_setup
        ],

        "recreation_idea": recreation_idea
    }


def display_recreation_guide(guide):

    print("\n\n=======================================================")
    print("              RECREATE THIS VISUAL STYLE")
    print("=======================================================")

    print("\n[CAMERA SETUP]")

    for item in guide["camera_setup"]:
        print("-", item)

    print("\n[LIGHTING SETUP]")

    for item in guide["lighting_setup"]:
        print("-", item)

    print("\n[COLOR & GRADING]")

    for item in guide["color_setup"]:
        print("-", item)

    print("\n[COMPOSITION]")

    for item in guide["composition_setup"]:
        print("-", item)

    print("\n[RECREATION IDEA]")
    print(guide["recreation_idea"])

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

        print("\nGenerating recreation guide...")

        analysis = analyze_image(image_path)

        guide = generate_recreation_guide(analysis)

        display_recreation_guide(guide)

    except Exception as e:

        print("Error:", e)