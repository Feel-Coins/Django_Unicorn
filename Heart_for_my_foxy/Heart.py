from turtle import *
from time import sleep

# start from bottom
right(90)
penup()
forward(275)
left(90)
pendown()

# mane code
begin_fill()
color('red')
pensize(3)
left(50)
forward(133*2)
circle(100, 200)
right(140)
circle(100, 200)
forward(133*2)
end_fill()

sleep(5)
