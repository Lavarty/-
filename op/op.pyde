x1=300
y1=300
def setup():
    
    size(600,600)
    frameRate(10)
def draw():
    clear()
    global x1
    global y1
    #background(random(0,255),random(0,255),random(0,255))
    stroke(random(0,255),random(0,255),random(0,255))
    noFill()
    ellipse(300,300,x1,y1)
    x1=x1-30
    y1=y1-30
    
