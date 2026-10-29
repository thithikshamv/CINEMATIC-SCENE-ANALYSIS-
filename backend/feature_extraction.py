import cv2
import numpy as np
import os

from preprocess_data import load_image


def calculate_brightness(image):
    """
    Calculate average image brightness.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    brightness = np.mean(gray)

    return round(float(brightness), 2)


def calculate_contrast(image):
    """
    Calculate image contrast using standard deviation
    of grayscale pixel intensities.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    contrast = np.std(gray)

    return round(float(contrast), 2)


def calculate_saturation(image):
    """
    Calculate average color saturation.
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    saturation = np.mean(hsv[:, :, 1])

    return round(float(saturation), 2)


def calculate_color_temperature(image):
    """
    Estimate whether the image has a warm, cool,
    or neutral color tendency.
    """

    red_channel = np.mean(image[:, :, 0])
    blue_channel = np.mean(image[:, :, 2])

    difference = red_channel - blue_channel

    if difference > 15:
        temperature = "Warm"
    elif difference < -15:
        temperature = "Cool"
    else:
        temperature = "Neutral"

    return temperature


def get_dominant_colors(image, number_of_colors=5):
    """
    Extract dominant colors using K-Means clustering.
    """

    pixels = image.reshape((-1, 3))

    pixels = np.float32(pixels)

    criteria = (
        cv2.TERM_CRITERIA_EPS +
        cv2.TERM_CRITERIA_MAX_ITER,
        100,
        0.2
    )

    flags = cv2.KMEANS_PP_CENTERS

    compactness, labels, centers = cv2.kmeans(
        pixels,
        number_of_colors,
        None,
        criteria,
        10,
        flags
    )

    centers = np.uint8(centers)

    counts = np.bincount(labels.flatten())

    sorted_indices = np.argsort(counts)[::-1]

    dominant_colors = []

    for index in sorted_indices:
        color = centers[index]

        dominant_colors.append({
            "rgb": (
                int(color[0]),
                int(color[1]),
                int(color[2])
            ),
            "percentage": round(
                float(counts[index] / len(labels) * 100),
                2
            )
        })

    return dominant_colors


def extract_visual_features(image_path):
    """
    Extract all basic visual features from an image.
    """

    image = load_image(image_path)

    # OpenCV loads images as BGR.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    brightness = calculate_brightness(image)

    contrast = calculate_contrast(image)

    saturation = calculate_saturation(image)

    temperature = calculate_color_temperature(image)

    dominant_colors = get_dominant_colors(image)

    features = {
        "brightness": brightness,
        "contrast": contrast,
        "saturation": saturation,
        "color_temperature": temperature,
        "dominant_colors": dominant_colors
    }

    return features


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

        features = extract_visual_features(image_path)

        print("\n========== VISUAL FEATURE ANALYSIS ==========\n")

        print("Brightness:", features["brightness"])

        print("Contrast:", features["contrast"])

        print("Saturation:", features["saturation"])

        print(
            "Color Temperature:",
            features["color_temperature"]
        )

        print("\nDominant Colors:")

        for color in features["dominant_colors"]:

            print(
                "RGB:",
                color["rgb"],
                "| Percentage:",
                str(color["percentage"]) + "%"
            )

        print("\n=============================================")

    except Exception as e:

        print("Error:", e)