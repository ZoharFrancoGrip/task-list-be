import json
from typing import List

from dal.data_sources.data_source import DataSource


class FsJsonDataSource(DataSource):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def create_data(self, data: List[T]) -> None:
        with open(self.file_path, "w") as file:
            json.dump(data, file)

    def read_data(self) -> List[T]:
        with open(self.file_path, "r") as file:
            return json.load(file)

    def update_data(self, data: List[T]) -> None:
        with open(self.file_path, "w") as file:
            json.dump(data, file)

    def delete_data(self) -> None:
        with open(self.file_path, "w") as file:
            json.dump([], file)
