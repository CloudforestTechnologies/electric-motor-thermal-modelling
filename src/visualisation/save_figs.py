'''
save_figs

This file supports saving figures with a particular configuration.

'''

# Module Importations
from datetime import datetime

# Helper Method for saving figures
def generate_fig_save_string(filename):
    """Save Figures
    ======================================
    Saves figures using prescribed filename, date/timestamp and directory.
    
    Args:
        filename (string) - Filename to be used for figure.
        
    Returns:
        save_string (string) - String to use for saving file.
    """

    # Save files to project
    filedirectory = r'C:/Developer/electric_motor_thermal_modelling/Reports/Figures'

    # Retrieve timestamp
    timestamp = datetime.now()
    timestamp_str = timestamp.strftime('%Y_%m_%d-%H_%M_%S')

    # Create filepath
    filepath = filedirectory + '/' + 'YC_' + filename + '_' + timestamp_str + '.png'

    # Return save string
    return filepath