from LoginSystem import LoginSystem
class FoodApp:

    __options={1:'New user',2 :'Login',3:'Exit'}

    @staticmethod
    def Init():

        loginsystem=LoginSystem()

        while True:
            print("\nWelcome to Online Food  Order Platform")
            print()

            for option in FoodApp.__options:
                print(f'{option}.{FoodApp.__options[option]}', end=' ')
            print()  

            try:
                choice=int(input('\nEnter Your Choices: '))
                loginsystem.VaildChoice(choice=choice)

            except(ValueError):
                print("Invaild Input Type ..Retry")

            








        