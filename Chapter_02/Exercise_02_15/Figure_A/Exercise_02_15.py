"""
15.Turtle Graphics Drawings
Use the turtle graphics library to write programs that reproduce each of the designs shown
in Figure 2-34.

@author Sharaf Qeshta
"""

# Figure A
import turtle

CENTER_X = turtle.xcor()
CENTER_Y = turtle.ycor()

turtle.down()

turtle.goto(CENTER_X-50, CENTER_Y-50)
turtle.goto(CENTER_X-100, CENTER_Y)
turtle.goto(CENTER_X-50, CENTER_Y+50)
turtle.goto(CENTER_X, CENTER_Y)
turtle.goto(CENTER_X+50, CENTER_Y-50)
turtle.goto(CENTER_X+100, CENTER_Y)
turtle.goto(CENTER_X+50, CENTER_Y+50)
turtle.goto(CENTER_X, CENTER_Y)

turtle.hideturtle()
turtle.done()
