import turtle 
import random
adam  = turtle.Turtle()
adam.shape ('turtle')
adam.speed (100)
colors = ['red', 'orange','blue' ,'yellow','green' ] 
for i in range(1000):
    for j in range(4):
        
        adam.forward(100)
        adam.left(90)
    adam.color(random.choice(colors))
    adam.left(5) 



































    