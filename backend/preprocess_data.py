import cv2
import numpy as np
import os


IMAGE_SIZE = (224, 224)


def load_image(image_path):
    """
    Load an image from the given path.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to read the image.")

    return image


def resize_image(image):
    """
    Resize image to the required size.
    """
    return cv2.resize(image, IMAGE_SIZE)


def normalize_image(image):
    """
    Normalize pixel values from 0-255 to 0-1.
    """
    return image.astype(np.float32) / 255.0


def remove_noise(image):
    """
    Reduce minor image noise using Gaussian blur.
    """
    return cv2.GaussianBlur(image, (3, 3), 0)


def convert_color(image):
    """
    Convert image from BGR to RGB.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def preprocess_image(image_path):
    """
    Complete image preprocessing pipeline.
    """

    image = load_image(image_path)

    image = resize_image(image)

    image = remove_noise(image)

    image = convert_color(image)

    normalized_image = normalize_image(image)

    return normalized_image


if __name__ == "__main__":

    sample_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "sample_images",
    "sample.jpg"
    )

    try:
        processed_image = preprocess_image(sample_path)

        print("Image preprocessing successful!")
        print("Processed image shape:", processed_image.shape)
        print(
            "Pixel value range:",
            processed_image.min(),
            "to",
            processed_image.max()
        )

    except Exception as e:
        print("Error:", e)
        