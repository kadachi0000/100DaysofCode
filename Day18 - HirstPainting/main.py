import turtle
from turtle import Turtle
from random import randint

color_list = [
    (183, 176, 8),
    (180, 6, 69),
    (245, 25, 139),
    (10, 142, 38),
    (241, 67, 6),
    (87, 5, 92),
    (50, 168, 158),
    (45, 25, 107),
    (114, 168, 115),
    (31, 62, 204)
]

tommy = Turtle()
tommy.speed("fastest")
screen = turtle.Screen()
screen.setup(height=500, width=500)
screen.setworldcoordinates(-10, -10, screen.window_height(), screen.window_width())


def change_color():
    turtle.colormode(255)
    color = color_list[randint(0, len(color_list) - 1)]
    tommy.pencolor(color)


y_start = 0
rows = 1
while rows < 11:
    for _ in range(10):
        tommy.hideturtle()
        change_color()
        tommy.dot(20)
        tommy.penup()
        tommy.forward(50)
    tommy.setpos(0, y_start + 50)
    y_start += 50
    rows += 1

screen.exitonclick()
