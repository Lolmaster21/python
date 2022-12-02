items = [0,0,0]
coins = 100

def shoppe(coins):
    stuff = items
    
    while coins > 0:
         print("Welcome to the shop you have ", coins, "coins")
         print("Your items are:", stuff)
         print("Todays scam is: Potion:$20, Food: $15, Keys: $30 ")
         choice = input("press p for potion, press f for food, and k for keys")
         
         if choice =="p":
             print("You got a potion ")
             items[0] = "Potion"
             coins -= 20
             return coins

                
         if choice == "f":
             print("You got food")
             coins -= 15
             items[1] = "food"
             return coins

                
         if choice == "k":
             print("You got a key")
             coins -=30
             items[2] = "key"
             return coins

         else:
             print("That no option you got scammed ")
             coins -=100

        
              


print (shoppe(coins))
    
    
