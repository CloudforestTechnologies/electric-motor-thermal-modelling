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

def build_multilayer_perceptron(n_hidden = 2, n_neurons = 30, input_shape = [8]):
    """
    Build and compile a multilayer perceptron model.
    ======================================

    Input:
        n_hidden (int) = Number of hidden layers in model.
        n_neurons (int) = Number of neurons in hidden layer.
        input_dim (array) - An array used to set the shape of the layers.

    Output:
        model (Sequential) - A multilayer perceptron model designed for the data profile.
    """
    # Print input dimension
    print("Input Dimension:", input_shape)

    # Define the network
    model = Sequential()

    # Create input layer
    model.add(InputLayer(input_shape = input_shape))

    # Add further layers
    for layer in range(n_hidden):
        model.add(Dense(n_neurons, activation = "relu"))

    # Add output layer
    model.add(Dense(1))

    # Compile model
    model.compile(loss = "mse", optimizer = "adam")

    return model

def train_multilayer_perceptron(model, X_train, X_test, y_train, y_test):
    """
    Wrap then train a multilayer perceptron model from training data.
    ======================================

    Input:
        model (Sequential) - Compiled model for training.
        X_train (Array) - Array of training data.
        X_test (Array) - Array of test data.
        y_train (Array) - Array of training data.
        y_test (Array) - Array of test data.

    Output:
        wrapped_model (KerasRegressor) - Trained model, wrapped for use with scikit-learn API.
    """

    # Wrap model for use with scikit learn.
    wrapped_model = KerasRegressor(model)

    # Train model
    print("[mlp nn] Training model ...")
    wrapped_model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 1, callbacks = [keras.callbacks.EarlyStopping(patience = 10)])

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
    print("Save Path:", filepath_full)

    # Save model
    model.save(filepath = filepath_full, overwrite = True, include_optimizer = True)