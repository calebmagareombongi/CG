import os
import json
import pandas as pd
from multiprocessing import Pool

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

    # Function to split and save data for a specific language
    def split_and_save_language(language_code, language_data):
        train_data = language_data[:train_split]
        test_data = language_data[train_split:test_split]
        dev_data = language_data[test_split:]

        # Convert DataFrames to JSONL format and save with language-specific file names
        train_df = pd.DataFrame(train_data)
        test_df = pd.DataFrame(test_data)
        dev_df = pd.DataFrame(dev_data)

        train_df.to_json(os.path.join(output_dir, f'{language_code}_train.jsonl'), orient='records', lines=True)
        test_df.to_json(os.path.join(output_dir, f'{language_code}_test.jsonl'), orient='records', lines=True)
        dev_df.to_json(os.path.join(output_dir, f'{language_code}_dev.jsonl'), orient='records', lines=True)

        split_data['train'].extend(train_data)
        split_data['test'].extend(test_data)
        split_data['dev'].extend(dev_data)

    # Use multiprocessing to split and save data for each language in parallel
    with Pool() as pool:
        pool.starmap(split_and_save_language, data.items())

    # Save split data
    for split_type, split_items in split_data.items():
        with open(os.path.join(output_dir, f'{split_type}_split.jsonl'), 'w') as split_file:
            for item in split_items:
                split_file.write(json.dumps(item) + '\n')
