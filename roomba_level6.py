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
window = room.draw_room(level = 6, radius = 5)

###
# Start your code here
speed(40)
sq = 40
left(180)
forward(sq*3)
right(90)
def sqrfunc(spiral):
        forward(spiral)
        right(90)

sqrfunc(sq*6)
sqrfunc(sq*14)
sqrfunc(sq*12)
sqrfunc(sq*13)
sqrfunc(sq*13)
for i in range(2):
      sqrfunc(sq*14)
sqrfunc(sq*13)
sqrfunc(sq*15)
sqrfunc(sq*12)
sqrfunc(sq*16)
sqrfunc(sq*12)
sqrfunc(sq*16)
sqrfunc(sq*11)
sqrfunc(sq*13)
for i in range(2):
       sqrfunc(sq*10)
sqrfunc(sq*9)
sqrfunc(sq*14)
sqrfunc(sq*8)
sqrfunc(sq*18)
sqrfunc(sq*8)
sqrfunc(sq*18)
sqrfunc(sq*7)
sqrfunc(sq*15)
sqrfunc(sq*11)
sqrfunc(sq*13)
sqrfunc(sq*15)
sqrfunc(sq*11)
sqrfunc(sq*16)
sqrfunc(sq*8)
sqrfunc(sq*18)
sqrfunc(sq*7)
sqrfunc(sq*12)
sqrfunc(sq*9)
sqrfunc(sq*11)
sqrfunc(sq*8)
sqrfunc(sq*10)
sqrfunc(sq*5)
sqrfunc(sq*4)
sqrfunc(sq*4)
sqrfunc(sq*3)
sqrfunc(sq*3)
sqrfunc(sq*2)
sqrfunc(sq*2)
sqrfunc(sq)

forward(sq*10)
backward(sq*20)
forward(sq*10)
right(90)
forward(sq*10)
backward(sq*20)
forward(sq*10)
forward(sq*9)
right(90)
forward(sq*4)

# End your code here
###
 
window.exitonclick()