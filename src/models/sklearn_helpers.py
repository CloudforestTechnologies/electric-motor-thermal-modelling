'''
sklearn_helpers

Helper routines for working with sklearn models

'''

# Module Importations
from sklearn.externals import joblib
import time

project_code = 'YC'

def name_model(model_type):
    """
    Returns a time-stamped model name.
    ======================================

    Input:
        model_type (string) - Type of model.

    Output:
        name (string) - Model name.
    """

    # Generate filename
    timestamp = time.strftime('%Y_%m_%d-%H_%M_%S')
    file_format = '.pkl'

    model_name = project_code + '_' + model_type + '_' + timestamp + file_format

    return model_name

def save_model(model, name):
    """
    Save model to Models folder using described name.
    ======================================

    Input:
        model (Pickle) - The model to be saved.
        name (string) - Model unique identifier

    Output:
        None.
    """
    # Create full filepath
    directory = r'C:\Developer\electric_motor_thermal_modelling\Models'
    filepath_full = directory + '\\' + name
    print("Save Path:", filepath_full) 

    # Save model
    joblib.dump(value = model, filename = filepath_full, compress = 3)