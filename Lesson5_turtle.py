import turtle
import random
colors = ['red','green','blue','orange','pink','yellow','purple']
turtlestoer = []
for i in range(-200,201,50):
    tt = turtle.Turtle('turtle')
    tt.speed(1000000000000)
    tt.color(random.choice(colors))
    tt.penup()
    tt.goto(-300,i)
    turtlestoer.append(tt)

while True:
    for tt in turtlestoer:
        tt.forward(random.randint(1,15))
        tt.circle (100)

turtle.mainloop()