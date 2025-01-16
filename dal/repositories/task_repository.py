from typing import List

from dal.repositories.repository import Repository
from dal.data_sources.data_source import DataSource
from models.task import Task


class TaskRepository(Repository):

    def __init__(self, data_source: DataSource):
        super().__init__(data_source)

    def get_all(self) -> List[Task]:
        return [Task(**task) for task in self.data_source.read_data()]

    def get_by_id(self, id: int) -> Task:
        return [Task(**task) for task in self.data_source.read_data() if task["id"] == id]

    def create(self, item: Task) -> Task:
        tasks = self.get_all()
        tasks.append(item)
        self.data_source.create_data(tasks)
        return item

    def update(self, item: Task) -> Task:
        tasks = self.get_all()
        tasks[tasks.index(item)] = item
        self.data_source.update_data(tasks)
        return item

    def delete(self, item: Task) -> None:
        tasks = self.get_all()
        tasks.remove(item)
        self.data_source.delete_data(tasks)
