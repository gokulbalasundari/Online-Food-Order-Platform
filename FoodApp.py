from LoginSystem import LoginSystem
class FoodApp:

    __options={1:'New user',2 :'Login',3:'Exit'}

    @staticmethod
    def Init():
        print("Welcome to Online Food  Order Platform")

        loginsystem=LoginSystem()

        while True:

            for option in FoodApp.__options:
                print(f'{option}.{FoodApp.__options[option]}', end=' ')
            print()  

            try:
                choice=int(input('Enter Your Choices: '))
                loginsystem.VaildChoice(choice=choice)
                
            except(ValueError):
                print("Invaild Input Type ..Retry")








        