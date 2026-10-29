import cv2
import os
import numpy as np
from ultralytics import YOLO

# =========================================================
# LOAD PRETRAINED OBJECT DETECTION MODEL
# =========================================================

print("Loading object detection model...")

model = YOLO("yolo11n.pt")

print("Object detection model loaded successfully!")


# =========================================================
# DETECT SUBJECTS
# =========================================================

def detect_subjects(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to load image.")

    height, width = image.shape[:2]

    results = model(
        image,
        verbose=False
    )

    detected_objects = []

    for result in results:

        if result.boxes is None:
            continue

        for box in result.boxes:

            confidence = float(box.conf[0])

            if confidence < 0.35:
                continue

            class_id = int(box.cls[0])

            class_name = model.names[class_id]

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)

            box_width = max(0, x2 - x1)
            box_height = max(0, y2 - y1)

            area = box_width * box_height

            detected_objects.append({
                "label": class_name,
                "confidence": round(confidence * 100, 2),
                "bbox": (x1, y1, x2, y2),
                "area": area,
                "center_x": (x1 + x2) / 2,
                "center_y": (y1 + y2) / 2,
                "width": box_width,
                "height": box_height
            })

    return detected_objects, width, height


# =========================================================
# FIND MAIN SUBJECT
# =========================================================

def find_main_subject(objects):

    if not objects:
        return None

    # Prefer people when present
    people = [
        obj for obj in objects
        if obj["label"] == "person"
    ]

    if people:
        return max(
            people,
            key=lambda obj: obj["area"]
        )

    # Otherwise use the largest detected object
    return max(
        objects,
        key=lambda obj: obj["area"]
    )


# =========================================================
# SUBJECT POSITION
# =========================================================

def determine_subject_position(subject, image_width, image_height):

    if subject is None:
        return "Unable to detect"

    center_x = subject["center_x"]
    center_y = subject["center_y"]

    horizontal = (
        "Left" if center_x < image_width / 3
        else "Right" if center_x > (image_width * 2 / 3)
        else "Center"
    )

    vertical = (
        "Top" if center_y < image_height / 3
        else "Bottom" if center_y > (image_height * 2 / 3)
        else "Middle"
    )

    return f"{horizontal} / {vertical}"


# =========================================================
# RULE OF THIRDS
# =========================================================

def analyze_rule_of_thirds(subject, image_width, image_height):

    if subject is None:
        return "Unable to determine"

    x = subject["center_x"]
    y = subject["center_y"]

    third_x_positions = [
        image_width / 3,
        image_width * 2 / 3
    ]

    third_y_positions = [
        image_height / 3,
        image_height * 2 / 3
    ]

    min_x_distance = min(
        abs(x - position)
        for position in third_x_positions
    )

    min_y_distance = min(
        abs(y - position)
        for position in third_y_positions
    )

    normalized_x = min_x_distance / image_width
    normalized_y = min_y_distance / image_height

    if normalized_x < 0.10 or normalized_y < 0.10:
        return "Strong tendency"

    elif normalized_x < 0.18 or normalized_y < 0.18:
        return "Moderate tendency"

    return "Weak tendency"


# =========================================================
# VISUAL BALANCE
# =========================================================

def analyze_visual_balance(
    subject,
    objects,
    image_width
):

    if subject is None:
        return "Unable to determine"

    subject_center = subject["center_x"]

    # Calculate visual mass on left and right
    left_mass = 0
    right_mass = 0

    for obj in objects:

        if obj["center_x"] < image_width / 2:
            left_mass += obj["area"]

        else:
            right_mass += obj["area"]

    total_mass = left_mass + right_mass

    if total_mass == 0:
        return "Unable to determine"

    difference = abs(
        left_mass - right_mass
    ) / total_mass

    if difference < 0.20:
        balance = "Balanced"

    elif difference < 0.45:
        balance = "Slightly off-center"

    else:
        balance = "Strongly off-center"

    # Mention subject placement when useful
    if subject_center < image_width / 3:
        return f"{balance} — subject weighted left"

    elif subject_center > image_width * 2 / 3:
        return f"{balance} — subject weighted right"

    return balance


# =========================================================
# BACKGROUND SEPARATION
# =========================================================

def analyze_background_separation(
    subject,
    image
):

    if subject is None:
        return "Unable to determine"

    x1, y1, x2, y2 = subject["bbox"]

    image_height, image_width = image.shape[:2]

    subject_area = (
        max(1, x2 - x1) *
        max(1, y2 - y1)
    )

    image_area = image_width * image_height

    subject_ratio = subject_area / image_area

    # Edge density around subject
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    edges = cv2.Canny(
        gray,
        100,
        200
    )

    surrounding_region = edges.copy()

    # Remove subject region
    surrounding_region[
        max(0, y1):min(image_height, y2),
        max(0, x1):min(image_width, x2)
    ] = 0

    surrounding_pixels = np.count_nonzero(
        surrounding_region
    )

    total_pixels = image_area

    edge_density = (
        surrounding_pixels /
        max(1, total_pixels)
    )

    # Heuristic interpretation
    if subject_ratio > 0.45:
        return "Strong"

    elif subject_ratio > 0.20:
        return "Moderate"

    elif edge_density < 0.03:
        return "Strong"

    else:
        return "Low"


# =========================================================
# COMPLETE COMPOSITION ANALYSIS
# =========================================================

def analyze_composition(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(
            "Unable to load image."
        )

    objects, width, height = detect_subjects(
        image_path
    )

    main_subject = find_main_subject(
        objects
    )

    subject_position = determine_subject_position(
        main_subject,
        width,
        height
    )

    rule_of_thirds = analyze_rule_of_thirds(
        main_subject,
        width,
        height
    )

    visual_balance = analyze_visual_balance(
        main_subject,
        objects,
        width
    )

    background_separation = analyze_background_separation(
        main_subject,
        image
    )

    # =====================================================
    # RETURN RESULTS
    # =====================================================

    result = {

        "subject_detected": (
            main_subject is not None
        ),

        "main_subject": (
            main_subject["label"]
            if main_subject
            else "Unable to detect"
        ),

        "subject_confidence": (
            main_subject["confidence"]
            if main_subject
            else 0
        ),

        "detected_objects": [
            {
                "label": obj["label"],
                "confidence": obj["confidence"]
            }
            for obj in objects
        ],

        "subject_position": subject_position,

        "rule_of_thirds": rule_of_thirds,

        "visual_balance": visual_balance,

        "background_separation": background_separation
    }

    return result


# =========================================================
# DISPLAY RESULTS
# =========================================================

def display_composition_analysis(results):

    print("\n========== COMPOSITION ANALYSIS ==========\n")

    print(
        "Main Subject:",
        results["main_subject"]
    )

    print(
        "Subject Confidence:",
        str(results["subject_confidence"]) + "%"
    )

    print(
        "Subject Position:",
        results["subject_position"]
    )

    print(
        "Rule of Thirds:",
        results["rule_of_thirds"]
    )

    print(
        "Visual Balance:",
        results["visual_balance"]
    )

    print(
        "Background Separation:",
        results["background_separation"]
    )

    print("\nDetected Objects:")

    if results["detected_objects"]:

        for obj in results["detected_objects"]:

            print(
                "-",
                obj["label"],
                "| Confidence:",
                str(obj["confidence"]) + "%"
            )

    else:

        print(
            "- No recognizable objects detected"
        )

    print(
        "\n=========================================="
    )


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

        results = analyze_composition(
            image_path
        )

        display_composition_analysis(
            results
        )

    except Exception as e:

        print(
            "Error:",
            e
        )