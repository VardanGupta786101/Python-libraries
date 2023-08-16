class DatasetNotFoundError(Exception):
    def __init__(self, key):
        self.message = f"Dataset '{key}' not found."
        super().__init__(self.message)

class InvalidDatasetError(Exception):
    def __init__(self, key, underlying_error=None):
        self.message = f"Error with dataset '{key}': {underlying_error}" if underlying_error else f"Invalid dataset '{key}'."
        super().__init__(self.message)
