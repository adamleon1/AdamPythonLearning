import turtle

# Register the image "dog.gif" so it can be used as a turtle shape
turtle.register_shape("dog.gif")

# Create a turtle named "myDog" with the shape "dog.gif"
myDog = turtle.Turtle()
myDog.shape("dog.gif")

# Set the speed of the turtle
myDog.speed(100)

for i in range(1000):
    for j in range(4):
        myDog.forward(100)  # Move the turtle forward by 100 units
        myDog.left(90)  # Turn the turtle left by 90 degrees
    myDog.left(5)  # Turn the turtle left by 5 degrees for the next iteration
