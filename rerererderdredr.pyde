w=0
def setup():
    size(600,600)
def draw():
    clear()
    citata=[2,10,9]
    global w
    textSize(15)
    text(citata[w],300,300)
    
    if keyPressed:
        if keyCode==UP:
            w+=1
        if keyCode==DOWN:
             w+=2
    
        
