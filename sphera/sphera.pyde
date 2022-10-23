x1=300
y1=300
x2=300
y2=300
x3=300
y3=300
x4=300
y4=300


def setup():
    size(600,600)
    frameRate(5)
    background(0,255)
    
def draw():
    clear()
    global x1
    global y1
    fill(random(0,255),random(0,255),random(0,255))
    stroke(random(0,255),random(0,255),random(0,255))
    ellipse(x1,y1,90,90)
    x1=x1+10
    y1=y1+10
    
    global x2
    global y2
    ellipse(x2,y2,90,90)
    x2=x2-10
    y2=y2-10
    
    global x3
    global y3
    ellipse(x3,y3,90,90)
    x3=x3+10
    y3=y3-10
    
    global x4
    global y4
    ellipse(x4,y4,90,90)
    x4=x4-10
    y4=y4+10
