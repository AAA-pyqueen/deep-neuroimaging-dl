import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

def build_model(input_shape):
    model = models.Sequential([
        layers.Conv3D(32, (3,3,3), activation='relu', input_shape=input_shape),
        layers.MaxPooling3D((2,2,2)),
        layers.Conv3D(64, (3,3,3), activation='relu'),
        layers.MaxPooling3D((2,2,2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')  # Binary
    ])
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model
