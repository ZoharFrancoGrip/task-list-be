import json
from typing import List

from dal.repositories.repository import Repository
from dal.data_sources.data_source import DataSource
from models.task import Task


class TaskRepository(Repository):

    def __init__(self, data_source: DataSource):
        super().__init__(data_source)


    def load_tasks(self) -> List[Task]:
        raw_data = self.data_source.read_data()
        if raw_data:
            return [Task(**task) for task in json.loads(raw_data)]
        else:
            return []
        
    def dump_tasks(self, tasks: List[Task]) -> None:
        raw_tasks = json.dumps([task.dict() for task in tasks])
        return raw_tasks

    def get_all(self) -> List[Task]:
        return self.load_tasks()

    def create(self, item: Task) -> Task:
        tasks = self.get_all() + [item]
        return self.data_source.create_data(self.dump_tasks(tasks))

    def update(self, item: Task) -> Task:
        tasks = self.get_all()
        updated_tasks = [task for task in tasks if task.id != item.id] + [item]
        return self.data_source.update_data(self.dump_tasks(updated_tasks))

    def delete(self, id: int) -> bool:
        tasks = self.get_all()
        tasks_after_delete = [task for task in tasks if task.id != id]
        return self.data_source.update_data(self.dump_tasks(tasks_after_delete))

