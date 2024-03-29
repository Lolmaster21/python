import random
print("Welcome to Mo's Chatbot. What's on your mind today?")
doExit = False

while doExit == False:
    choice = input()
    if choice == "quit":
        doExit = True
        break

    #listen and respond to feelings
    if choice.find("sad") != -1 or choice.find("feeling down") != -1 or choice.find("upset") != -1 or choice.find("angry") != -1 :
        print("I'm sorry to hear you're feeling that way.")
    elif choice.find("happy") != -1 or choice.find("glad") != -1 or choice.find("excited") != -1 or choice.find("looking forward") != -1 :
        print("That's great!")
    elif choice.find("I'm") != -1: #these next three lines let you repeat the word after "I'm" back in a sentence
        word_list = choice.split() #break the sentence into a list with one word per slot
        next_word = word_list[word_list.index("I'm")-1] #find the word after "I'm"
        print("Why are you", next_word+ "?") #repeat it back
        #NOTE: it would be good to add an if statement here checking if the next word was "a"
        #so if someone says "I'm a frog", it doesn't say back, "Why are you a?"

    #listen and respond to specific topics
    elif choice.find("mom") != -1 or choice.find("dad") != -1 or choice.find("brother") != -1 or choice.find("sister") != -1 :
        print("Tell me more about your family.")

    elif choice.find("dog") != -1 or choice.find("cat") != -1 or choice.find("fish") != -1 or choice.find("bird") != -1 :
        print("I'd like to hear more about this pet.")
   
    elif choice.find("popcorn") != -1 or choice.find("candy") != -1 or choice.find("chips") != -1 or choice.find("cerael") != -1 :
        print("Is this your favorite snack?")
   
    elif choice.find("Fortnite") != -1 or choice.find("Call Of Duty") != -1 or choice.find("Pokemon") != -1 or choice.find("Minecraft") != -1 :
        print("How much time have you spent on the game?")
       
    elif choice.find("Draw") != -1 or choice.find("Play videogames") != -1 or choice.find("Go out") != -1 or choice.find("Biking") != -1 :
        print("Cool hobbys")
       
    elif choice.find("Summer") != -1 or choice.find("Fall") != -1 or choice.find("Spring") != -1 or choice.find("Winter") != -1 :
        print("Why is that your favorite?")

    else: #randomize last statement so it's not too repetetive
        num = random.randrange(1, 100)
        if num <50:
            print("Can you tell me more?")
        else:
            print("What does that suggest to you?")
