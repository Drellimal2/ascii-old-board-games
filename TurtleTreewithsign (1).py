import turtle

turtle.showturtle()
turtle.mode('logo')


def moveTurtle(disp):
    turtle.fd(disp)

def drawLimb(l, d):
    turtle.lt(d)
    moveTurtle(l)
        
    return turtle.position() 

def makeTree(h, l, b, d, ad):
    
    Base(b)
    
    turtle.color("brown")
    
    
    if h > 0:
        
        if h == 1:
            turtle.color("green")

        if h== 4:
            Apple(b)
        if d == 0:
            
            makeTree(h-1 , l*.75, drawLimb(l, d*ad), d+1,ad)
        else:
            y = turtle.heading()
            
            makeTree(h-1 , l*.75, drawLimb(l*.75, d*ad/2.00), d,ad)
            Base(b)
            d = d*-1
            turtle.setheading(y)
            makeTree(h-1 , l*.75, drawLimb(l*.75, d*ad/2.00), d,ad)
        
    else:
        Base(b)

def drawTreeFractal(height,AngularDisp, Length):
    turtle.bgcolor("#191970")
    a = (0,-200)
    Base(a)
    turtle.setheading(90)
    turtle.color("green")
    turtle.fd(1000)
    turtle.bk(2000)
    Base(a)
    star1()
    star2()
    sign()
    makeTree(height, Length,a,0,AngularDisp*2)
    turtle.setheading(180)
    makeTree(3, Length/2.00,a,0,AngularDisp*2)
    turtle.done()
    
def Base(b):
    turtle.pu()
    turtle.goto(b)
    turtle.pd()
    
    
def Apple(b):
    turtle.color('red')
    y = turtle.heading()
    turtle.setheading(180)
    moveTurtle(15)
    turtle.setheading(90)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.fillcolor("red")
    turtle.end_fill()
    Base(b)
    turtle.setheading(y)

def sign():
    turtle.color("chocolate")
    turtle.width(5)
    Base((-250,-200))
    turtle.setheading(0)
    turtle.fd(100)
    Tip = turtle.pos()
    turtle.fill(True)
    for x in range (1,5):
        
        
        
        turtle.setheading(turtle.heading() + 90)
        if x % 2 != 0:
            turtle.fd(150)
        else:
            turtle.fd(75)
        if turtle.heading() == 180:
            turtle.fd(25)
            turtle.bk(25)
    turtle.fillcolor('chocolate')
    turtle.fill(False)
    

    def writing():
        turtle.width(1)
        turtle.color("white")
        Base((-250,-100))
        turtle.setheading(162)
        turtle.pu()
        turtle.fd(28)
        turtle.setheading(180)
        turtle.fd(10)
        turtle.write("Raphaella and Danes' ", font=("Calibri", 12, "italic"))
        turtle.fd(14)
        turtle.pd()
        turtle.write("   Apple Tree",font = ("Calibri",12,"bold"))
        
    
    writing()
    turtle.setheading(0)


def star1():
    Base((200,200))
    turtle.color('yellow', 'white')
    turtle.begin_fill()
    for x in range (1,20):
        turtle.fd(10)
        turtle.lt(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    
def star2():
    Base((-200,150))
    turtle.color('yellow', 'white')
    turtle.begin_fill()
    for x in range (1,10):
        turtle.fd(10)
        turtle.lt(150)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()    
    
