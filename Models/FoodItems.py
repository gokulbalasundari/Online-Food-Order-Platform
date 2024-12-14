from Models.AbstractModels import AbstractItem

class FoodItem(AbstractItem):
    def __init__(self,name,rating,price,describtion):
        super().__init__(name,rating)
        self.price=price
        self.describtion=describtion

    def DisplayDetails(self, index):
        print(f'\n {index}.{self.name} => {self.rating} => {self.price} => {self.describtion}')
        return     