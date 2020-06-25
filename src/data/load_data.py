'''
load_data

This file supports loading project data into memory.

'''

# Module importations
import pandas as pd

def load_motor_data():
    """Load Dataset
    ======================================
    Loads dataset from user-specified directory.
    
    Args:
        None.
        
    Returns:
        dataframe (dataframe) - Dataframe loaded with data from csv.
    """

    file_string = r'C:\Users\ASUS-PC\OneDrive\Cloudforest Technologies\M. Projects\Yellow Cuckoo\pmsm_temperature_data.csv'
    
    return pd.read_csv(file_string)