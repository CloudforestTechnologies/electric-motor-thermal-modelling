'''
keras_helpers

Helper routines for building & training neural networks using keras API

'''

# Module Importations
from keras.layers import Dense, InputLayer
from keras.models import Sequential
from keras.optimizers import Adam
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import keras
import time

project_code = 'YC'

def build_multilayer_perceptron(n_hidden = 2, n_neurons = 30, learning_rate = 3e-3, input_shape = [11]):
    """
    Build and compile multilayer perceptron model.
    ======================================

    Input:
        n_hidden (int) = Number of hidden layers in model.
        n_neurons (int) = Number of neurons in hidden layer.
        learning_rate (float) = Learning rate for optimiser.
        input_shape (array) - An array used to set the shape of the layers.

    Output:
        model (Sequential) - A multilayer perceptron model designed for the data profile.
    """

    model = Sequential()

    # Create input layer
    model.add(InputLayer(input_shape = input_shape))

    # Add further layers
    for layer in range(n_hidden):
        model.add(Dense(n_neurons, activation = "relu"))

    # Add output layer
    model.add(Dense(1))

    # Compile model
    optimiser = keras.optimizers.SGD(lr = learning_rate)
    model.compile(loss = "mse", optimizer = optimiser)

    return model

def wrap_model():
    """
    Build and wrap keras-TF model for use with scikit-learn API.
    ======================================

    Input:
        None

    Output:
        wrapped_model (KerasRegressor) - Wrapped model for use with scikit-learn API.
    """

    # Build and wrap model.
    wrapped_model = KerasRegressor(build_multilayer_perceptron)

    # Return model
    return wrapped_model

def name_model():
    """
    Returns a time-stamped model name.
    ======================================

    Input:
        None.

    Output:
        name (string) - Model name.
    """
    
    # Generate filename
    timestamp = time.strftime('%Y_%m_%d-%H_%M_%S')
    file_format = '.h5'

    model_name = project_code + '_model_' + timestamp + file_format

    return model_name

def make_save_string(file_name):
    """
    Returns a complete save string for saving a model.
    ======================================

    Input:
        file_name (string) - Filename used in save string.

    Output:
        save_string (string) - Save string for specified model.
    """
    pass

def save_model(model, name):
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
    print("Save Path:", filepath_full)

    # Save model
    model.save(filepath = filepath_full, overwrite = True, include_optimizer = True)