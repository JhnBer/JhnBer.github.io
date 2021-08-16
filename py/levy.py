import turtle
turtle.speed('fastest')

def levy(l, n):
    if n == 0:
        turtle.forward(l)
        return
    turtle.left(45)
    levy(l*2**0.5/2, n-1)
    turtle.right(90)
    levy(l*2**0.5/2, n-1)
    turtle.left(45)

def draw(l, n, n2):
    turtle.penup()
    turtle.left(180)
    turtle.forward(l/2)
    turtle.right(90)
    turtle.forward(l/3*2)
    turtle.right(90)
    turtle.pendown()
    for i in range(n-1, n2+1):
        levy(l, i)
        turtle.penup()
        turtle.left(180)
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(l/3*(1.5+(i/3)))
        turtle.left(90)
        turtle.pendown()

def change_pos(lenght):
    turtle.penup()
    turtle.left(180)
    turtle.forward(lenght/2)
    turtle.left(90)
    turtle.forward(lenght/4)
    turtle.left(90)
    turtle.pendown()

lenght = 400

change_pos(lenght)

levy(lenght, 12)
#draw(300, 9, 11)

### uncomment next lines if the turtle window closes immediately after the drawing ends
#import time
#time.sleep(9999) 
