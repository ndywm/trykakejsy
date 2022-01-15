from random import randint
from math import floor
from colorama import Fore,Style
print(Fore.GREEN+Style.BRIGHT)
Data=[]
class Category:
    def __init__(self,str):
        str=str.split('\n')
        header=str[0].split(' ')
        self.name=header[0]
        self.base=float(header[1])
        self.amplifier=float(header[2])
        self.rewards=[]
        self.empty=False
        if len(str)<=1:
            self.empty=True
            self.rewards=[]
            return
        for i in range(1,len(str)):
            item=str[i].split(' ')
            if(item==['']):
                continue
            self.rewards.append((item[0],int(item[1])))
        self.bound=len(self.rewards)-1

def load():
    global Data
    with open('data','r') as f:
        Data=f.read().split('\n\n')
    for i in range(0,len(Data)):
        Data[i]=Category(Data[i])

load()
def randomise():
    Case={}
    for category in Data:
        amount=category.base
        while(randint(0,1)):
            amount+=category.amplifier
        amount=floor(amount)
        if(category.empty):
            Case[category.name]=amount
            if(amount>0):
                if(amount<64):
                    print(f"{category.name}: {amount}")
                elif(amount%64==0):
                    print(f"{category.name}: {amount//64}st")
                else:
                    print(f"{category.name}: {amount//64}st+{amount%64}")
        else:
            thing=category.rewards[randint(0,category.bound)]
            amount*=thing[1]
            Case[category.name]=[thing[0],amount]
            if(amount>0):
                if(amount<64):
                    print(f"{category.name}: {amount}  {thing[0]}")
                elif(amount%64==0):
                    print(f"{category.name}: {amount//64}st  {thing[0]}")
                else:
                    print(f"{category.name}: {amount//64}st+{amount%64}  {thing[0]}")
    return Case

randomise()
print(Style.RESET_ALL)
