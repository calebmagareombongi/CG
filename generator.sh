#!/bin/bash

# Activate your virtual environment if you are using one
# source /path/to/your/virtualenv/bin/activate

# Navigate to the directory where your Python scripts are located
# The assumption is that your generator.sh script is in the same directory as main.py
cd "$(dirname "$0")"

# Run the main.py script with the necessary arguments
# Use the GitHub URL for the raw content of main.py
python main.py --input_dir /path/to/your/input_directory --output_dir /path/to/your/output_directory

# Deactivate the virtual environment if you activated one
# deactivate

# Exit with a success status code (0) if everything completes successfully
exit 0
