room=1



# Variable to keep the main loop running
running = True

# Main loop
while running:
    if room == 1:
        print("you're in room 1, you can go e")
        choice = input()
    if choice == 'e':
        room = 2
        print("Youre in room 2, you can go w or s")
        choice = input()
    elif choice == 'w':
        room = 1
        
        
    if choice == 's':
        room = 3
        print("Youre in room 3, you can go n or e")
        choice = input()
    elif choice == 'n':
        room = 2
        
    if choice == 'e':    
        room = 4
        print("Youre in room 4 congrats you finished!!!! press (q)to quit")
        if choice == 'q':
            doExit = True
