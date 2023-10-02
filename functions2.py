import pandas as pd
import os
import json

# Function to split and save data
def split_and_save_data(data, language, folder_path):
    def split_and_save_data(data, language, folder_path):
        # Specify proportions for the split
        train_proportion = 0.70
        test_proportion = 0.15
        dev_proportion = 0.15

        # Calculate the split indices
        total_samples = len(data)
        train_split = int(train_proportion * total_samples)
        test_split = train_split + int(test_proportion * total_samples)

        # Split the data
        train_data = data.iloc[:train_split]
        test_data = data.iloc[train_split:test_split]
        dev_data = data.iloc[test_split:]

        # Convert DataFrames to JSONL format and save with language-specific file names
        train_data.to_json(os.path.join(folder_path, f'{language}_train.jsonl'), orient='records', lines=True)
        test_data.to_json(os.path.join(folder_path, f'{language}_test.jsonl'), orient='records', lines=True)
        dev_data.to_json(os.path.join(folder_path, f'{language}_dev.jsonl'), orient='records', lines=True)


def main():
    # Ask the user for the folder path containing the Excel files
    folder_path = input("Enter the folder path containing your Excel files: ")

    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    # Initialize dictionaries to store data for each language
    data_by_language = {'en': pd.DataFrame(), 'sw': pd.DataFrame(), 'de': pd.DataFrame()}

    # Iterate through Excel files in the folder
    for file in os.listdir(folder_path):
        if file.endswith(".xlsx"):
            file_path = os.path.join(folder_path, file)


            try:
                # Determine the language from the file name
                if 'en' in file:
                    language = 'en'
                elif 'sw' in file:
                    language = 'sw'
                elif 'de' in file:
                    language = 'de'
                else:
                    # Skip files that don't contain language info
                    continue

                # Read data from each Excel file
                data = pd.read_excel(file_path)

                # Concatenate the data from each file into the main DataFrame
                data_by_language[language] = pd.concat([data_by_language[language], data], ignore_index=True)

                print(f"Data from '{file}' has been loaded.")
            except Exception as e:
                print(f"An error occurred while loading data from '{file}': {e}")

    # Perform the split and save operation for each language
    for language, data in data_by_language.items():
        split_and_save_data(data, language, folder_path)

    # Generate the large JSON file showing translations from en to xx
    large_json_data = {'en_to_xx': data_by_language['en'].to_dict(orient='records')}

    # Save the large JSON file
    large_json_file_path = os.path.join(folder_path, 'large_translation.json')
    with open(large_json_file_path, 'w') as json_file:
        json.dump(large_json_data, json_file, indent=4)

    print("Data has been split and saved to JSONL files.")
    print("The large JSON file has been generated.")


if __name__ == "__main__":
    main()
