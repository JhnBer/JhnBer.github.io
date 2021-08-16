import turtle
turtle.speed('fastest')

start_rotation = False

def dragon(l, n):
    global start_rotation
    if not start_rotation:
        turtle.right(45*n)
        start_rotation = True
    if n == 0:
        turtle.forward(l)
        return
    dragon(l, n-1)
    turtle.left(90)
    dragon_r(l, n-1)

def dragon_r(l, n):
    if n == 0:
        turtle.forward(l)
        return
    dragon(l, n-1)
    turtle.right(90)
    dragon_r(l, n-1)

def move_turtle(x = 0, y = 0):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()

move_turtle(0, 200)
dragon(5, 3)

### uncomment next lines if the turtle window closes immediately after the drawing ends
#import time
#time.sleep(9999) 
