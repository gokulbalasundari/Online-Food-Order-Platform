from User import User
class UserManager:

    __Users=[]


    @classmethod
    def AddUser(cls,userobj):
        # we need to check give object is from User
        if isinstance(userobj,User):
            cls.__Users.append(userobj)
            print("User was succesfully Register")
        else:
            print('The give user was invaild')

    @classmethod
    def FindUser(cls,email,pwd):
        for user in cls.__Users:
            if user.email==email and user.password==pwd:
                print('Successfully Login')
                return user
        print('Invaild Password or Email')
    
