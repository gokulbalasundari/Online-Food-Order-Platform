from Models.AbstractModels import AbstractItem
from Models.FoodMenu import FoodMenu

class Restaurants(AbstractItem):

    def __init__(self,name,rating,location,offer):
     
        super().__init__(name,rating)
        self.location=location
        self.offer=offer
        self.__FoodMenu=[]

    @property
    def FoodMenu(self):
        return self.__FoodMenu
    
    @FoodMenu.setter
    def FoodMenu(self,FoodMenus):

        for menu in FoodMenus:
            if not isinstance(menu,FoodMenu):
                print('\nThe Menu was Not in FoodMenus')
                return
        self.__FoodMenu=FoodMenus

    def DisplayDetails(self, index):
        print(f'\n{index}.Name :{self.name}  Rating :{self.rating}  Location:{self.location}')
        return
    

