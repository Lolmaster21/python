import random


lol = [[0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0]
       ]


geekin = int(random.randint(0,9)) #Random room x variable

XD = int(random.randint(0,9)) #Random y variable 
    
DX = int(random.randint(1,5)) #Random room value

direction = 0

j = input("Welcome to text based game press anything to continue and q to quit ")
#game loop-----------------------------------------------
while j != 'q':
     
    if lol[geekin][XD] == 0:
        DX = int(random.randint(1,5)) #Random room value
    DX = int(random.randint(1,5)) #Random room value
    
    print("What direction do you want to? (0)to go down, (1) to go up, (2)to go right, (3) to go left")
    
    direction = int(input())

    
    
    
    
    if direction == 0 and geekin != 9: #Y variable going down
        geekin += 1
        print("You went down")
        
        
    if direction == 1 and geekin != 0: #Y variable going up 
        geekin -= 1
        print("You went up")

        
    if direction == 2 and XD != 9: #X variable right
        XD += 1
        print("You went right")

    if direction == 3 and XD != 0: #X variable going left
        XD -= 1
        print("You went left")

    
    lol[geekin][XD] = DX
    for i in range(10):
        print(lol[i])
        
    
        
   
    
    




    
    
