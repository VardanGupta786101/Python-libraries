import pandas as pd
import json
from errors import DatasetNotFoundError, InvalidDatasetError

class InMemoryDatasetManager:
    def __init__(self):
        self.datasets = {}

    def add_dataset(self, key, dataset):
        self.datasets[key] = dataset

    def get_dataset(self, key):
        dataset = self.datasets.get(key)
        if dataset is None:
            raise DatasetNotFoundError(key)
        return dataset

    def list_datasets(self):
        return list(self.datasets.keys())

    def remove_dataset(self, key):
        if key in self.datasets:
            del self.datasets[key]

    def dataset_to_json(self, key):
        try:
            dataset = self.get_dataset(key)
            return dataset.to_json(orient='records')
        except Exception as e:
            raise InvalidDatasetError(key, underlying_error=e)

    def load_dataset_from_json(self, key, json_data):
        try:
            dataset = pd.read_json(json_data, orient='records')
            self.add_dataset(key, dataset)
        except Exception as e:
            raise InvalidDatasetError(key, underlying_error=e)
