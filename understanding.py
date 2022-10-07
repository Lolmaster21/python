import random

num = 0
def npc(choice):
    
    num = random.randrange(1,100)
    
    if num<10:
        print("DO A BARREL ROLL!")
    elif num<15:
        print("Science isn't about why, it's about why not!")
    elif num < 20:
        print("Eat my shorts")
    elif num < 35:
        print("What is man? A miserable little pile of secrets")
    else:
        print ("I used to be an adventurer like you. Then I took an arrow in the knee")


choice = 'a'

 
    
        
for i in range(5):
    print("Press random number or press'q' to quit")
    choice = input()
    npc(int(choice))
    
    
#Question 2-----------------------------------------------------------------------------------------------------------

def bipolar(sappy):
    gold = 100
    
    num = random.randrange(1,100)

    if num<50 : #Grumpy 
        if num<25:
             print("Someone poisoned the waterhole! You lost 30 gold")
             gold-=30
        elif num<50:
             print("Welcome to the realm of madness ill be taking your gold now. You lost 25 gold")
             gold-=25
        elif num < 75:
             print("You lost a battle. Everything turned black. Minus 40 gold ")
             gold-=40
        else:
             print ("GET YOURSELF SOME CRUNCHY BOY. You lost 60 gold to cereal man ")
             gold-=60
             
    else:      #Friendly 
        if num<25 :
            print("Villager exchange noise. You got 45 gold")
            gold+=45
        elif num<50:
            print("A unicorn flew over your head pooping out gold. Plus 50 gold.(You feel weird now)")
            gold+=50
        elif num < 75:
            print("You found something shiny under your shoe. Plus 10 dabloons")
            gold+=10
        else:
            print ("THERES NO SUCH THING AS A HAPPILY EVER AFTER... Wait... You got 100 shmoney money")
            gold+=60
            return(gold)
        
    print(gold)
    
for l in range(5):
    print("Press random number or press'q' to quit")
    choice = input()
    bipolar(int(choice))
    
    
    
    
    
    
