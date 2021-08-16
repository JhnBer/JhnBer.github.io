import turtle
turtle.speed('fastest')

def koch(l, n):
    if n == 0:
        turtle.forward(l)
        return
    koch(l/3, n-1)
    turtle.left(60)
    koch(l/3, n-1)
    turtle.right(120)
    koch(l/3, n-1)
    turtle.left(60)
    koch(l/3, n-1)

def draw(l, n):
    turtle.penup()
    turtle.left(180)
    turtle.forward(l/2)
    turtle.right(90)
    turtle.forward(l/3*0.65*(n-1)/2)
    turtle.right(90)
    turtle.pendown()
    for i in range(1, n+1):
        koch(l, i)
        turtle.penup()
        turtle.left(180)
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(l/3*0.65)
        turtle.left(90)
        turtle.pendown()

def draw_snowflake(l, n):
    turtle.penup()
    turtle.left(180)
    turtle.forward(l/2)
    turtle.right(90)
    turtle.forward(l/2)
    turtle.right(90)
    turtle.pendown()
    for i in range(3):
        koch(l, n)
        turtle.right(120)

#koch(100, 1)
#draw(1000, 8)
draw_snowflake(500, 4)

### uncomment next lines if the turtle window closes immediately after the drawing ends
#import time
#time.sleep(9999) 
