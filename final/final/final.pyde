t = 0 
x=random(0,1250)
y=random(0,720)
z=0
def setup():
    size(1250,720)
    frameRate(60)
def draw():
    
    global x,y,z,t
    if t == 40:
        x=random(0,1250)
        t = 0
    clear()
    textSize(25)
    text(z,100,100)
    img = loadImage("rfbueh.jpg")
    image(img,x,y,75,150)
    t+=1
def mouseClicked():
    global x,y,z
    if mouseX > x and mouseX < x+75 and mouseY > y and mouseY < y+150:
       z+=1
        
        
