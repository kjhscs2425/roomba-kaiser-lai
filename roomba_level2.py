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

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)

###
# Start your code here


sq = 40

def srfunc(num):    
    forward(num)
    left(90)
        

srfunc(sq*14)
srfunc(sq*19)
srfunc(sq*14)
srfunc(sq*18)
srfunc(sq*13)
srfunc(sq*17)
srfunc(sq*12)
srfunc(sq*16)
srfunc(sq*11)
srfunc(sq*15)
srfunc(sq*10)
srfunc(sq*14)
srfunc(sq*9)
srfunc(sq*13)
srfunc(sq*8)
srfunc(sq*12)
srfunc(sq*7)
srfunc(sq*11)
srfunc(sq*6)
srfunc(sq*10)
srfunc(sq*5)
srfunc(sq*9)
srfunc(sq*4)
srfunc(sq*8)
srfunc(sq*3)
srfunc(sq*7)
srfunc(sq*2)
srfunc(sq*6)
srfunc(sq*1)
srfunc(sq*5)



# End your code here
###
 
window.exitonclick()