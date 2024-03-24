import requests
import pandas as pd
from glob import glob
import json
import os


def convert_to_csv(files, dest_folder_path):
    for key,value in files.items():
        file_path = f'{dest_folder_path}/' + key.split('\\')[-1][:-4] + 'csv'
        df = pd.DataFrame(value)
        if glob(file_path):
            print(f'WARNING: File {file_path} already exists!!')
        else:
            df.to_csv(file_path, sep=',', index=False, encoding='utf-8')
            print(f'File {file_path} created successfully')


def find_and_load_json_files(source_path):
    files = {}

    files_path = glob(source_path + '/**/*.json', recursive=True)
    for p in files_path:
        with open(p) as f:
            content = json.load(f)
            # flattening the nested data
            files[p] = pd.json_normalize(content)
    return files


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def main():
    folder_path = 'data'
    dest_folder_path = 'extracted'

    files = find_and_load_json_files(folder_path)
    create_dir(dest_folder_path)
    convert_to_csv(files, dest_folder_path)
    

if __name__ == "__main__":
    main()
