from abc import ABC, abstractmethod


class PyAtomRepository(ABC):

    #persiste no db
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def save(self, obj):
        pass

    @abstractmethod
    def save(self, obj, db):
        pass

    @abstractmethod
    def save(self, obj, con):
        pass

    #methods get
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def getById(self, obj):
        pass

    @abstractmethod
    def getAll(self):
        pass

    #execute queryes
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def execute(self):
        pass
