import turtle
from funs import make_square, make_loop

t1 = turtle.Turtle('turtle')
t2 = turtle.Turtle('turtle')
t2.speed(1000)

make_loop(t2,200,2)

turtle.done()