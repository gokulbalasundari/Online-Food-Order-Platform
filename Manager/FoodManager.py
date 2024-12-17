from Models.FoodItems import FoodItem
from Models.FoodMenu import FoodMenu
from Models.Restaurants import Restaurants

class FoodManager:

    def __init__(self):
        self.Restaurants=self.__PrepareRestaurants()

    def __PrepareFoodItems(self):

        Item1=FoodItem('ChinkanBiriyani',4.8,200,"***")
        Item2=FoodItem('Mattan Biryani',4.2,300,"***")
        Item3=FoodItem('Rice',4.0,100,"***")
        Item4=FoodItem('Pannir Patter Masala',4.5,130,"***")
        Item5=FoodItem('Fraid Rise',4.9,90,"***")
        Item6=FoodItem('Noodules',4.3,100,"***")

        return [Item1,Item2,Item3,Item4,Item5,Item6]

        
    def __PrepareFoodMenus(self):

        FoodItems=self.__PrepareFoodItems()
        Menu1=FoodMenu('Vedge')
        Menu1.FoodItem=[FoodItems[2],FoodItems[3]]
        Menu2=FoodMenu('Non-Ved')
        Menu2.FoodItem=[FoodItems[0],FoodItems[1]]
        Menu3=FoodMenu('Chanish')
        Menu3.FoodItem=[FoodItems[4],FoodItems[5]]

        return [Menu1,Menu2,Menu3]


    def __PrepareRestaurants(self):

        FoodMenus=self.__PrepareFoodMenus()
        res1=Restaurants('Anapurna',4.5,'Coimbatore','10%')
        res1.FoodMenu=[FoodMenus[0]]
        res2=Restaurants('Muniyadi Vilase',4.8,'Madurai','20%')
        res2.FoodMenu=[FoodMenus[1],FoodMenus[2]]
        res3=Restaurants('KFC',4.2,'Coimbatore','30%')
        res3.FoodMenu=[FoodMenus[2]]
        return [res1,res2,res3]
    
    def FindRestaurants(self,res_name):

        for res in self.Restaurants:
            if res.name==res_name:
                print('\nThe Restanurants was Found..')
                print(f'{res.name}=> Rating: {res.rating}  Location : {res.location} Offer: {res.offer}')
                return res
        return None    
        