import os
import cv2
import numpy as np

from feature_extraction import extract_visual_features


def classify_brightness(brightness):
    """
    Classify the overall brightness of the image.
    """

    if brightness < 70:
        return "Low"
    elif brightness < 160:
        return "Medium"
    else:
        return "High"


def classify_contrast(contrast):
    """
    Classify the overall image contrast.
    """

    if contrast < 40:
        return "Low"
    elif contrast < 80:
        return "Medium"
    else:
        return "High"


def classify_saturation(saturation):
    """
    Classify the overall color saturation.
    """

    if saturation < 60:
        return "Low"
    elif saturation < 140:
        return "Medium"
    else:
        return "High"


def classify_lighting(brightness, contrast):
    """
    Estimate whether the scene has a low-key,
    balanced, or high-key lighting tendency.
    """

    if brightness < 90 and contrast >= 45:
        return "Low-key"

    elif brightness >= 160 and contrast < 70:
        return "High-key"

    else:
        return "Balanced"


def analyze_lighting_and_color(image_path):
    """
    Perform lighting and color analysis using
    extracted visual features.
    """

    features = extract_visual_features(image_path)

    brightness = features["brightness"]
    contrast = features["contrast"]
    saturation = features["saturation"]
    temperature = features["color_temperature"]

    lighting_type = classify_lighting(
        brightness,
        contrast
    )

    brightness_level = classify_brightness(
        brightness
    )

    contrast_level = classify_contrast(
        contrast
    )

    saturation_level = classify_saturation(
        saturation
    )

    analysis = {
        "brightness": brightness,
        "brightness_level": brightness_level,

        "contrast": contrast,
        "contrast_level": contrast_level,

        "saturation": saturation,
        "saturation_level": saturation_level,

        "color_temperature": temperature,

        "lighting_type": lighting_type,

        "dominant_colors": features["dominant_colors"]
    }

    return analysis


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

        result = analyze_lighting_and_color(
            image_path
        )

        print("\n========== LIGHTING & COLOR ANALYSIS ==========\n")

        print(
            "Brightness:",
            result["brightness"],
            "(" + result["brightness_level"] + ")"
        )

        print(
            "Contrast:",
            result["contrast"],
            "(" + result["contrast_level"] + ")"
        )

        print(
            "Saturation:",
            result["saturation"],
            "(" + result["saturation_level"] + ")"
        )

        print(
            "Color Temperature:",
            result["color_temperature"]
        )

        print(
            "Lighting Type:",
            result["lighting_type"]
        )

        print("\nDominant Colors:")

        for color in result["dominant_colors"]:

            print(
                "RGB:",
                color["rgb"],
                "| Percentage:",
                str(color["percentage"]) + "%"
            )

        print(
            "\n===============================================\n"
        )

    except Exception as e:

        print("Error:", e)