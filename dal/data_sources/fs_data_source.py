import json
from typing import List

from pydantic import BaseModel
from pyparsing import TypeVar

from dal.data_sources.data_source import DataSource


T = TypeVar("T", bound=BaseModel)

class FsJsonDataSource(DataSource):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def create_data(self, data: str) -> None:
        try:
            with open(self.file_path, "w") as file:
                file.write(data)
        except Exception as e:
            return False
        return True

    def read_data(self) -> str:
        try:
            with open(self.file_path, "r") as file:
                return file.read()
        except Exception as e:
            return ""

    def update_data(self, data: str) -> None:
        try:    
            with open(self.file_path, "w") as file:
                file.write(data)
        except Exception as e:
            return False
        return True

    def delete_data(self) -> None:
        try:
            with open(self.file_path, "w") as file:
                file.write("")
        except Exception as e:
            return False
        return True
