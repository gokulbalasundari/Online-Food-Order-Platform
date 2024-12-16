class Cart:

    def __init__(self,res_name=None,choices=None,fooditems=None):
        self.res_name=res_name
        self.choices=choices
        # after they enter choices we need collecte number of food items immidiatly  and add the card food items so , we will call immediatly call addcard fuction .
        self.fooditems=fooditems
        if res_name:self.cartfooditems=self.__AddtoCart()

    def __AddtoCart(self):

        cartfooditems={}

        for choice in self.choices:
            if choice>len(self.fooditems):
                raise KeyError('Your are Enter Invalid Choices ...')
            if choice in cartfooditems:
                cartfooditems[choice]+=1
            else:    
                cartfooditems[choice]=1
        return cartfooditems
    
    def ProcessOrder(self,res=None,quantity=None,item=None):

        if res and quantity:

            print(f'\n---Your are Order in {res.name}---')
            price=item.price*quantity
            print(f'\n{item.name} x {quantity}= {price}')
            print(f'\nTotal : {price}')

            return False

        else:
            Total=0

            print(f'\nYour Order in {self.res_name}')
            print()
            for i,cartchoice in enumerate (self.cartfooditems,1):
                price=self.cartfooditems[cartchoice]*self.fooditems[cartchoice-1].price
                Total+=price
                print(f'{i}=>{self.fooditems[cartchoice-1].name} x {self.cartfooditems[cartchoice]} = {price}')
                
            print(f'\nTotal Amount: {Total}')    
                