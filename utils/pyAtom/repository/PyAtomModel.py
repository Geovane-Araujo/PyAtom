from abc import ABC, abstractmethod
class PyAtomModel(ABC):

    @abstractmethod
    def id(self):
        pass

    @abstractmethod
    def fk(self):
        pass

    @abstractmethod
    def listObject(self):
        pass

    @abstractmethod
    def simpleObject(self):
        pass

    @abstractmethod
    def noEntity(self):
        pass

    @abstractmethod
    def tableName(self):
        pass

    @abstractmethod
    def union(self):
        pass

    @abstractmethod
    def ignore(self):
        pass

    @abstractmethod
    def alias(self):
        pass

    @abstractmethod
    def join(self):
        pass