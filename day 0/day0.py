from turtle import *

#we want to paint a house
shape("circle")
#step 1:  draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()


begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()


begin_fill()
color("purple")














exitonclick()