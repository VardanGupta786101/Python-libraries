import os
import pandas as pd
import pickle
from errors import DatasetNotFoundError, InvalidDatasetError

class DatabasedDatasetManager:
    def __init__(self, storage_path='dataset_manager/file_storage/'):
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)

    def save_dataset(self, key, dataset):
        dataset_path = os.path.join(self.storage_path, f"{key}.pkl")
        with open(dataset_path, 'wb') as f:
            pickle.dump(dataset, f)

    def load_dataset(self, key):
        dataset_path = os.path.join(self.storage_path, f"{key}.pkl")
        if not os.path.exists(dataset_path):
            raise DatasetNotFoundError(key)
        try:
            with open(dataset_path, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            raise InvalidDatasetError(key, underlying_error=e)

    def list_datasets(self):
        return [file.replace('.pkl', '') for file in os.listdir(self.storage_path) if file.endswith('.pkl')]

    def delete_dataset(self, key):
        dataset_path = os.path.join(self.storage_path, f"{key}.pkl")
        if os.path.exists(dataset_path):
            os.remove(dataset_path)
