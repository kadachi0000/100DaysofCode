import turtle
from turtle import Turtle
from random import randint, choice

tommy = Turtle()
tommy.shape("turtle")
tommy.color("medium aquamarine")
tommy.speed("fastest")
screen = turtle.Screen()


#screen.setup(width=400, height=400)

#draw a square
# for _ in range(4):
#     tommy.forward(100)
#     tommy.right(90)

# make a dashed line
# for _ in range(20):
#     tommy.forward(10)
#     tommy.penup()
#     tommy.forward(10)
#     tommy.pendown()

#make a random color
def change_color():
    turtle.colormode(255)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tommy.pencolor(r, g, b)
    tommy.pensize(1)


#go in a random direction
def change_direction():
    directions = [0, 90, 180, 360]
    tommy.setheading(choice(directions))


#walk in a random direction
# for _ in range(200):
#     change_color()
#     change_direction()
#     tommy.forward(20)


# draw a shape
def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tommy.forward(100)
        tommy.right(angle)


#make a triangle, square, pentagon, hexagon, hepta, octa, nona and decagon
# for sides in range(3, 11):
#     draw_shape(sides)
#     change_color()


def draw_spirograph(angle):
    for _ in range(int(360 / angle)):
        change_color()
        tommy.circle(40)
        tommy.right(angle)


draw_spirograph(20)

screen.exitonclick()
