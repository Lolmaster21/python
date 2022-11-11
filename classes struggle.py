import random


candy = [0,0,0,0,0]

def halloween():
    num = random.randrange(1,100)
    
    if num < 15:
         candy[0]+1
         
    elif num < 20:
         candy[1]+1
    
    elif num < 35:
         candy[2]+1
    
    elif num < 10:
         candy[3]+1 
    
    elif num < 18:
         candy[4]+1
         
    elif num < 2:
         candy[5]+1
         
for i in range(5):
    print("New house: \n")
    print("You got :",candy[0],"Butterfinger")
    print("You got :",candy[1],"Hersheys")
    print("You got :",candy[2],"PB cups")
    print("You got :",candy[3],"M&Ms")
    print("You got :",candy[4],"Sour Patch Kids")
    print("You got rock")
   



