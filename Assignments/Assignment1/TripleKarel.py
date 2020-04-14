from karel.stanfordkarel import *

"""
File: TripleKarel.py
Diane Ngo
April 13, 2020
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""

def main():
    for i in range(2):
        paint_rectangle()
        turn_around()
    paint_rectangle()
    turn_right()

# Defines the turn_right function for Karel
def turn_right():
    for i in range(3):
        turn_left()

# Defines the turn_around function for Karel
def turn_around():
    turn_left()
    turn_left()

# Paints the 3 sides of a rectangle
def paint_rectangle():
    for i in range(2):
        paint_side()
        move()
    paint_side()

# If Karel is adjacent to a side of the building, paint
def paint_side():
    while left_is_blocked():
        put_beeper()
        move()
    turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
