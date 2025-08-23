

######## working code
import turtle as t

# ------------ Config ------------
WIDTH, HEIGHT = 1000, 900
FPS = 60                # target frames per second
DT_MS = int(1000 / FPS) # timer delay per frame
PADDLE_SPEED = 12
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
PADDLE_STRETCH_LEN = 1      # width
PADDLE_STRETCH_WID = 10      # height (≈ 6*20px = 120px)
PADDLE_HALF_HEIGHT = PADDLE_STRETCH_WID * 10  # ≈ 60px
BALL_SIZE = 1.2             # stretch for circle (≈ 24px diameter)
BALL_RADIUS = BALL_SIZE * 10

# ------------ Classes ------------
class RodBall(t.Turtle):
    def __init__(self, shape_parameter, color_p, size_x, size_y, position_x, position_y):
        super().__init__(visible=False)
        self.penup()
        self.shape(shape_parameter)
        self.color(color_p)
        self.shapesize(stretch_wid=size_y, stretch_len=size_x)
        self.goto(position_x, position_y)
        self.speed(0)
        self.showturtle()

    def move_up(self):
        top_limit = HEIGHT//2 - PADDLE_HALF_HEIGHT
        if self.ycor() < top_limit:
            self.sety(min(self.ycor() + PADDLE_SPEED, top_limit))

    def move_down(self):
        bottom_limit = -HEIGHT//2 + PADDLE_HALF_HEIGHT
        if self.ycor() > bottom_limit:
            self.sety(max(self.ycor() - PADDLE_SPEED, bottom_limit))

# ------------ Screen ------------
screen = t.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Smooth Pong")
screen.bgcolor("white")
screen.tracer(0)   # manual screen updates for smooth animation

# ------------ Objects ------------
right_Rod = RodBall("square", "red", PADDLE_STRETCH_LEN, PADDLE_STRETCH_WID,  WIDTH//2 - 60, 0)
left_Rod  = RodBall("square", "green", PADDLE_STRETCH_LEN, PADDLE_STRETCH_WID, -WIDTH//2 + 60, 0)
ball      = RodBall("circle", "black", BALL_SIZE, BALL_SIZE, 0, 0)

# Ball velocity
vx, vy = BALL_SPEED_X, BALL_SPEED_Y

# ------------ Scoreboard ------------
score_left = 0
score_right = 0
writer = t.Turtle(visible=False)
writer.hideturtle()
writer.penup()
writer.goto(0, HEIGHT//2 - 60)

def draw_score():
    writer.clear()
    writer.write(f"{score_left} : {score_right}", align="center", font=("Arial", 32, "bold"))

draw_score()

# ------------ Input ------------
movement = [False, False, False, False]  # L-up, L-down, R-up, R-down

def pressed(i):  movement.__setitem__(i, True)
def released(i): movement.__setitem__(i, False)

screen.listen()
screen.onkeypress(lambda: pressed(0), "w")
screen.onkeypress(lambda: pressed(1), "s")
screen.onkeypress(lambda: pressed(2), "Up")
screen.onkeypress(lambda: pressed(3), "Down")
screen.onkeyrelease(lambda: released(0), "w")
screen.onkeyrelease(lambda: released(1), "s")
screen.onkeyrelease(lambda: released(2), "Up")
screen.onkeyrelease(lambda: released(3), "Down")

# ------------ Helpers ------------
def reset_ball(to_right=True):
    global vx, vy
    ball.goto(0, 0)
    vx = abs(vx) if to_right else -abs(vx)
    vy = BALL_SPEED_Y if vy == 0 else vy

def paddle_collision(paddle):
    """Axis-aligned hit test using paddle extents."""
    px, py = paddle.xcor(), paddle.ycor()
    bx, by = ball.xcor(), ball.ycor()

    paddle_half_width  = 10 * PADDLE_STRETCH_LEN   # ≈ 10px
    paddle_half_height = PADDLE_HALF_HEIGHT        # ≈ 60px

    # Paddle rectangle
    left   = px - paddle_half_width
    right  = px + paddle_half_width
    bottom = py - paddle_half_height
    top    = py + paddle_half_height

    # Circle-rect collision (clamp method)
    closest_x = max(left, min(bx, right))
    closest_y = max(bottom, min(by, top))
    dx = bx - closest_x
    dy = by - closest_y
    return (dx*dx + dy*dy) <= (BALL_RADIUS * BALL_RADIUS)

# ------------ Main Loop ------------
def step():
    global vx, vy, score_left, score_right

    # Move paddles (continuous while keys held)
    if movement[0]: left_Rod.move_up()
    if movement[1]: left_Rod.move_down()
    if movement[2]: right_Rod.move_up()
    if movement[3]: right_Rod.move_down()

    # Move ball
    ball.setx(ball.xcor() + vx)
    ball.sety(ball.ycor() + vy)

    # Bounce top/bottom edges
    top_edge = HEIGHT//2 - BALL_RADIUS
    bot_edge = -HEIGHT//2 + BALL_RADIUS
    if ball.ycor() >= top_edge:
        ball.sety(top_edge)
        vy = -abs(vy)
    elif ball.ycor() <= bot_edge:
        ball.sety(bot_edge)
        vy = abs(vy)

    # Paddle collisions (with small "push out" to avoid sticking)
    # Right paddle
    if vx > 0 and paddle_collision(right_Rod):
        ball.setx(right_Rod.xcor() - (10 * PADDLE_STRETCH_LEN) - BALL_RADIUS - 1)
        vx = -abs(vx)
        # Add a bit of angle based on where it hit the paddle
        vy += int((ball.ycor() - right_Rod.ycor()) * 0.08)

    # Left paddle
    if vx < 0 and paddle_collision(left_Rod):
        ball.setx(left_Rod.xcor() + (10 * PADDLE_STRETCH_LEN) + BALL_RADIUS + 1)
        vx = abs(vx)
        vy += int((ball.ycor() - left_Rod.ycor()) * 0.08)

    # Scoring: ball passes left/right edges
    right_goal = WIDTH//2 + BALL_RADIUS
    left_goal  = -WIDTH//2 - BALL_RADIUS
    if ball.xcor() > right_goal:
        score_left += 1
        draw_score()
        reset_ball(to_right=False)
    elif ball.xcor() < left_goal:
        score_right += 1
        draw_score()
        reset_ball(to_right=True)

    screen.update()
    screen.ontimer(step, DT_MS)

# Start
reset_ball(to_right=True)
step()

t.done()


