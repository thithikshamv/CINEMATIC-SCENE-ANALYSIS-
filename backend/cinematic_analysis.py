import os

import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image


# ============================================================
# CINESCALE CLASS LABELS
# ============================================================

ANGLE_CLASSES = [
    "Overhead",
    "High",
    "Neutral",
    "Low",
    "Dutch"
]

LEVEL_CLASSES = [
    "Aerial",
    "Eye",
    "Shoulder",
    "Hip",
    "Knee",
    "Ground"
]


# ============================================================
# CINESCALE MODEL
# ============================================================

class CineScaleModel(nn.Module):

    def __init__(self):
        super().__init__()

        # ResNet-18 backbone
        self.resnet = models.resnet18(weights=None)

        # CineScale checkpoint uses a 512-dimensional
        # feature layer instead of the normal 1000 classes.
        self.resnet.fc = nn.Linear(
            512,
            512
        )

        # Camera angle classification head
        self.angle_head = nn.Linear(
            512,
            5
        )

        # Camera level classification head
        self.level_head = nn.Linear(
            512,
            6
        )

    def forward(self, x):

        # ResNet feature extraction
        x = self.resnet.conv1(x)
        x = self.resnet.bn1(x)
        x = self.resnet.relu(x)
        x = self.resnet.maxpool(x)

        x = self.resnet.layer1(x)
        x = self.resnet.layer2(x)
        x = self.resnet.layer3(x)
        x = self.resnet.layer4(x)

        x = self.resnet.avgpool(x)
        x = torch.flatten(x, 1)

        # 512-dimensional CineScale feature representation
        features = self.resnet.fc(x)

        # Two independent prediction heads
        angle_output = self.angle_head(features)
        level_output = self.level_head(features)

        return angle_output, level_output


# ============================================================
# LOAD CINESCale MODEL
# ============================================================

def load_cinescale_model():

    project_root = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    model_path = os.path.join(
        project_root,
        "models",
        "model.ckpt"
    )

    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"CineScale model not found:\n{model_path}"
        )

    print("Loading checkpoint...")

    checkpoint = torch.load(
        model_path,
        map_location="cpu",
        weights_only=False
    )

    state_dict = checkpoint["state_dict"]

    model = CineScaleModel()

    model.load_state_dict(
        state_dict,
        strict=True
    )

    model.eval()

    print("CineScale model loaded successfully!")

    return model


# ============================================================
# IMAGE TRANSFORMATION
# ============================================================

image_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# ============================================================
# CAMERA ANALYSIS
# ============================================================

def analyze_camera(image_path):

    model = load_cinescale_model()

    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Image not found:\n{image_path}"
        )

    image = Image.open(
        image_path
    ).convert("RGB")

    input_tensor = image_transform(
        image
    )

    input_tensor = input_tensor.unsqueeze(0)

    with torch.no_grad():

        angle_output, level_output = model(
            input_tensor
        )

        angle_probabilities = torch.softmax(
            angle_output,
            dim=1
        )

        level_probabilities = torch.softmax(
            level_output,
            dim=1
        )

        angle_index = torch.argmax(
            angle_probabilities,
            dim=1
        ).item()

        level_index = torch.argmax(
            level_probabilities,
            dim=1
        ).item()

    angle = ANGLE_CLASSES[
        angle_index
    ]

    level = LEVEL_CLASSES[
        level_index
    ]

    angle_confidence = (
        angle_probabilities[
            0,
            angle_index
        ].item() * 100
    )

    level_confidence = (
        level_probabilities[
            0,
            level_index
        ].item() * 100
    )

    return {
        "camera_angle": angle,
        "camera_angle_confidence": round(
            angle_confidence,
            2
        ),
        "camera_level": level,
        "camera_level_confidence": round(
            level_confidence,
            2
        )
    }


# ============================================================
# TEST
# ============================================================

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

        print("\nLoading CineScale model...\n")

        results = analyze_camera(
            image_path
        )

        print(
            "\n========== CINEMATIC CAMERA ANALYSIS ==========\n"
        )

        print(
            "Camera Angle:",
            results["camera_angle"]
        )

        print(
            "Angle Confidence:",
            str(
                results[
                    "camera_angle_confidence"
                ]
            ) + "%"
        )

        print(
            "Camera Level:",
            results["camera_level"]
        )

        print(
            "Level Confidence:",
            str(
                results[
                    "camera_level_confidence"
                ]
            ) + "%"
        )

        print(
            "\n===============================================\n"
        )

    except Exception as e:

        print("\nERROR:")
        print(e)
