items = [0,0,0]
coins = 100

def shoppe(coins):
    stuff = items
    
    while coins > 0 :
         print("Welcome to the shop you have ", coins, "coins")
         print("Your items are:", stuff)
         print("Todays scam is: Potion:$20, Food: $15, Keys: $30 ")
         choice = input("press p for potion, press f for food, and k for keys. Press q to quit")
         
         if choice =="p":
             if coins >= 20:
                 print("You got a potion ")
                 items[0] = "Potion"
                 coins -= 20
             else:
                  print("You broke")
                  return coins


                
         elif choice == "f":
              if coins >= 15:
                 print("You got food")
                 items[1] = "food"
                 coins -= 15
              else:
                  print("You broke")
                  return coins


                
         elif choice == "k":
              if coins >= 30:
                 print("You got a key")
                 items[2] = "key"
                 coins -= 30
              else:
                  print("You broke")
                  return coins
                
         elif choice == "q":
             print("Goodbye")
             return coins

         else:
             print("That no option you got scammed ")
             coins -=100

        
              


coins = shoppe(coins)
