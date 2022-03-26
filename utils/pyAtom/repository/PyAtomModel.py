from abc import ABC, abstractmethod
class PyAtomModel(ABC):

    @abstractmethod
    def __id__(self):
        pass

    @abstractmethod
    def __fk__(self):
        pass

    @abstractmethod
    def __listObject__(self):
        pass

    @abstractmethod
    def __simpleObject__(self):
        pass

    @abstractmethod
    def __noEntity__(self):
        pass

    @abstractmethod
    def __tableName__(self):
        pass

    @abstractmethod
    def __union__(self):
        pass

    @abstractmethod
    def __ignore__(self):
        pass

    @abstractmethod
    def __alias__(self):
        pass

    @abstractmethod
    def __join__(self):
        pass