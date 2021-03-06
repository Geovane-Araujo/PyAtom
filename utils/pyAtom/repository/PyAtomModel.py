import json
from abc import ABC, abstractmethod
class PyAtomModel(ABC):

    @classmethod
    def __id__(self):
        return ""

    @classmethod
    def __fk__(self):
        return []

    @classmethod
    def __listObject__(self):
        return []

    @classmethod
    def __simpleObject__(self):
        return []

    @classmethod
    def __noEntity__(self):
        return False

    @classmethod
    def __tableName__(self):
        return ""

    @classmethod
    def __union__(self):
        return ""

    @classmethod
    def __ignore__(self):
        return []

    @classmethod
    def __alias__(self):
        pass

    @classmethod
    def __join__(self):
        pass

    @classmethod
    def toJson(self, obj):
        return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @classmethod
    def toArray(self, obj):
        arra = []
        for fl in obj:
            arra.append(self(fl))
        return arra