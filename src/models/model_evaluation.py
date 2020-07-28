'''
model_evaluation

Helper routines for evaluating model performance

'''

# Module Importations
from sklearn.metrics import mean_absolute_error


def evaluate_model(model_name, y_true, y_pred):
    """
    Evaluate model using series of metrics.
    ======================================

    Input:

    Output:
        
    """
    mae_eval = evaluate_mae(y_true, y_pred)

def evaluate_mae(y_true, y_pred):

    mae_eval = mean_absolute_error(y_true, y_pred)
    
    return mae_eval

def evaluate_rmse():
    pass

def evaluate_r2():
    pass

def print_evaluation():
    pass