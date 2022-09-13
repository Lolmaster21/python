import random

num = 0
def MonsterGen(biome):
    num = random.randrange(1,105)

    
    if num<25 :
        print("You spawned in the desert")
        if num<25:
             print("A husk is attacking you")
        elif num<50:
             print("A drowned spawned lol")
        elif num < 75:
             print("A normal zombie lunges at you")
        else:
             print ("A mutant zombie came in ")
                 
    elif num<50:
        print("You spawned in the cold artic")
        if num<45:
             print("A wild polar bear lunged at you")
        elif num<70:
             print("An artic fox spawned... its kind of cute")
        elif num < 95:
             print("A killer bunny spawned")
     
    elif num<100:
        print("Where are you?")
        if num<55:
             print("A huge warden spawned")
        elif num<80:
             print("An ender TITAN SPAWNED")
        elif num < 105:
             print("IT'S A MUTANT SKELETON")
      

choice = 'a'
while choice != 'q':
    print("Press random number")
    choice = input()
    if choice != 'q':
        MonsterGen(int(choice))
