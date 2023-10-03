import os
import json
import pandas as pd
from multiprocessing import Pool

def load_data_optimized(input_dir):
    data = {}
    file_paths = [os.path.join(input_dir, filename) for filename in os.listdir(input_dir) if filename.endswith(".jsonl")]
    
    def load_file(file_path):
        language_code = os.path.splitext(os.path.basename(file_path))[0]
        data[language_code] = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                json_data = json.loads(line)
                data[language_code].append({
                    'id': json_data['id'],
                    'utt': json_data['utt'],
                    'annot_utt': json_data['annot_utt']
                })

    with Pool() as pool:
        pool.map(load_file, file_paths)

    return data

# ... (rest of the functions.py code remains the same)
