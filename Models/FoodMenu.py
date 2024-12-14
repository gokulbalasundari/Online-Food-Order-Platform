from Models.AbstractModels import AbstractItem

class  FoodMenu(AbstractItem):
    def __init__(self,name):
        super.__init__(name)
        self.FoodItem=[]