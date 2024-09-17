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

# Draw the Level 3 version of the room
window = room.draw_room(level = 3, radius = 5)

###
# Start your code here
sq = 40

forward(sq*5)
def ski(bidi):
    left(90)
    forward(bidi)
  

ski(sq)
ski(sq)
ski(sq*2)
ski(sq*2)
ski(sq*3)
ski(sq*3)
ski(sq*4)
ski(sq*4)
ski(sq*5)
ski(sq*5)
ski(sq*6)
ski(sq*6)
ski(sq*7)
ski(sq*6)
ski(sq*8)
ski(sq*6)
ski(sq*7)
ski(sq*7)
ski(sq*6)
ski(sq*8)
ski(sq*6)
ski(sq*4)
ski(sq*3)

forward(sq*5)
backward(sq*10)
forward(sq*5)
right(90)
forward(sq*5)
backward(sq*10)
forward(sq*5)
 
# End your code here
###
 
window.exitonclick()