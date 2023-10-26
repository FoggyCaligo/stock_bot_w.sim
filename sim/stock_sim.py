import random



class Order:
    priceidx = 0
    amount = 0
    def __init__(self,price,amount):
        self.priceidx = price
        self.amount = amount
        self.code = ""    
        self.state = True


class Customer:
    def __init__(self):
        self.orders = []


    def update():
        pass




class Sim:
    
    def __init__(self,code):#initialize variables
        self.code = code
        self.hogalen = 20
        self.tick = 500
        self.pricearr = [0 for i in range(20)]
        self.amountarr = [0 for i in range(20)]    
        self.orders = []                
        bottomprice = random.randint(10000,50000)
        for i in range(self.hogalen):#init_pricearr
            self.pricearr[i] = bottomprice
            bottomprice += self.tick
        for i in range(self.hogalen):#init_amountarr
            self.amountarr[i] = random.randint(0,30)
    #indicates changing order amount 
    def update(self):
        origidx = random.randint(0,19)
        targetidx = random.randint(0,19)
        randamount = random.randint(1,10)
        if(origidx>9):#sell
            if(targetidx>9 and self.amountarr[origidx]>randamount ):
                self.amountarr[origidx] -= randamount
                self.amountarr[targetidx] += randamount
            elif(targetidx<=9 and self.amountarr[origidx]>randamount and self.amountarr[targetidx]>randamount):
                self.amountarr[origidx]-= randamount
                self.amountarr[targetidx] -= randamount        
        else:#buy
            if(targetidx<=9 and self.amountarr[origidx]>randamount):
                self.amountarr[origidx] -= randamount
                self.amountarr[targetidx] += randamount
            elif(targetidx>9 and self.amountarr[origidx]>randamount and self.amountarr[targetidx]>randamount):
                self.amountarr[origidx]-= randamount
                self.amountarr[targetidx] -= randamount        
        #add_order
        randidx = random.randint(0,19)
        randamount = random.randint(1,5)#add amount
        self.amountarr[randidx] += randamount

    def show(self):
        print("............................................................")
        for i in range(len(self.amountarr)):
            bar = ""
            for j in range(self.amountarr[i]):
                if(i<10): bar += "+"
                else : bar += "-"
            print(i,":",self.pricearr[i],":",self.amountarr[i], ":", bar)
        print("............................................................\n")
         
    def get_amountarr(self):
        return self.amountarr

    def get_pricearr(self):
        return self.pricearr

    def get_code(self):
        return self.code



    





class Kiwoom:
    def __init__(self):
        self.stockarr = []
        for i in range(10):
            self.stockarr.append(Sim(str(i)))

    def update(self):
        rand_stock = random.randrange(0,10)
        currstock = self.stockarr[rand_stock]
        

    pass







stock = Sim("a");
stock.show()


for i in range(10):
    for i in range(100):
        stock.update()
    stock.show()
    

kiwoom = Kiwoom()
