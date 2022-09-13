import turtle
from turtle import Turtle, Screen
import random
# tim = Turtle()
screen = Screen()
# screen.listen()
#
#
# def move_forward():
#     tim.forward(10)
#
#
# def backwards():
#     tim.back(10)
#
#
# def left():
#     tim.left(10)
#
#
# def right():
#     tim.right(10)
#
#
# def clear():
#     tim.reset()
#
#
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=backwards)
# screen.onkey(key="a", fun=left)
# screen.onkey(key="d", fun=right)
# screen.onkey(key="c", fun=clear)
is_race_on = False

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick a colour: ")
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []
for turtle_index in range(6):
    new_turtle= Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost, The {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
