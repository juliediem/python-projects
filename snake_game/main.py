import turtle
from turtle import Screen, Turtle
import snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# screen.tracer(0)

snake = snake.Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    # The higher the time sleep is, the slower the snake parts move
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
