from Manager.FoodManager import FoodManager

class MainMenu:

    __options={1:'Show Restaurants',2:'Show FoodItems',3:'Search Restaurants',4:'Search FoodItems',5:'Logout'} # private class variable 
    __curentuser=''

    def __init__(self):
        self.__FoodManager=FoodManager()

    def ShowRestaurants(self):
        for i,res in enumerate(self.__FoodManager.Restaurants,1) :
            res.DisplayDetails(i)
         
    def ShowFoodItems(self):
        pass
    def SearchRestaurants(self):
        pass
    def SearchFoodItems(self):
        pass
    def Logout(self):
        print(f'Thank You {MainMenu.__curentuser.name}')
        exit()

    def Start(self,user):

        MainMenu.__curentuser=user

        while True:
            print(f'\n\nWelcome { user.name} to Online Food Order Platform')
            print()
            for option in MainMenu.__options:
                print(f'{option}.{MainMenu.__options[option]}',end=" ")
            print() 
            try:
                choice=int(input("Enter Your Choices: ") )  
                valu=MainMenu.__options[choice].replace(' ','')
                getattr(self,valu)()
            except(ValueError,KeyError):
                print(" Invaild Inputs or Invaild Choices ")



