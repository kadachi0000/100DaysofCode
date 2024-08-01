from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_pieces = ["head", "body", "tail"]

snake = []
starting_position = [(0, 0), (-20, 0), (-40, 0)]
i = 0
for piece in snake_pieces:
    piece = Turtle(shape="square")
    piece.color("white")
    piece.penup()
    piece.goto(starting_position[i])
    i += 1
    snake.append(piece)

game_running = True
while game_running:
    screen.update()
    time.sleep(.5)

    for piece in range(len(snake) - 1, 0, -1):
        new_x = snake[piece-1].xcor()
        new_y = snake[piece-1].ycor()
        snake[piece].goto(new_x, new_y)
    snake[0].forward(20)

snake = Snake()
snake.move()

screen.exitonclick()