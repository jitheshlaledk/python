#abstraction

from abc import ABC,abstractmethod
class person(ABC):
    @abstractmethod
    def print(self):
        pass
class person2(person):
    def print1(self):
        print("its")
ob=person2
ob.print1()
