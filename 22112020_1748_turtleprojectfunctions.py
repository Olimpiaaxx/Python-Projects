import random
import turtle
fred = turtle.Pen()

fred.shape("turtle")
fred.width(3)
fred.speed(0)

colorlist = ["red", "blue", "green", "purple", "pink", "orange"]

def star(size):
    for i in range(8):
        fred.forward(size)
        fred.left(225)

def square(size):
    for i in range(4):
        fred.forward(size)
        fred.left(90)

def goto(objectFred):
    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    objectFred.up()
    objectFred.goto(x, y)
    objectFred.down()
    col = random.choice(colorlist)
    objectFred.color(col)
    #objectFred.goto(x, y)
        
for i in range(100):
    size = random.randrange(10,200)
    star(size)
    goto(fred)
    square(size)
    goto(fred)
    

    
