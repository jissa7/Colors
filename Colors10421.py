#Initialize Turtle
import turtle
import random
jenna=turtle.Turtle()
turtle.colormode(255)
jenna.speed(100)

#Functions
def randomDot():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    s=random.randint(0,300)
    jenna.color(r,g,b)
    jenna.begin_fill()
    jenna.circle(s)
    jenna.end_fill()
    print(r,g,b)
def drawSquare():
    s=random.randint(0,300)
    for i in range (4):
        jenna.forward(s)
        jenna.right(90)
def randomSquare():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    jenna.color(r,g,b)
    jenna.begin_fill()
    drawSquare()
    jenna.end_fill()
    
#Main
for i in range (500):
    x=random.randint(-500,500)
    y=random.randint(-500,500)
    jenna.penup()
    jenna.goto(x,y)
    jenna.pendown()
    randomDot()
    jenna.penup()
    jenna.goto(x,y)
    jenna.pendown()
    randomSquare()
