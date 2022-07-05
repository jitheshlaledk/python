

from abc import ABC,abstractmethod
class a(ABC):
    @abstractmethod
    def print1(self,name):
        self.name=name
        pass
class b(a):
    def print(self,age):
        self.age=age
        self.name=26
        print(self.name,self.age)

