import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import ast
import os
import glob
from PIL import Image

# Modified from CMPT 419 assignment 3 GestureSequenceDataset and HandLandMarkDataset class

class SocialSignalDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        """
        Args:
            dataframe (pd.DataFrame): Pandas DataFrame containing the hand landmarks and labels.
            landmarks_column (str): Name of the column containing the nested lists.
            label_column (str): Name of the column containing the labels.
            sequence_length (int): Number of frames per sequence (default: 30).
            transform (callable, optional): Optional transform to be applied on a sample.
        """
        self.root_dir = root_dir
        # get all images (.png extension) in folder
        self.labels = sorted(glob.glob(os.path.join(self.root_dir, "*.png")))
        self.transform = transform

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        image_path = self.labels[idx]
        # Grayscale transform
        image = Image.open(image_path).convert("L")
        file_name = os.path.basename(image_path).lower()

        if "surprise" in file_name:
            label_idx = 0
        else:
            label_idx = 1
        if self.transform:
            image = self.transform(image)


        return image, label_idx  # (Sequence, Label)   



