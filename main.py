import argparse
import os
import json
import pandas as pd
import functions
import functions2

# This function creates the flag and calls arguments.
def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Process the dataset and generate Excel files for different languages.')
    parser.add_argument('--input_dir', type=str, help='Input directory containing JSONL files.')
    parser.add_argument('--output_dir', type=str, help='Output directory for generated files.')
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.input_dir is None:
        input_dir = input("Please enter the full path to the JSONL dataset directory: ")
    else:
        input_dir = args.input_dir

    if args.output_dir is None:
        output_dir = input("Please enter the full path to the output directory: ")
    else:
        output_dir = args.output_dir

    os.makedirs(output_dir, exist_ok=True)

    # Load data from JSONL files
    data = functions.load_data(input_dir)

    # Generate Excel files for all languages
    functions.generate_excel_files(data, output_dir, pivot_language='en')

    # Split and save data
    functions2.split_and_save_data(data, output_dir)

if __name__ == "__main__":
    main()
