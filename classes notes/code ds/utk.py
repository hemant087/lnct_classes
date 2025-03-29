# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


import numpy as np
import pandas as pd
import os
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import Dense, MaxPooling2D, Conv2D, Dropout, Flatten, BatchNormalization, Input, Activation
from tensorflow.keras.models import Model
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
# Load data and preprocess images
fldr = "/kaggle/input/utkface-new/UTKFace"
files = os.listdir(fldr)
ages, genders, images = [], [], []

# Read and preprocess images
for file in files:
    age = int(file.split('_')[0])
    gender = int(file.split("_")[1])
    ages.append(age)
    genders.append(gender)
    total = fldr + "/" + file
    image = cv2.imread(total)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (64, 64))
    images.append(image)

image_f = np.array(images)
age_f = np.array(ages)
gender_f = np.array(genders)

# Normalize images
image_f_2 = image_f / 255.0

# Scale ages to range [0, 1]
age_max = np.max(age_f)
age_f = age_f / age_max  # Scaling the age values to [0, 1]


# Prepare labels (age, gender)
labels = [[ages[i], genders[i]] for i in range(len(ages))]
label_f = np.array(labels)

# Split data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(image_f_2, label_f, test_size=0.2)

# Split labels into separate outputs for age and gender
y_train_2 = [y_train[:, 1], y_train[:, 0]]
y_test_2 = [y_test[:, 1], y_test[:, 0]]

# Convolution block function with batch normalization and dropout
def convolution(input_tensor, filters):
    x = Conv2D(
        filters=filters,
        kernel_size=(3, 3),
        padding="same",
        strides=(1, 1),
        kernel_regularizer=l2(0.001),
    )(input_tensor)
    x = BatchNormalization()(x)
    x = Activation("relu")(x)
    x = Dropout(0.2)(x)
    return x


# Define the model architecture
def model(input_shape):
    inputs = Input(shape=input_shape)
    
    conv_1 = convolution(inputs, 512)
    maxp_1 = MaxPooling2D(pool_size=(2, 2))(conv_1)

    conv_2 = convolution(maxp_1, 256)
    maxp_2 = MaxPooling2D(pool_size=(2, 2))(conv_2)
    
    conv_3 = convolution(maxp_2, 128)
    maxp_3 = MaxPooling2D(pool_size=(2, 2))(conv_3)

    conv_4 = convolution(maxp_3, 64)
    maxp_4 = MaxPooling2D(pool_size=(2, 2))(conv_4)

  conv_5 = convolution(maxp_4, 32)
    maxp_5 = MaxPooling2D(pool_size=(2, 2))(conv_5)

    flatten = Flatten()(maxp_5)
    dense_1 = Dense(64, activation="relu")(flatten)
    dense_2 = Dense(64, activation="relu")(flatten)

    drop_1 = Dropout(0.2)(dense_1)
    drop_2 = Dropout(0.2)(dense_2)


    output_1 = Dense(1, activation="sigmoid", name="sex_out")(drop_1)
    output_2 = Dense(1, activation="linear", name="age_out")(drop_2)

    model = Model(inputs=inputs, outputs=[output_1, output_2])
    
    model.compile(
        loss=["binary_crossentropy", "mse"],  # Binary crossentropy for gender and MSE for age
        optimizer=Adam(),
        metrics={"sex_out": "accuracy", "age_out": "mae"},
    )
    return model

# Instantiate the model
input_shape = (64, 64, 3)
model_instance = model(input_shape)

# Print the model summary
print(model_instance.summary())

# Callbacks: ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
checkpoint = ModelCheckpoint(
    filepath='/kaggle/working/age_sex_detection.keras',  # Path to save the model
    monitor='val_loss',  # Monitor validation loss
    verbose=1,
    save_best_only=True,
    save_weights_only=False,
    mode='auto',
    save_freq='epoch'
)
early_stop = EarlyStopping(
    patience=75,
    monitor='val_loss',
    restore_best_weights=True
)

reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=20,
    min_lr=1e-6
)

callbacks = [checkpoint, early_stop, reduce_lr]
# Train the model
history = model_instance.fit(
    x_train,  # Training data
    y_train_2,  # Labels
    batch_size=32,  # Batch size
    validation_data=(x_test, y_test_2),  # Validation data
    epochs=250,  # Number of epochs
    callbacks=callbacks  # Callbacks
)


# Evaluate the model on the test set
model_instance.evaluate(x_test, y_test_2)

# Generate predictions
pred = model_instance.predict(x_test)

# Plot actual vs predicted ages
predicted_ages = pred[1].flatten()
actual_ages = y_test_2[1].flatten()


# Create scatter plot
plt.figure(figsize=(8, 8))
plt.scatter(actual_ages, predicted_ages, alpha=0.6, edgecolor='k', label='Predictions')
plt.plot([actual_ages.min(), actual_ages.max()], [actual_ages.min(), actual_ages.max()], 'r--', lw=2, label='Ideal Fit Line')
plt.xlabel('Actual Age')
plt.ylabel('Predicted Age')
plt.title('Actual vs. Predicted Ages')
plt.legend()
plt.show()

# Classification report and confusion matrix for gender
pred_l = [int(np.round(pred[0][i])) for i in range(len(pred[0]))]
report = classification_report(y_test_2[0], pred_l)
print(report)

result = confusion_matrix(y_test_2[0], pred_l)
sns.heatmap(result, annot=True)
plt.show()

# Test image function (display prediction for a single image)
def test_image(ind, image_f, image_f_2, model_instance):
    plt.imshow(image_f[ind])
    plt.show()
    image_test = image_f_2[ind]
    pred_l = model_instance.predict(np.array([image_test]))
    sex_f = ['male', 'female']
    age = int(np.round(pred_l[1][0] * age_max))  # Denormalize age
    sex = int(np.round(pred_l[0][0]))
    print(f"Predicted Age: {age}, Predicted Sex: {sex_f[sex]}")

# Test with an example image
test_image(9, image_f, image_f_2, model_instance
