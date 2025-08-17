import turtle

def make_square(tt,steps):
    for i in range(4):
        tt.forward(steps)
        tt.left(90)


def make_loop(tt,steps,space):
    for i in range(steps,0,-space):
        tt.forward(i)
        tt.left(90)
