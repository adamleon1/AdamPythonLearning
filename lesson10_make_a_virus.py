import turtle

def make_virus(tt,sp,ep):
    a = 0
    b = 0
    tt.penup()  
    tt.goto(sp,ep)
    tt.pendown()
    tt.speed (10000)
    while True:
        b = b + 1
        a = a + 1
        tt.forward(a)
        tt.right(b)

        if b == 200:break


import random
x_poss = list(range(-200,200,140))
colors = ['red','green','blue','orange','yellow','pink']
y_poss = list(range(-200,200,140))
for i in range(1):    
    for xpos in x_poss:
        for ypos in y_poss:
            t1 = turtle.Turtle()
            t1.speed('fastest')
            t1.color(colors[i%6])
            make_virus(t1,xpos,ypos)
turtle.done()