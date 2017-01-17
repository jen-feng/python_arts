## @file Rectangles.py
#  @title Rectangles
#  @author Jenny Feng Chen
#  @date 02/22/2016

from turtle import*
from math import*
def nestedSquares():
    reset()
    hideturtle()
    x=-200;y=200
    penup()
    setposition(x,y)
    pendown()
    right(90)
    for i in range(200,-1,-20):
        for a in range(4):
            forward(i)
            left(90)
        x+=5;y-=5
        penup()
        setposition(x,y)
        pendown()
        
def artisticSquares():
    reset()
    hideturtle()
    penup()
    setposition(-200,100)
    pendown()
    left(90)
    length=100
    n=['purple','grey']
    for i in range(7):
        for j in range(8):
            begin_fill()
            color(n[i%2])
            for k in range(4):
                pencolor(n[(i+1)%2])
                pensize(length/30)
                forward(length)
                right(90)
            end_fill()   
            penup()
            right(45)
            forward(sqrt(2*length**2))
            pendown()
        right(135)
        penup()
        forward(length)
        pendown()
        left(157.5)
        length=length/1.847
        






        
    
