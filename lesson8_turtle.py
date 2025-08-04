import turtle

for i in range(500):
    turtle.forward(1)
    if turtle.xcor()>300:
        turtle.hideturtle()

turtle.done()