x=0
y=0

def setup():
    size(600, 600)
    frameRate(5)
    
def draw():
    clear()
    global x
    global y
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(x,y,90,90)
   
    x=x+10
    y=y+10
