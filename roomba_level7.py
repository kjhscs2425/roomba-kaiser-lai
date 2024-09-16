# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# THIS PARAMETER CAN CHANGE!!!
# Make sure your code works for n_alcoves = 0, 1, 2, 3, and 4
# (You are allowed to use this parameter in your code)
n_alcoves = 3

# Draw the Level 7 version of the room
window = room.draw_room(level = 7, n_alcoves = n_alcoves)

###
# Start your code here
sq = 40


forward(sq) 
left(90)
forward(sq*3)
backward(sq*6)
right(90)
forward(sq*1)
right(90)
forward(sq*1)
backward(sq*8)
left(90)
forward(sq*1)
right(90)
forward(sq*8)
left(90)
forward(sq)
left(90)
forward(sq*8)
right(90)
forward(sq)
right(90)
backward(sq)
forward(sq*10)
backward(sq)
left(90)
forward(sq)
left(90)
forward(sq*8)
right(90)
forward(sq)
right(90)
forward(sq*8)
left(90)
forward(sq)
left(90)
forward(sq*8)
backward(sq)
right(90)
forward(sq)
left(90)
backward(sq*6)
forward(sq*3)
right(90)
forward(sq)

forward(sq*10)

def sqrfunc(size):
    for i in range(4):
        forward(size)
        left(90)
        size = size + sq

sqrfunc(sq)
sqrfunc(sq*3)
sqrfunc(sq*4)
# End your code here
###
 
window.exitonclick()