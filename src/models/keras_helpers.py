'''
keras_helpers

Helper routines for building & training neural networks using keras API

'''

# Module Importations
from keras.models import Sequential
from keras.layers.core import Dense

def create_multilayer_perceptron(dim):
    """
    Build and return a multilayer perceptron model.
    ======================================

    Input:
        dim (array) - An array used to set the shape of the layers.

    Output:
        model (Sequential) - A multilayer perceptron model designed for the data profile.
    """

    # Define the network.
    model = Sequential()
    model.add(Dense(8, input_dim = dim, activation = "relu"))
    model.add(Dense(4, activation = "relu"))
    model.add(Dense(1, activation = "linear"))

    return model

def train_multilayer_perceptron(dataset, target):
    pass