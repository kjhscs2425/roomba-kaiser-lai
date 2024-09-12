# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: kaiser lai <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)
 
###
# Start your code here
window = room.draw_room(level = 0)
for i in range(3):
      left(90)
      forward(160)
for i in range (2):
      left(90)
      forward(120)
for i in range(2):
      left(90)
      forward(80)

    
   

# End your code here
###
 
window.exitonclick()