from turtle import Turtle, Screen


tommy = Turtle()
screen = Screen()


def move_forward():
    tommy.forward(10)


def move_backward():
    tommy.backward(10)


def move_right():
    tommy.right(10)


def move_left():
    tommy.left(10)


def clear_screen():
    tommy.reset()
    tommy.shape("arrow")
    tommy.color("medium aquamarine")
    tommy.pensize(3)
    tommy.speed("fast")


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=clear_screen, key="c")

tommy.shape("arrow")
tommy.color("medium aquamarine")
tommy.pensize(3)
tommy.speed("fast")

screen.exitonclick()