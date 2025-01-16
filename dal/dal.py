from enum import Enum

from pyparsing import C
from dal.data_sources.fs_data_source import FsJsonDataSource
from dal.repositories.task_repository import TaskRepository
from dal.data_sources.data_source import DataSource
from dal.repositories.repository import Repository



class RepositoryConfig:
    data_source: DataSource
    arguments: dict
    
REPOSITORIES_CONFIG = {
    TaskRepository : RepositoryConfig(
        data_source=FsJsonDataSource,
        arguments={"file_path": 'tasks.json'}
    )
}

class RepositoryFactory:

    def get_repository(self, repository_type: Repository):
        return self.build_repository_from_repository_config(repository_type, REPOSITORIES_CONFIG[repository_type])
    
    def build_repository_from_repository_config(self, repository_type: Repository, config: RepositoryConfig):
        return repository_type(config.data_source(**config.arguments))
    
