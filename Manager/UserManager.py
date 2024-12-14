from Models.User import User
class UserManager:

    __Users=[]


    @classmethod
    def AddUser(cls,userobj):
        # we need to check give object is from User
        if isinstance(userobj,User):
            cls.__Users.append(userobj)
            print(f"{userobj.name} was succesfully Register")
            print()
        else:
            print('The give user was invaild')

    @classmethod
    def FindUser(cls,email,pwd):
        for user in cls.__Users:
            if user.email==email and user.password==pwd:
                return user                
        return None
    
    @classmethod
    def new(cls):
        pass
