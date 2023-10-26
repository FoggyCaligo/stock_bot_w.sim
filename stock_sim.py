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
        bottomprice = random.randint(10000,50000)
        for i in range(self.hogalen):#init_pricearr
            self.pricearr[i] = bottomprice
            bottomprice += self.tick
        for i in range(self.hogalen):#init_amountarr
            self.amountarr[i] = random.randint(0,30)
        
# 
    def update2(self):
        buyidx = random.randint(0,9)
        sellidx = random.randint(10,19)
        randamount = random.randint(1,10)
        if(self.amountarr[buyidx]>randamount and self.amountarr[sellidx]>randamount):
                self.amountarr[buyidx] -= randamount
                self.amountarr[sellidx]-= randamount
        print(buyidx,":",sellidx,":",randamount)
        #add_order
        randidx = random.randint(0,19)
        randamount = random.randint(1,10)
        self.amountarr[randidx] += randamount

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
        else:
            if(targetidx<=9 and self.amountarr[origidx]>randamount):
                self.amountarr[origidx] -= randamount
                self.amountarr[targetidx] += randamount
            elif(targetidx>9 and self.amountarr[origidx]>randamount and self.amountarr[targetidx]>randamount):
                self.amountarr[origidx]-= randamount
                self.amountarr[targetidx] -= randamount        
        #add_order
        randidx = random.randint(0,19)
        randamount = random.randint(1,10)
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
         


class Kiwoon:
    pass







stock = Stock();
stock.show()


for i in range(10):
    for i in range(10):
        stock.update()
    stock.show()
    
