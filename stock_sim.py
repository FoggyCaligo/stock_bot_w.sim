import random



class Order:
    priceidx = 0
    amount = 0
    def __init__(self,price,amount):
        self.priceidx = price
        self.amount = amount
    



class Stock:
    
    def __init__(self):
        self.hogalen = 20
        self.tick = 500
        self.pricearr = [0 for i in range(20)]
        self.amountarr = [0 for i in range(20)]    
        self.orders = []                
        bottomprice = random.randrange(10000,50000)
        for i in range(self.hogalen):#init_pricearr
            self.pricearr[i] = bottomprice
            bottomprice += self.tick
        for i in range(self.hogalen):#init_amountarr
            self.amountarr[i] = random.randrange(0,30)


    def update(self):
        pass


        


    def show(self):
        for i in range(len(self.amountarr)):
            bar = ""
            for j in range(self.amountarr[i]):
                if(i<10): bar += "+"
                else : bar += "-"
            print(self.pricearr[i], ":", bar)
         


class Kiwoon:
    pass







stock = Stock();
stock.show()
