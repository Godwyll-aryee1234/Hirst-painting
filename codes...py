import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('image hirst.jpg', 100)

x_dist = 40
y_dist = 40
x_start = -100
y_start= -100

turtle = Turtle()
screen = Screen()
turtle.penup()
screen.colormode(1)


def circle():
    color = random.choice(colors).rgb
    color_options = (color.r / 255, color.g / 255, color.b / 255)
    turtle.color(color_options)
    turtle.speed(200)
    turtle.begin_fill()
    turtle.dot(20)
    turtle.end_fill()
    turtle.hideturtle()

for row in range(8):
    for col in range(9):
        turtle.teleport(x_start + col * x_dist, y_start + row * y_dist)
        circle()

screen.exitonclick()
