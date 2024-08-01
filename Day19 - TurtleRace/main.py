from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="I wonder who will win...",
                            prompt="Which color turtle do you think will win? Enter a color: ")

turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
i = 0
y = -200
for color in turtle_colors:
    color = Turtle(shape="turtle")
    color.color(turtle_colors[i])
    color.speed("fastest")
    color.penup()
    y += 60
    color.goto(x=-230, y=y)
    turtle_list.append(color)
    i += 1

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if turtle.pencolor() == user_bet.lower():
                print(f"You won! The winning turtle is {winning_color}!")
            else:
                print(f"Sorry, you guessed wrong. The winning turtle is {winning_color}.")
        else:
            steps = randint(0, 10)
            turtle.forward(steps)


screen.exitonclick()
