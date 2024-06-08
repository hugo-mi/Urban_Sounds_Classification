#%% IMPORT LIBS
import torch
from torch.utils.data import random_split

from audio_utils import read_metadata
from genereate_dataset import SoundDS
from build_model import AudioClassifier
from predict_model import inference
from device import check_device


#%% IMPORT AUDIO
df = read_metadata()


#%% DEVICE CHECK
check_device()


#%% AUDIO DATAPROCESSING

myds = SoundDS(df, data_path)

#%% SPLIT DATA INTO TRAIN AND TEST SET

# Random split of 80:20 between training and validation
num_items = len(myds)
num_train = round(num_items * 0.8)
num_val = num_items - num_train
train_ds, val_ds = random_split(myds, [num_train, num_val])

# Create training and validation data loaders
train_dl = torch.utils.data.DataLoader(train_ds, batch_size=16, shuffle=True)
val_dl = torch.utils.data.DataLoader(val_ds, batch_size=16, shuffle=False)

#%% BUILD MODEL

# Create the model and put it on the GPU if available
myModel = AudioClassifier()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
myModel = myModel.to(device)
# Check that it is on Cuda
next(myModel.parameters()).device

#%% TRAIN MODEL

#%% MODEL INFERENCE

# Run inference on trained model with the validation set
inference(myModel, val_dl)

#%% EVALUATE MODEL
