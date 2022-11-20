x=50
y=350
x1=50
x2=50
x3=50
x4=50
x5=50



def setup():
    size(600,600)
    frameRate(10)

def draw():
    global x,y
    clear()
    background(random(0,255),random(0,255),random(0,255))
    fill(random(0,255),random(0,255),random(0,255))
    img=loadImage("images.jpg")
    image(img,x,0,100,100)
    x=x+5
    
    
    global x1
    img=loadImage("images.jpg")
    image(img,x1,100,100,100)
    
    x1=x1+2
    
    global x2
    img=loadImage("images.jpg")
    image(img,x2,200,100,100)
    
    x2=x2+6
    
    global x3
    img=loadImage("images.jpg")
    image(img,x3,300,100,100)
    
    x3=x3+3
    
    global x4
    img=loadImage("images.jpg")
    image(img,x4,400,100,100)
    
    x4=x4+7
    
    global x5
    img=loadImage("images.jpg")
    image(img,x5,500,100,100)
    
    x5=x5+9
