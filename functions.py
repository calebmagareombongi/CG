import argparse
import os
import json
import pandas as pd


# This function creates the flag and calls arguments.
def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Process the dataset and generate Excel files for different languages.')
    parser.add_argument('--input_dir', type=str, help='Input directory containing JSONL files.')
    parser.add_argument('--output_dir', type=str, help='Output directory for generated Excel files.')
    return parser.parse_args()


# This helps specify the language code
def generate_excel_files(data, output_dir, pivot_language='en'):
    os.makedirs(output_dir, exist_ok=True)

    # Get the list of available language codes (excluding the pivot language)
    available_languages = [lang_code for lang_code in data.keys() if lang_code != pivot_language]

    # Prompt the user to select a language code
    print("Available language codes (excluding pivot language):", available_languages)
    target_language = input("Enter the language code for which you want to generate an Excel file: ")

    # Check if the selected language code is valid
    if target_language not in available_languages:
        print("Invalid language code. Please select a valid language code.")
        return


# This function loads the data from the specified input directory that contains the JSONL files.
def load_data(input_dir):
    data = {}
    for filename in os.listdir(input_dir):
        if filename.endswith(".jsonl"):
            language_code = os.path.splitext(filename)[0]
            data[language_code] = []
            with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as file:
                for line in file:
                    json_data = json.loads(line)
                    data[language_code].append({
                        'id': json_data['id'],
                        'utt': json_data['utt'],
                        'annot_utt': json_data['annot_utt']
                    })
    return data


# This function takes the input directory specified and creates the output directory.
# It then detects the language code and processes the data providing an Excel ouput.
# After it is done, it prints out that the Excel files have been generated.

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

    data = load_data(input_dir)

    generate_language_excel = input("Do you want to generate Excel files for a specific language? (y/n): ")
    if generate_language_excel.lower() == 'y':
        # Call the generate_excel_files function to generate Excel for a specific language
        generate_excel_files(data, output_dir, pivot_language='en')  # You can specify the pivot language here.
    else:
        # Generate Excel files for all languages
        for language_code, language_data in data.items():
            df = pd.DataFrame(language_data)
            output_filename = os.path.join(output_dir, f"en-{language_code}.xlsx")
            df.to_excel(output_filename, index=False)

    print("Excel files generated for selected languages.")


if __name__ == "__main__":
    main()
