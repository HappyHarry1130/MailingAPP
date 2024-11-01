# setup.py
from distutils.core import setup
import py2exe

setup(
    console=['main_ui.py'],  # Use 'windows' instead of 'console' for GUI apps
    options={
        'py2exe': {
            'includes': [],  # Add any additional modules that need to be included
            'excludes': [],  # Add any modules to exclude
            'bundle_files': 1,  # Bundle everything into a single executable
            'compressed': True,  # Compress the library archive
        }
    },
    zipfile=None,  # Include the library archive inside the executable
)