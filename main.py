#%%
import os
import pandas as pd
import mutagen
import mutagen.wave
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import torch
from torch.utils.data import random_split
from genereate_dataset import SoundDS
from build_model import AudioClassifier
from predict_model import inference
from device import check_device
from pathlib import Path
from train_model import *

def read_metadata():
    download_path = Path.cwd()

  
    metadata_file = download_path / 'metadata' / 'UrbanSound8K.csv'
    try:
        df = pd.read_csv(metadata_file)
        print(df.head())  

    
        df['relative_path'] = '/fold' + df['fold'].astype(str) + '/' + df['slice_file_name'].astype(str)
 
        df = df[['relative_path', 'classID']]
        print(df.head())  
        return df
    except FileNotFoundError:
        print("Metadata file not found. Please check the path and try again.")
        return None


df = read_metadata()
 

#%% DEVICE CHECK
check_device()

myds = SoundDS(df, Path.cwd() / 'audio')

num_items = len(myds)

num_train = round(num_items * 0.8)
num_val = num_items - num_train
train_ds, val_ds = random_split(myds, [num_train, num_val])
train_dl = torch.utils.data.DataLoader(train_ds, batch_size=16, shuffle=True)
val_dl = torch.utils.data.DataLoader(val_ds, batch_size=16, shuffle=False)

myModel = AudioClassifier()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
myModel = myModel.to(device)
#%%
training(myModel, train_dl, 35)
# Check that it is on Cuda
next(myModel.parameters()).device

inference(myModel, val_dl)

# %%
