import turtle as t
import random

screen = t.Screen()
# screen.screensize(100, 100)
# screen.bgcolor("black")
cursor = t.Turtle()
cursor.shape("arrow")
cursor.penup()
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


def random_color():
    color = random.choice(colors)
    return color


def draw_row():
    for dots in range(10):
        cursor.dot(20, random_color())
        cursor.fd(50)


def move_column():
    cursor_x = -200
    cursor_y = -200
    cursor.goto(cursor_x, cursor_y)
    for rows in range(10):
        draw_row()
        cursor_y += 50
        cursor.goto(cursor_x, cursor_y)
    cursor.


move_column()  # start

# once its done turtle just chills
while True:
    cursor.left(1)


screen.exitonclick()
