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

# Simulated data
x_dummy = np.random.rand(10, 64, 64, 64, 1).astype(np.float32)
y_dummy = np.random.randint(0, 2, size=(10, 1)).astype(np.float32)

model = build_dummy_3d_cnn()
model.fit(x_dummy, y_dummy, epochs=1, batch_size=2)

model.save("models/brain_classifier_model.h5")
model.save_weights("models/brain_cnn_weights.h5")
