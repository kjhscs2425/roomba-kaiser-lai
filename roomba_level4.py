# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 4 version of the room
window = room.draw_room(level = 4,radius = 5)

###
# Start your code here 
sq = 40

forward(sq*5)
def spiral(num):
    left(90)
    forward(num)

for i in range(2):
    spiral(sq)
for i in range(2):
    spiral(sq*2)
for i in range(2):
    spiral(sq*3)
for i in range(2):
    spiral(sq*4)
for i in range(2):
    spiral(sq*5)
for i in range(2):
    spiral(sq*6)
spiral(sq*7)
spiral(sq*6)
spiral(sq*7)
spiral(sq*7)
spiral(sq*6)
spiral(sq*7)
spiral(sq*7)
spiral(sq*6)
spiral(sq*7)
spiral(sq*7)
spiral(sq*6)
spiral(sq*4)
spiral(sq*3)
forward(sq*5)
backward(sq*10)
forward(sq*5)
right(90)
forward(sq*5)
backward(sq*5)
# End your code here
###
 
window.exitonclick()