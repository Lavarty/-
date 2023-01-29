x=100
naprovlenie="right"
def setup():
    size(600,600)
    
def draw():
    global x
    clear()
    rectMode(CENTER)
    rect(300,300,x,x)
    
    x+=2
    
    if x==600:
        x=100
    
    
