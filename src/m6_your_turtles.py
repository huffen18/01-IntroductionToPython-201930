"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Elijah Huff.
"""
########################################################################
#   DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
dan = rg.SimpleTurtle('turtle')
dan.pen = rg.Pen('pink',5)
dan.speed = 30
size = 200
for k in range(10):
    dan.draw_circle(size)
    dan.pen_up()
    dan.right(135)
    dan.forward(5)
    dan.left(135)
    dan.pen_down()
    size = size + 18
#######################################################################

#######################################################################
window.tracer(100)

bob = rg.SimpleTurtle('square')
bob.pen = rg.Pen('yellow',8)
bob.forward(10)
for k in range(600):
    bob.right(30)
    bob.forward(k)


window.close_on_mouse_click()
#######################################################################
