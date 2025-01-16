from abc import ABC, abstractmethod
from typing import Any

class DataSource(ABC):


    @abstractmethod
    def create_data(self, data: Any, *args, **kwargs) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def read_data(self, *args, **kwargs) -> Any:
        raise NotImplementedError
    
    @abstractmethod
    def update_data(self, data: Any, *args, **kwargs) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def delete_data(self, data: Any, *args, **kwargs) -> None:
        raise NotImplementedError

    