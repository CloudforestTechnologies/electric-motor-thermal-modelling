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

def train_multilayer_perceptron(model, dataset, target):
    """
    Train a multilayer perceptron model from training data.
    ======================================

    Input:
        model (Sequential) - Multilayer perceptron for training.
        dataset (dataframe) - Dataframe containing training dataset.
        target (dataframe) - Target data for model training.

    Output:
        model (Sequential) - Multi-layer perceptron model, fitted to training data.
    """

    # Create training and test datasets
    X_train, X_test, y_train, y_test = train_test_split(dataset, target, test_size = 0.2, random_state = 0)

    # Compile model
    opt = Adam(lr = 1e-3, decay = 1e-3 /200)
    model.compile(loss = "mean_absolute_percentage_error", optimizer = opt)

    # Train model
    print("[mlp nn] Training model ...")
    model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 10, batch_size = 8)

    # Make predictions on the test data.
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    print("mlp nn MAE: " + str(mae))

    rmse = mean_squared_error(y_test, y_pred, squared = False)
    print("mlp nn MSE: " + str(rmse))

    # Return model
    return model