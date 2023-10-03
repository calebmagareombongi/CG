
# Multilingual Text Data Processing with Python

This repository contains Python scripts to simplify the handling and processing of large multilingual datasets.

## Introduction

Working with multilingual text data can be a challenging task, but this project aims to streamline the process. It includes Python scripts designed to process datasets with English as the reference language, featuring parallel text translations in multiple languages.

## Data Source

The main dataset for this project is available [here](https://drive.google.com/file/d/1I1b5YflUxIMIvqis0a7dCgLGzrkYXrLi/view?usp=drive_link). This dataset contains parallel text translations aligned with English.

## Setup

To set up the environment for this project, follow these steps:

1. Create a virtual environment:
   ```
   python3 -m venv env
   source env/bin/activate
   ```

2. Install the required dependencies:
   ```
   pip install pandas jsonlib2
   ```

## Data Processing

To process the dataset and generate Excel files for each language, follow these steps:

1. Import the dataset mentioned above.
2. Run the following command:
   ```
   python functions.py
   ```

This will execute the data processing functions and create Excel files in the format `en-xx.xlsx` for each language.

## File Generation

Details about file generation:

- The script responsible for splitting data and generating JSONL files can be found in `main2.py`.
- This script takes the dataset and splits it for English, Swahili, and German into train/test/dev files.
- The resulting files are stored in the `data` folder with names like `en_train.jsonl`, etc.
- A comprehensive JSON file containing all translations from English to other languages, complete with unique IDs and utterances, is also generated.

## Functions

### `parse_arguments()`

This function handles command-line arguments.

### `generate_excel_files(data, output_dir, pivot_language='de')`

A function that allows you to specify the pivot language code when generating Excel files.

### `load_data(input_dir)`

This function loads data from a specified input directory that contains JSONL files.

### `main()`

The main function of this project. It processes data from the input directory and creates an output directory. It automatically detects the language code and provides Excel output. Once completed, it notifies you that the Excel files have been generated.

### `split_and_save_data(data, language, folder_path)`

A function for splitting and saving data based on language.

## Usage

To use this project effectively, follow these steps:

1. Set up a virtual environment and install the required dependencies.
2. Execute `python functions.py` to initiate the data processing functions.
3. Run `python main2.py` to split and process the data further.
4. Check the `data` folder for the resulting output files.

Feel free to explore and customize these Python scripts to work with your specific multilingual text data processing needs.
```
