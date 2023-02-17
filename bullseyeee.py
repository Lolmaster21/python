score = int(input("What score did you hit?(Choose 1-5) "))


def targetScore(score):
    if score == 1:
        print("BULLSEYE you got 50 points ")
        score += 50
        score -= 1
    
    elif score == 2:
        print("You hit the white circle. You got 40 points")
        score += 40
        score -= 2
        
    elif score == 3:
        print("You hit the blue circle. Plus 30 ")
        score += 30
        score -= 3
        
    elif score == 4:
        print("You hit a random color. You got 20 points")
        score += 20
        score -= 4
        
    elif score == 5:
        print("You hit the wall. You got 10 points")
        score += 10
        score -= 5
        
    else:
        print("You missed")
        score == 0
        
    return score


