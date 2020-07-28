'''
model_evaluation

Helper routines for evaluating model performance

'''

# Module Importations
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

def evaluate_model(model_name, y_true, y_pred):
    """
    Evaluate model using series of metrics.
    ======================================

    Input:

    Output:
        
    """

    # Calculate performance metrics
    mae_eval = evaluate_mae(y_true, y_pred)
    rmse_eval = evaluate_rmse(y_true, y_pred)
    r2_eval = evaluate_r2(y_true, y_pred)

    # Print results
    print_evaluation(model_name, mae_eval, rmse_eval, r2_eval)

def evaluate_mae(y_true, y_pred):

    mae_eval = mean_absolute_error(y_true, y_pred)
    
    return mae_eval

def evaluate_rmse(y_true, y_pred):

    mse_eval = mean_squared_error(y_true, y_pred)

    rmse_eval = np.sqrt(mse_eval)

    return rmse_eval    

def evaluate_r2(y_true, y_pred):
    
    r2_eval = r2_score(y_true, y_pred)

    return r2_eval

def print_evaluation(model_name, mae_eval, rmse_eval, r2_eval):
    
    print(model_name, "mae (Eval):", mae_eval)
    print(model_name, "rmse (Eval):", rmse_eval)
    print(model_name, "r2 (Eval):", r2_eval)