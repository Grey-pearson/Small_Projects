from turtle import *
import random

cursor = Turtle()
cursor.speed(0)
cursor.pensize(5)
screen = Screen()

# how far out each flower of circles is going
radius = 200
# how far seperated circles are
turn = 30

colors = [
    "#7400B8",
    "#6930C3",
    "#5E60CE",
    "#5390D9",
    "#4EA8DE",
    "#48BFE3",
    "#56CFE1",
    "#64DFDF",
    "#72EFDD",
    "#80FFDB",
]


def change_color():
    cursor.color(random.choice(colors))


for i in range(10):
    cursor.color(colors[i])

    for j in range(12):
        cursor.circle(radius)
        cursor.right(turn)

    # turn -= 5
    radius -= 15

while True:
    cursor.left(5)
