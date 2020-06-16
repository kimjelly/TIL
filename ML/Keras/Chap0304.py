import os
# For AMD GPU usage
# If you want to use AMD GPU, do not import keras from tensorflow
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

# Binary classification

from keras.datasets import imdb
from keras import models
from keras import layers
import numpy as np

# data import
## Workaround error 'Object arrays cannot be loaded when allow_pickle=False'

# save np.load
np_load_old = np.load
# modify the default parameters of np.load
np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)
# call load_data with allow_pickle implictly set to True
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
# restore np.load for future normal usage
np.load = np_load_old

# list([1, 14, 20, 47, 111, 439, 3445, 19, 12, 15, 166, 12, 216, 125, 40, 6, 364, 352, 707, 1187, 39, 294, 11, 22, 396, 13, 28, 8, 202, 12, 1109, 23, 94, 2, 151, 111, 211, 469, 4, 20, 13, 258, 546, 1104, 7273, 12, 16, 38, 78, 33, 211, 15, 12, 16, 2849, 63, 93, 12, 6, 253, 106, 10, 10, 48, 335, 267, 18, 6, 364, 1242, 1179, 20, 19, 6, 1009, 7, 1987, 189, 5, 6, 8419, 7, 2723, 2, 95, 1719, 6, 6035, 7, 3912, 7144, 49, 369, 120, 5, 28, 49, 253, 10, 10, 13, 1041, 19, 85, 795, 15, 4, 481, 9, 55, 78, 807, 9, 375, 8, 1167, 8, 794, 76, 7, 4, 58, 5, 4, 816, 9, 243, 7, 43, 50])], ...
#print(train_data[:1])
# [1 0 0 1 0 0 1 0 1 0]
#print(train_labels[:10])


# Tensor conversion needed
## 1. Add paddings on train_data to make all lists have same length
##    then convert to integer tensor - size (samples, seq_length)
##    And introduce embedding layer as a first layer to handle integer tensor
## 2. Convert train_data to 0-1 vector using one-hot encoding
## I'll use the latter approach

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')


# Define NN model
## Input: vector / Label: scalar
## FCC with ReLU

model = models.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(10000, )))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(
    optimizer='rmsprop',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
# model.compile(
#   optimizer=optimizers.RMSprop(lr=0.001), 
#   loss=losses.binary_crossentropy,
#   metrics=[metrics.binary_accuracy]
# )


# Validation set preparation
x_val = x_train[:10000]
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

## acc, loss, val_acc, val_loss
history = model.fit(
    partial_x_train, partial_y_train, 
    epochs=20, batch_size=512, 
    validation_data=(x_val, y_val)
)


# Draw graphs
import matplotlib.pyplot as plt

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Overfitting shows around 3~4 epoch.