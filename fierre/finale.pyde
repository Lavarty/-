#зДРАВСТВУЙТЕ это мой финальный проект как говорится Let s go go go !
t = 0
x=random(0,1250)
y=random(0,720)
z=0
def setup():
    size(1250,720)
    frameRate(60)
    
    
    
def draw():
    
    global x,y,z,t
    if t ==10:
        x=random(0,1250)
        t = 0
    clear()
    textSize(25)
    text(z,100,100)
    img = loadImage("rfbueh.jpg")
    image(img,x,y,75,150)
    t+=1
    
    if z==15:
       img = loadImage("the end.jpg")
       image(img,0,0,1250,720)
       
    
    w = loadImage("wwqwq.png")
    image(w,mouseX,mouseY,75,150)
    
    if key=="K" or key=="k":
        a = loadImage("kukri.png")
        image(a,mouseX,mouseY,75,150)
        
    if key=="R" or key=="r":
        a = loadImage("wwqwq.png")
        image(a,mouseX,mouseY,75,150)
    
    
    
def mouseClicked():
    global x,y,z
    if mouseX > x and mouseX < x+75 and mouseY > y and mouseY < y+150:
       z+=1
