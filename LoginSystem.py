from User import User
from Manager.UserManager import UserManager
from Controller.MainMenu import MainMenu

class LoginSystem:

    def VaildChoice(self,choice):
        
        if choice ==1:
            self.NewUser()
        elif choice ==2:
            self.Login()
        elif choice ==3:
            self.Exit()
        else:
            print('Invaild Choice pls Retry..')


    def NewUser(self):

        name=input('Enter your Name: ')
        age=int(input('Enter your Age: '))
        email=input('enter your email: ')
        password=input('Enter Your Password: ')
        user=User(name=name,age=age,email=email,pwd=password)
        user=UserManager.AddUser(user)
        if user:
            menu=MainMenu()
            



    def Login(self):
        email=input('Enter your Email : ')
        pwd=input('Enter your Password : ')
        UserManager.FindUser(email=email,pwd=pwd)

        
    def Exit(self):
        exit()
