import os
# For AMD GPU usage
# If you want to use AMD GPU, do not import keras from tensorflow
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

from keras.datasets import boston_housing

# data import
## Workaround error 'Object arrays cannot be loaded when allow_pickle=False'

import numpy as np

# save np.load
np_load_old = np.load
# modify the default parameters of np.load
np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)
# call load_data with allow_pickle implictly set to True
(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()
# restore np.load for future normal usage
np.load = np_load_old


# data normalization
mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std

test_data -= mean
test_data /= std

from keras import models
from keras import layers

def build_model(shape):
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(shape, )))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae']) 
    return model


# K-fold cross validation
## Separate dataset to K folds, and generate K models
## For each model, train the model by K-1 dividened sets, and test it by the left set
## Validation score := mean of the K validation scores

k = 4
num_val_samples = len(train_data) // k
num_epochs = 100
all_scores = []
for i in range(k):
    print('Fold #', i)
    begin = i * num_val_samples
    end = begin + num_val_samples
    val_data = train_data[begin:end]
    val_targets = train_targets[begin:end]

    # train data: All other dataset
    partial_train_data = np.concatenate([train_data[:begin], train_data[end:]], axis=0)
    partial_train_targets = np.concatenate([train_targets[:begin], train_targets[end:]], axis=0)

    print(len(val_data), len(val_targets), len(partial_train_data), len(partial_train_targets))

    #model = build_model(train_data.shape[1])
    #model.fit(partial_train_data, partial_train_targets, epochs=num_epochs, batch_size=1, verbose=0)
    #val_mse, val_mae = model.evaluate(val_data, val_targets, verbose=0)
    #all_scores.append(val_mae)

#print(all_scores)
#print(np.mean(all_scores))