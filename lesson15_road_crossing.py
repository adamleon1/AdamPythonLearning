


import turtle

# Setup screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("white")

# Register car gi
car_gif = "car.gif"   # put your gif in the same folder
screen.addshape(car_gif)

# Create car turtle
car = turtle.Turtle()
car.shape(car_gif)
car.penup()
car.goto(0,-300)
# Movement functions
def move_up():
    car.sety(car.ycor() + 10)

def move_down():
    car.sety(car.ycor() - 10)
    

# Key bindings
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

screen.mainloop()


