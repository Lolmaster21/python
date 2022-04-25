import math

def CircleCollision(x1,y1,x2,y2,size):
    if math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)) < size:
        print("BOOM")
        return True
    else:
        print("miiiiiiissssss")
        return False
    
    

xa = int(input(print ("Enter circle's x1 coord: ")))
xb = int(input(print ("Enter circle's x2 coord: ")))
ya = int(input(print ("Enter circle's y1 coord: ")))
yb = int(input(print ("Enter circle's y2 coord: ")))
siz = int(input(print ("Enter circle's radius : ")))

CircleCollision(xa,ya,xb,yb,siz)

