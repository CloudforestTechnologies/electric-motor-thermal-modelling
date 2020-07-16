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
    # Print input dimension
    print("Input Dimension:", dim)

    # Define the network
    model = Sequential()
    model.add(Dense(100, input_dim = dim, activation = "relu"))
    model.add(Dense(60, activation = "relu"))
    model.add(Dense(30, activation = "relu"))
    model.add(Dense(1))

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
    opt = "adam"
    model.compile(loss = "mean_squared_error", optimizer = opt)

    # Train model
    print("[mlp nn] Training model ...")
    model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 20, batch_size = 8)

    # Return model
    return model

def save_sequential_model(model, name):
    """
    Save model to Models folder using described name.
    ======================================

    Input:
        model (Sequential) - The model to be saved.
        name (string) - Model unique identifier

    Output:
        None.
    """

    # Create full filepath, including name
    filepath = r'C:\Developer\electric_motor_thermal_modelling\Models'
    filepath_full = filepath + '\\' + name + '.h5'

    # Save model
    model.save(filepath = filepath_full, overwrite = True, include_optimizer = True, save_format = 'h5')