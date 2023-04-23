x=100
a=["pelmeni","computer","jkomando"]
u=0
def setup():
    size(600,600)
    frameRate(1)
def draw():
    
    global x, a, u
    x=100
    for i in range(len(a)):
        textSize(50)
        if u==i:
            fill(random(0,255),random(0,255),random(0,255))
        else:
            fill(255)
        text(a[i],50,x)
    
        x+=100
        
        if keyPressed:
            if keyCode==UP:
                if u > 0:
                    u-=1
        
            if keyCode==DOWN:
                if u < 2:
                    u+=1
