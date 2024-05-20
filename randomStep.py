from turtle import Turtle, Screen
import random

WIDTH, HEIGHT = 1000, 1000
screen = Screen()
screen.bgcolor("black")
cursor = Turtle()
cursor.shape("circle")
cursor.pensize(15)
cursor.speed(0)
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
direction = [0, 90, 180, 270]

while True:
    cursor.forward(50)
    cursor.left(random.choice(direction))
    cursor.color(random.choice(colors))
