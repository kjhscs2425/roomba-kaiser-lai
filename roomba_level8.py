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
# THIS PARAMETER CAN CHANGE!!!
# Make sure your code works for any positive integer value of cirlce_room_radius
# (You are allowed to use this parameter in your code)
circle_room_radius = 2

# Draw the Level 5 version of the room
window = room.draw_room(level = 8,
                        n_alcoves = n_alcoves,
                        radius = circle_room_radius)

###
# Start your code here
sq = 40
 
forward(sq)
right(90)
forward(sq)
backward(sq*2)
forward(sq)
left(90)
forward(sq*2)
right(90)
forward(sq)
for i in range(2):
    left(90)
    forward(sq*2)
left(90)
forward(sq)
left(90)
forward(sq*5)
backward(sq)
left(90)
forward(sq)
backward(sq*2)
forward(sq)
left(90)
forward(sq*4)
left(90)
forward(sq)
backward(sq)
right(90)
forward(sq*3)
backward(sq)
left(90)
forward(sq)
backward(sq*2)




 
 
# End your code here
###
 
window.exitonclick()