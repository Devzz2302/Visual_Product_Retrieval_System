import torch
from torchvision import models
from torchvision import transforms
from PIL import Image


class FeatureExtractor:

    def __init__(self):

        self.model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)

        self.model = torch.nn.Sequential(
            *list(self.model.children())[:-1]
        )

        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

    def extract(self, image_path):

        img = Image.open(image_path).convert("RGB")

        tensor = self.transform(img)

        tensor = tensor.unsqueeze(0)

        with torch.no_grad():

            features = self.model(tensor)

        features = features.squeeze()

        features = features.numpy()

        features = features / (
            (features ** 2).sum() ** 0.5
        )

        return features