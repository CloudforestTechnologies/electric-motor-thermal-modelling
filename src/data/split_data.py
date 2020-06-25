'''
split_data

This file supports splitting data into development and validation sets.

'''

# Module importations
import numpy as np
import pandas as pd

def split_train_test(data, test_ratio):
    """Split Training & Test Data
    ======================================
    Splits original dataset into training and evaluation data.
    
    Args:
        data (dataframe) - Original test data.
        test_ratio (int) - Ratio for splitting dataset as training percentage.
        
    Returns:
        data_train (dataframe) - Dataframe with training data slice.
        data_test (dataframe) - Dataframe with testing data slice.
    """

    # Random seed setting ensures identical data split between calls
    np.random.seed(42)
    shuffled_indices = np.random.permutation(len(data))

    test_set_size = int(len(data) * test_ratio)

    # Create slices of test and training indices
    train_indices = shuffled_indices[test_set_size:]
    test_indices = shuffled_indices[:test_set_size]

    return data.iloc[train_indices], data.iloc[test_indices]