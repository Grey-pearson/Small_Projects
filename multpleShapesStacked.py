from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(0)
turtle.penup()
turtle.goto(-5, 510)
turtle.pendown()

colors = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]


def draw_shape(sides, angle):
    for shape in range(sides):
        turtle.forward(40)
        turtle.right(angle)


def change_color():
    turtle.color(random.choice(colors))


sides_of_shape = 999

for sides in range(3, sides_of_shape):
    # dynamically generate angles and use sides using range
    angle = 360 / sides
    draw_shape(sides, angle)
    change_color()


while True:
    turtle.left(5)


screen = Screen()
