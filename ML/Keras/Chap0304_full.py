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


# In the previous file, there was overfitting from epoch 3~4
model.fit(x_train, y_train, epochs=4, batch_size=512)
results = model.evaluate(x_test, y_test)
print(results)