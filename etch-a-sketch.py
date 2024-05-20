import turtle as t

# w forward
# s backwards
# a reletive to turtle turn left
# d reletive to turtle turn right

screen = t.Screen()
cursor = t.Turtle()
cursor.shape("arrow")
cursor.color("green")


def move_up():
    cursor.forward(3)


def move_left():
    cursor.left(3)


def move_down():
    cursor.back(3)


def move_right():
    cursor.right(3)


screen.onkeypress(move_up, "w")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")
screen.listen()

screen.mainloop()
