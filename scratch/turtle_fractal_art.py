import turtle as tu
import random

# Setup
speed = 0  # Maximum speed
roo = tu.Turtle()
wn = tu.Screen()
wn.bgcolor("black")
wn.title("Fractal Tree Pattern")
roo.left(90)
roo.speed(speed)

# Parameters

factor1_pensize = 2
factor2_pensize = 2
factor3_pensize = 3
factor1 = 3/4
factor2 = 5/7
factor3 = 6/7
left_angle = 30
right_angle = 60
min_length = 10
max_length = 3000

# Screen boundaries
screen_width = wn.window_width() // 2
screen_height = wn.window_height() // 2

# Recursive draw function with boundary check
def draw(leg, pensize, color, factor, left_angle, right_angle, min_length):
    if leg < min_length:
        return
    if abs(roo.xcor()) > screen_width or abs(roo.ycor()) > screen_height:
        return
    if leg > max_length:
        return
    roo.pensize(pensize)
    roo.pencolor(color)
    roo.forward(leg)
    roo.left(left_angle)
    draw(leg * factor, pensize, color, factor, left_angle, right_angle, min_length)
    roo.right(right_angle)
    draw(leg * factor, pensize, color, factor, left_angle, right_angle, min_length)
    roo.left(left_angle)
    roo.backward(leg)

# Draw patterns with different parameters
patterns = [
    (20, factor1_pensize, "yellow", factor1),
    (20, factor1_pensize, "magenta", factor1),
    (20, factor1_pensize, "red", factor1),
    (20, factor1_pensize, "#FFF8DC", factor1),
    (40, factor2_pensize, "lightgreen", factor2),
    (40, factor2_pensize, "red", factor2),
    (40, factor2_pensize, "yellow", factor2),
    (40, factor2_pensize, "#FFF8DC", factor2),
    (60, factor3_pensize, "cyan", factor3),
    (60, factor3_pensize, "yellow", factor3),
    (60, factor3_pensize, "magenta", factor3),
    (60, factor3_pensize, "#FFF8DC", factor3)
]

#random.shuffle(patterns)

for length, pensize, color, factor in patterns:
    draw(length, pensize, color, factor, left_angle, right_angle, min_length)
    roo.right(90)
    roo.speed(speed)

wn.exitonclick()