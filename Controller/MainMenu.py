from Manager.FoodManager import FoodManager
from Models.Cart import Cart

class MainMenu:

    __options={1:'Show Restaurants',2:'Show FoodItems',3:'Search Restaurants',4:'Search FoodItems',5:'Logout'} # private class variable 
    __curentuser=''

    def __init__(self):
        self.__FoodManager=FoodManager()

    def ShowRestaurants(self):

        for i,res in enumerate(self.__FoodManager.Restaurants,1) :
            res.DisplayDetails(i)
        print()    
        try:    
            choice=int(input('Choice Your Restaurants : ')) 
            choice_res=self.__FoodManager.Restaurants[choice-1]
            self.ShowFoodMenus(choice_res)

        except(IndexError,ValueError):
            print('Invaid  Choice Retry...')   
       
    def ShowFoodMenus(self,res=None):
        print(f'\n{res.name} Restaurants FoodMenus  ')
        print()
        for i,menu in enumerate(res.FoodMenu,1) :
            menu.DisplayDetails(i)
        print() 

        try:
            choice=int(input("Choice Your FoodMenus : ")) 
            choice_foodmenu=res.FoodMenu[choice-1]
            self.ShowFoodItems(res,choice_foodmenu)

        except(IndexError,ValueError):
            print('Invaid  Choice Retry...')   


    def ShowFoodItems(self,res=None,foodmenu=None):

        if res and foodmenu:
            print(f'\n{res.name} {foodmenu.name} Food Items')
            print()
            for i,item in enumerate(foodmenu.FoodItem,1):
                item.DisplayDetails(i)
            print()    

            choice=list(map(int,input('Enter FoodItems like 1,2 :').split(',')))
            cart=Cart(choices=choice,res_name=res.name,fooditems=foodmenu.FoodItem)
            cart.ProcessOrder()

        
    def SearchRestaurants(self):
        res_name=input('Enter Your Restaurants Name : ')
        res=self.__FoodManager._FindRestaurants(res_name)
        if res is not None:
            self.ShowFoodMenus(res)
        else:
            print(f'The {res_name} Restaurant was not Found')        


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
            
                choice=int(input("\nEnter Your Choices: ") )  
            
                valu=MainMenu.__options[choice].replace(' ','')
                getattr(self,valu)()

            except(ValueError,KeyError):
                print(" Invaild Inputs or Invaild Choices ")



