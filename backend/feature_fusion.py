import os

from feature_extraction import extract_visual_features
from lighting_color import analyze_lighting_and_color
from composition_analysis import analyze_composition
from cinematic_analysis import analyze_camera


# =========================================================
# COMPLETE CINEMATIC SCENE ANALYSIS
# =========================================================

def analyze_image(image_path):

    print("\nStarting complete cinematic scene analysis...\n")

    # -----------------------------------------------------
    # 1. VISUAL FEATURE EXTRACTION
    # -----------------------------------------------------

    print("1. Extracting visual features...")

    visual_features = extract_visual_features(
        image_path
    )

    # -----------------------------------------------------
    # 2. LIGHTING AND COLOR ANALYSIS
    # -----------------------------------------------------

    print("2. Analyzing lighting and color...")

    lighting_color = analyze_lighting_and_color(
        image_path
    )

    # -----------------------------------------------------
    # 3. SUBJECT AND COMPOSITION ANALYSIS
    # -----------------------------------------------------

    print("3. Analyzing composition...")

    composition = analyze_composition(
        image_path
    )

    # -----------------------------------------------------
    # 4. CINEMATIC CAMERA ANALYSIS
    # -----------------------------------------------------

    print("4. Running CineScale AI model...")

    cinematic_analysis = analyze_camera(
        image_path
    )

    # -----------------------------------------------------
    # 5. FEATURE FUSION
    # -----------------------------------------------------

    print("5. Combining all features...")

    combined_analysis = {
        "image_path": image_path,

        "cinematic_analysis": cinematic_analysis,

        "visual_features": visual_features,

        "lighting_color": lighting_color,

        "composition": composition
    }

    return combined_analysis


# =========================================================
# DISPLAY COMPLETE ANALYSIS
# =========================================================

def display_analysis(results):

    print("\n")
    print("=" * 60)
    print("          COMPLETE CINEMATIC SCENE ANALYSIS")
    print("=" * 60)

    # -----------------------------------------------------
    # CINEMATIC CAMERA
    # -----------------------------------------------------

    cinematic = results["cinematic_analysis"]

    print("\n[CINEMATIC CAMERA]")

    print(
        "Camera Angle:",
        cinematic["camera_angle"]
    )

    print(
        "Angle Confidence:",
        str(
            cinematic["camera_angle_confidence"]
        ) + "%"
    )

    print(
        "Camera Level:",
        cinematic["camera_level"]
    )

    print(
        "Level Confidence:",
        str(
            cinematic["camera_level_confidence"]
        ) + "%"
    )

    # -----------------------------------------------------
    # VISUAL FEATURES
    # -----------------------------------------------------

    visual = results["visual_features"]

    print("\n[VISUAL FEATURES]")

    print(
        "Brightness:",
        visual["brightness"]
    )

    print(
        "Contrast:",
        visual["contrast"]
    )

    print(
        "Saturation:",
        visual["saturation"]
    )

    print(
        "Color Temperature:",
        visual["color_temperature"]
    )

    # -----------------------------------------------------
    # LIGHTING AND COLOR
    # -----------------------------------------------------

    lighting = results["lighting_color"]

    print("\n[LIGHTING AND COLOR]")

    if "lighting_type" in lighting:
        print(
            "Lighting Type:",
            lighting["lighting_type"]
        )

    if "brightness_level" in lighting:
        print(
            "Brightness Level:",
            lighting["brightness_level"]
        )

    if "contrast_level" in lighting:
        print(
            "Contrast Level:",
            lighting["contrast_level"]
        )

    if "saturation_level" in lighting:
        print(
            "Saturation Level:",
            lighting["saturation_level"]
        )

    # -----------------------------------------------------
    # SUBJECT AND COMPOSITION
    # -----------------------------------------------------

    composition = results["composition"]

    print("\n[SUBJECT AND COMPOSITION]")

    print(
        "Main Subject:",
        composition["main_subject"]
    )

    print(
        "Subject Confidence:",
        str(
            composition["subject_confidence"]
        ) + "%"
    )

    print(
        "Subject Position:",
        composition["subject_position"]
    )

    print(
        "Rule of Thirds:",
        composition["rule_of_thirds"]
    )

    print(
        "Visual Balance:",
        composition["visual_balance"]
    )

    print(
        "Background Separation:",
        composition["background_separation"]
    )

    print("\nDetected Objects:")

    detected_objects = composition[
        "detected_objects"
    ]

    if detected_objects:

        for obj in detected_objects:

            print(
                "-",
                obj["label"],
                "| Confidence:",
                str(
                    obj["confidence"]
                ) + "%"
            )

    else:

        print(
            "- No recognizable objects detected"
        )

    print("\n")
    print("=" * 60)


# =========================================================
# TEST
# =========================================================

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

        results = analyze_image(
            image_path
        )

        display_analysis(
            results
        )

    except Exception as e:

        print(
            "\nError:",
            e
        )