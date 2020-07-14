'''
keras_helpers

Helper routines for building & training neural networks using keras API

'''

# Module Importations
from keras.layers.core import Dense
from keras.models import Sequential
from keras.optimizers import Adam
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def create_multilayer_perceptron(dim):
    """
    Build and return a multilayer perceptron model.
    ======================================

    Input:
        dim (array) - An array used to set the shape of the layers.

    Output:
        model (Sequential) - A multilayer perceptron model designed for the data profile.
    """

    # Define the network
    model = Sequential()
    model.add(Dense(8, input_dim = dim, activation = "relu"))
    model.add(Dense(4, activation = "relu"))
    model.add(Dense(1, activation = "linear"))

    return model

def train_multilayer_perceptron(model, X_train, X_test, y_train, y_test):
    """
    Train a multilayer perceptron model from training data.
    ======================================

    Input:
        model (Sequential) - Multilayer perceptron for training.
        X_train (Array) - Array of training data.
        X_test (Array) - Array of test data.
        y_train (Array) - Array of training data.
        y_test (Array) - Array of test data.

    Output:
        model (Sequential) - Multi-layer perceptron model, fitted to training data.
    """

    # Compile model
    opt = Adam(lr = 1e-3, decay = 1e-3 /200)
    model.compile(loss = "mean_absolute_percentage_error", optimizer = opt)

    # Train model
    print("[mlp nn] Training model ...")
    model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 20, batch_size = 8)

    # Return model
    return model