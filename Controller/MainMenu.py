from Manager.FoodManager import FoodManager

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
       
    def ShowFoodItems(self,res,choice_menu=None):
        print(f'\n{res.name} {choice_menu.name} Food Items')
        print()
        for i,item in enumerate(choice_menu.FoodItem,1):
            item.DisplayDetails(i)
        print()    

        
    def SearchRestaurants(self):
        pass
    def SearchFoodItems(self):
        pass

    def ShowFoodMenus(self,res=None):
        print(f'\n{res.name} Restaurants FoodMenus  ')
        print()
        for i,menu in enumerate(res.FoodMenu,1) :
            menu.DisplayDetails(i)
        print() 

        try:
            choice=int(input("Choice Your FoodMenus : ")) 
            choice_menu=res.FoodMenu[choice-1]
            self.ShowFoodItems(res,choice_menu)

        except(IndexError,ValueError):
            print('Invaid  Choice Retry...')   


            



       
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



