print("Give me a number ")
cases = int(input()) #Gets the number of phrases
thing = [] #empty list to hold stuff

#get the phrases from the user
for i in range(cases):
    phrase = input() #get user input
    thing.append(phrase)
    
#print them back out
for i in range(len(thing)):
    print(thing[i])

