from abc import ABC 
class AbstractItem( ABC):
    def __init__(self,name,rating=None):
        self.name=name
        self.rating=rating
