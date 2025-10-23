from torch.utils.data import Dataset
import torch
import torchvision
import os
import math
import warnings
warnings.filterwarnings('ignore')
from torchvision.transforms import (
    Compose,
    ToTensor,
    Normalize,
    RandomHorizontalFlip,
    RandomVerticalFlip,
    Resize,
    RandomRotation,
    RandomResizedCrop,
    InterpolationMode
)
from matplotlib import pyplot as plt
from einops import rearrange
from PIL import Image
from PIL import UnidentifiedImageError


def get_transforms(do_augmentation=True):
    if do_augmentation:
        return Compose([
            Resize(size=(224, 224), interpolation=InterpolationMode.NEAREST), 
            RandomRotation(degrees=(0, 90)),
            RandomHorizontalFlip(p=0.5),
            RandomVerticalFlip(p=0.5),
            RandomResizedCrop(224, scale=(0.5, 2.0)),
            ToTensor(),
            Normalize(mean=[0.485, 0.456, 0.406],
                      std=[0.229, 0.224, 0.225])
        ])
    else:
        return Compose([
            Resize(size=(224, 224), interpolation=InterpolationMode.NEAREST),
            ToTensor(),
            Normalize(mean=[0.485, 0.456, 0.406],
                      std=[0.229, 0.224, 0.225])
        ])

class USImagesDataset(Dataset): 
    def __init__(self, image_paths, do_augmentation=True):
        self.image_paths = image_paths
        self.transform = get_transforms(do_augmentation)
                
    def __len__(self):
        return len(self.image_paths)
    
    def __getitem__(self, index):
        img_path = self.image_paths[index]

        try:
            img = Image.open(img_path).convert("RGB")
        except (OSError, UnidentifiedImageError) as e:
            print(f"[WARNING] Skipping corrupted image: {img_path} — {str(e)}")
            # Try the next image
            return self.__getitem__((index + 1) % len(self.image_paths))

        img = self.transform(img)
        return img
