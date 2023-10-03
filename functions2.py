import os
import json
import pandas as pd

# Function to split and save data
def split_and_save_data(data, output_dir):
    # Specify proportions for the split
    train_proportion = 0.70
    test_proportion = 0.15
    dev_proportion = 0.15

    # Calculate the split indices
    total_samples = sum(len(language_data) for language_data in data.values())
    train_split = int(train_proportion * total_samples)
    test_split = train_split + int(test_proportion * total_samples)

    # Initialize dictionaries to store split data
    split_data = {
        'train': [],
        'test': [],
        'dev': []
    }

    # Split the data
    for language_code, language_data in data.items():
        train_data = language_data[:train_split]
        test_data = language_data[train_split:test_split]
        dev_data = language_data[test_split:]

        split_data['train'].extend(train_data)
        split_data['test'].extend(test_data)
        split_data['dev'].extend(dev_data)

        # Convert DataFrames to JSONL format and save with language-specific file names
        train_df = pd.DataFrame(train_data)
        test_df = pd.DataFrame(test_data)
        dev_df = pd.DataFrame(dev_data)

        train_df.to_json(os.path.join(output_dir, f'{language_code}_train.jsonl'), orient='records', lines=True)
        test_df.to_json(os.path.join(output_dir, f'{language_code}_test.jsonl'), orient='records', lines=True)
        dev_df.to_json(os.path.join(output_dir, f'{language_code}_dev.jsonl'), orient='records', lines=True)

    # Save split data
    for split_type, split_items in split_data.items():
        with open(os.path.join(output_dir, f'{split_type}_split.jsonl'), 'w') as split_file:
            for item in split_items:
                split_file.write(json.dumps(item) + '\n')

def main():
    # Ask the user for the folder path containing the Excel files
    folder_path = input("Enter the folder path containing your Excel files: ")

    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    # Initialize dictionary to store data for each language
    data_by_language = {}

    # Iterate through Excel files in the folder
    for file in os.listdir(folder_path):
        if file.endswith(".xlsx"):
            file_path = os.path.join(folder_path, file)

            try:
                # Determine the language from the file name
                language = file.split('-')[1].split('.')[0]
                if language not in data_by_language:
                    data_by_language[language] = []

                # Read data from each Excel file
                data = pd.read_excel(file_path)

                # Append data to the respective language list
                data_by_language[language].append(data)

                print(f"Data from '{file}' has been loaded.")
            except Exception as e:
                print(f"An error occurred while loading data from '{file}': {e}")

    # Perform the split and save operation for each language
    for language, language_data in data_by_language.items():
        split_and_save_data(language_data, folder_path)

    # Generate the large JSON file showing translations from en to xx
    large_json_data = {'en_to_xx': data_by_language['en'][0].to_dict(orient='records')}

    # Save the large JSON file
    large_json_file_path = os.path.join(folder_path, 'large_translation.json')
    with open(large_json_file_path, 'w') as json_file:
        json.dump(large_json_data, json_file, indent=4)

    print("Data has been split and saved to JSONL files.")
    print("The large JSON file has been generated.")

if __name__ == "__main__":
    main()
