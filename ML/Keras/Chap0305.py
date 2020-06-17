import os
# For AMD GPU usage
# If you want to use AMD GPU, do not import keras from tensorflow
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

from keras.datasets import reuters

# data import
## Workaround error 'Object arrays cannot be loaded when allow_pickle=False'

import numpy as np

# save np.load
np_load_old = np.load
# modify the default parameters of np.load
np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)
# call load_data with allow_pickle implictly set to True
(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)
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

# Convert labels to vector (one-hot encoding)
from keras.utils.np_utils import to_categorical
one_hot_train_labels = to_categorical(train_labels)
one_hot_test_labels = to_categorical(test_labels)


from keras import models
from keras import layers

# model definition
def createModel():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(10000, )))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(46, activation='softmax')) # 46 is not a typo!

    model.compile(
        optimizer='rmsprop',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

model = createModel()

def validation(model, x_train, one_hot_train_labels, epochs):
    train_cnt = 1000
    x_val = x_train[:train_cnt]
    partial_x_train = x_train[train_cnt:]

    y_val = one_hot_train_labels[:train_cnt]
    partial_y_train = one_hot_train_labels[train_cnt:]

    history = model.fit(
        partial_x_train, partial_y_train,
        epochs=epochs, batch_size=512,
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


#validation(model, x_train, one_hot_train_labels, 20)

# from validation(), just 9 epochs of learning is enough
model = createModel()
model.fit(x_train, one_hot_train_labels, epochs=9, batch_size=512)
results = model.evaluate(x_test, one_hot_test_labels)
print(results)