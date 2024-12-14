from Models.AbstractModels import AbstractItem

class Restaurants(AbstractItem):

    def __init__(self,name,rating,location,offer):
        self.name=name
        self.rating=rating
        self.location=location
        self.offer=offer
        self.FoodMenu=[]