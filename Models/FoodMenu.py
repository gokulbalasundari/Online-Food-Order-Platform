from Models.AbstractModels import AbstractItem
from Models.FoodItems import FoodItem

class  FoodMenu(AbstractItem):
    def __init__(self,name):
        super().__init__(name)
        self.__FoodItem=[]

    @property
    def FoodItem(self):
        return self.__FoodItem  
    
    @FoodItem.setter
    def FoodItem(self,Items):
        for Item in Items:
            if not isinstance(Item,FoodItem):
                print('Invaid Food Items ')
        self.__FoodItem=Items       

    def DisplayDetails(self, index):
        print(f'\n{index} => {self.name}')
        return    