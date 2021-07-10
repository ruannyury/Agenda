from abc import ABC, abstractmethod
from typing import Dict, Type, Union


class DatabaseInterface(ABC):

    @abstractmethod
    def select_one(self):
        pass


class MysqlRepository(DatabaseInterface):

    def select_one(self) -> Dict:
        return {
            'sucess': True,
            'data': 'Ola mundo'
        }


class UseCase:

    def __init__(self, repository: Type[DatabaseInterface]):
        self.__repository = repository

    def do_something(self, data: bool) -> Union[Dict, None]:
        if data is True:
            repositoryResponse = self.__repository.select_one()
            return repositoryResponse
        return None


class UseCaseFactory:

    @staticmethod
    def create() -> UseCase:
        return UseCase(MysqlRepository())


if __name__ == '__main__':
    usecase = UseCaseFactory.create()

    response = usecase.do_something(True)
    print(response)
