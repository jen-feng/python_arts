## @file Squares.py
#  @title Squares
#  @author Jenny Feng Chen
#  @date 02/22/2016

from turtle import*
def adjacentRectangles():
    reset()
    hideturtle()
    right(90)
    width=512
    g=98
    for i in range(9):
        begin_fill()
        color('grey'+str(g))
        for j in range(2):
            pencolor('red')
            forward(300)
            left(90)
            forward(width)
            left(90)
        end_fill()
        width=width/2
        g=g-14
        
def atisticRectangles():
    reset()
    bgcolor("black")
    hideturtle()
    penup()
    setposition(0,-30)
    pendown()
    b=0
    for a in range(2):
        for i in range(4):
            n=14
            for j in range(4):
                begin_fill()
                color('grey'+str(n))
                n+=14
                pencolor('black')
                if b!=0 or a!=0:
                    if b==0:
                        penup()
                        left(90)
                        forward(30)
                        right(90)
                        pendown()
                    for k in range(2):  
                        forward(30)
                        left(90)
                        forward(90)
                        left(90)
                elif b == 0:
                    for k in range(2):
                        forward(30)
                        left(90)
                        forward(120)
                        left(90)
                        b=0
                else:
                    b
                left(90)
                end_fill()
                penup()
                if a==1:
                    b=1
                if b==0:  
                    forward(30)
                    
                else:
                    forward(30)
                right(90)
                if a==0:
                    backward(30)
                else:
                    forward(30)
                pendown()
            penup()
            if a ==0:
                forward(150)
            else:
                backward(90)
            right(90)
            if a==0:
                forward(90)
            else:
                forward(150)
            pendown()
            if a==0:
                b=0
            else:
                b=1
        penup()
        if a==0:
            forward(30)
        else:
            forward(150)
        pendown()


        






        

        






                
                

                





    
