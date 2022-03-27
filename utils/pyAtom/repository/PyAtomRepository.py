from abc import ABC, abstractmethod


class PyAtomRepository(ABC):

    #persiste no db
    @classmethod
    def save(self):
        pass

    @classmethod
    def save(self, obj):
        pass

    @classmethod
    def save(self, obj, db):
        pass

    @classmethod
    def save(self, obj, con):
        pass

    #methods get
    @classmethod
    def get(self):
        pass

    @classmethod
    def getById(self, obj):
        pass

    @classmethod
    def getAll(self):
        pass

    #execute queryes
    @classmethod
    def execute(self):
        pass

    @classmethod
    def execute(self):
        pass
