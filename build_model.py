import torch
import torch.nn as nn
import torch.nn.init as init

class AudioClassifier(nn.Module):
    def __init__(self, num_classes=10, init_gain=0.1):
        super(AudioClassifier, self).__init__()

        channels = [2, 16, 32, 64, 128]  # Channel sizes for each convolutional layer
        self.conv_layers = nn.Sequential()

        # Create multiple convolutional blocks with ReLU, Batch Normalization, and Dropout
        for i in range(1, len(channels)):
            # Define the convolution layer
            conv = nn.Conv2d(channels[i-1], channels[i], kernel_size=3, stride=2, padding=1)
            relu = nn.ReLU()
            bn = nn.BatchNorm2d(channels[i])
            dropout = nn.Dropout(p=0.25)  # Dropout layer to reduce overfitting

            # Initialize convolutional layers using Kaiming He initialization
            init.kaiming_normal_(conv.weight, nonlinearity='relu', a=init_gain)
            #conv.bias.data.zero_()

            # Naming layers for clarity
            layer_name = f"conv_block_{i}"
            self.conv_layers.add_module(f"{layer_name}_conv", conv)
            self.conv_layers.add_module(f"{layer_name}_relu", relu)
            self.conv_layers.add_module(f"{layer_name}_bn", bn)
            self.conv_layers.add_module(f"{layer_name}_dropout", dropout)

        # Adaptive pooling and linear classifier
        self.ap = nn.AdaptiveAvgPool2d(output_size=(1, 1))
        self.fc = nn.Linear(channels[-1], num_classes)

    def forward(self, x):
        x = self.conv_layers(x)       # Pass through convolutional layers
        x = self.ap(x)                 # Adaptive average pooling
        x = x.view(x.size(0), -1)      # Flatten the output for the linear layer
        x = self.fc(x)                 # Final linear layer
        x = nn.Softmax()(x)            # Softmax output
        return x

