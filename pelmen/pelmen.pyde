x=100
y=300

def setup():
    size(600,600)
    frameRate(25)
    background(255)
    
def draw():
    clear()
    global x
    img=loadImage("pelmen.jpg")
    image(img,x,y,75,75)
    
    img=loadImage("tarelka pelmen.jpg")
    image(img,100,y,75,75)
    push()
    
    img=loadImage("pelmeball.jpg")
    image(img, 525,y,75,75)
    pop()
    if x>600:
        x=100
    
    x+=5
