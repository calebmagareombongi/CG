# Working with files in Python

This project contains Python scripts to process a large dataset

## Data

The dataset used: https://drive.google.com/file/d/1I1b5YflUxIMIvqis0a7dCgLGzrkYXrLi/view?usp=drive_link.
It contains parallel text translations for multiple languages with English as the pivot language.

## Setup

1. To set up the environment, run python3 -m venv env to create a virtual environment. Then activate it.
2. Install dependencies
   - Pandas
   - JSON
   - OS
3. Import the dataset mentioned above.
4. Run python [functions.py]() to process the MASSIVE dataset and generate en-xx.xlsx files for each 
language.

## File Generation

1. The script to split data and generate JSONL files is in [main2.py]().

2. It takes the dataset and splits English, Swahili and German data into train/test/dev files.

3. These are output to the data folder with names like en_train.jsonl, etc.

4. A large JSON file showing all the translations from en to xx with id and utt for all
the train sets is also generated.

## Functions

### parse_arguments()
Creates the flag and calls arguments.
### generate_excel_files(data, output_dir, pivot_language='de')
This helps specify the language code
### load_data(input_dir)
Loads the data from the specified input directory that contains the JSONL files.
### main()
This function takes the input directory specified and creates the output directory.
It then detects the language code and processes the data providing an Excel ouput.
After it is done, it prints out that the Excel files have been generated.
### split_and_save_data(data, language, folder_path)
Function to split and save data

## Usage
1. Set up virtualenv and install dependencies.
2. Run python [functions.py]().
3. Run python [main2.py]().
4. Check the data folder for output files.

