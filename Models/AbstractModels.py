from abc import ABC,abstractmethod
class AbstractItem( ABC):
    def __init__(self,name,rating=None):
        self.name=name
        self.rating=rating

    @abstractmethod
    def DisplayDetails(self,index):
        pass  
