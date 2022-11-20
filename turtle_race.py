from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor('lightgrey')

user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'yellow', 'blue', 'green', 'orange']
new_turtles = []

x_coord = -230
y_coord = -130


for i in range(len(colors)):
    color = Turtle(shape='turtle')
    color.penup()
    y_coord += 50
    color.goto(x=x_coord, y=y_coord)
    color.color(colors[i])
    new_turtles.append(color)

if user_bet:
    is_race_on = True


while is_race_on:
    
    # turtle.forward = random_distance
    for turtle in new_turtles:
        if turtle.xcor()>230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You\'ve won! The {winning_color} turtle is the winner!')
            else:
                print(f'You\'ve lost! The {winning_color} turtle is the winner!')
            is_race_on = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()