from abc import ABC, abstractmethod
from typing import List, TypeVar

from dal.data_sources.data_source import DataSource

T = TypeVar('T')

class Repository(ABC):

    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    @abstractmethod
    def get_all(self) -> List[T]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int) -> T:
        raise NotImplementedError

    @abstractmethod
    def create(self, item: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def update(self, item: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def delete(self, item: T) -> None:
        raise NotImplementedError
