from Models.AbstractModels import AbstractItem

class FoodItem(AbstractItem):
    def __init__(self,name,rating,price,describtion):
        super().__init__(name,rating)
        self.price=price
        self.describtion=describtion

    def DisplayDetails(self, index=None):
        if index:
            print(f'\n{self.name} => Rating :{self.rating}  Price:{self.price}Rs')
            return 
        else:    
            print(f'\n {index}.{self.name} => Rating :{self.rating}  Price:{self.price}Rs')
            return     