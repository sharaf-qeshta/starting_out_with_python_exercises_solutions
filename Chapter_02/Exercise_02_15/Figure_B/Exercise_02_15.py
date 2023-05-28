"""
15.Turtle Graphics Drawings
Use the turtle graphics library to write programs that reproduce each of the designs shown
in Figure 2-34.

@author Sharaf Qeshta
"""

# Figure B
import turtle

x = turtle.xcor()
y = turtle.ycor()

turtle.down()

turtle.goto(x+100, y+100)
turtle.goto(x+200, y)
turtle.goto(x+100, y+50)
turtle.goto(x, y)
turtle.goto(x+200, y)

turtle.hideturtle()
turtle.done()
