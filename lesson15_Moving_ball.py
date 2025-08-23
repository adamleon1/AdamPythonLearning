import turtle
ball = turtle.Turtle('circle')
ball.shapesize(2,2)



left_rod = turtle.Turtle('square')
left_rod.shapesize(1,20)
left_rod.setheading(90)
left_rod.color('blue')
left_rod.penup()
left_rod.goto(-500,0)

right_rod = turtle.Turtle('square')
right_rod.shapesize(1,20)
right_rod.setheading(90)
right_rod.penup()
right_rod.color('red')
right_rod.goto(500,0)


turtle.listen()
turtle.onkeypress(lambda:left_rod.forward(20),'Up')
turtle.onkeypress(lambda:left_rod.forward(-20),'Down')
turtle.onkeypress(lambda:right_rod.forward(20),'w')
turtle.onkeypress(lambda:right_rod.forward(-20),'s')





speed = 2
x = speed
y = speed
posx = 0
posy = 0
while True:
    ball.goto(posx,posy)
    if ball.distance(right_rod)<30:
        ball.color('red')
        x = -speed
    if ball.distance(left_rod) <30:
        ball.color('blue')
        x = speed
    if ball.ycor()>200:
        y= -speed
    if ball.ycor() < -200:
        y = speed
        



    posx = posx+x
    posy = posy+y
turtle.done()