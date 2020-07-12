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

    # Location files are saved
    #save_directory = r'C:\Users\ASUS-PC\OneDrive\Cloudforest Technologies\M. Projects\Yellow Cuckoo\Figures'

    # Retrieve timestamp
    timestamp = datetime.now()
    timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')

    # Create filename
    filename = filename + ' ' + timestamp_str + '.png'

    # Return save string
    #save_string = save_directory + '\\' + filename
    #save_string = os.path.join(save_directory, filename)
    return filename