from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Diane Ngo
April 15, 2020
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""

def main():
   turn_left()
   repair_bridge()

"""
Makes Karel turn right
Pre: none
Post: Karel is facing to the right of whichever
      direction Karel was facing previously
"""
def turn_right():
    for i in range(3):
        turn_left()
"""
Makes Karel turn to the direction behind
Pre: none
Post: Karel is facing behind whichever
      direction Karel was facing previously
"""
def turn_around():
    for i in range(2):
        turn_left()
# If there is no beeper in the column tile, put a beeper and move
def repair_pillar():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()
    if no_beepers_present():
        put_beeper()
    turn_around()
# Repeat repair_pillar for all 4 pillars
def repair_bridge():
    for i in range(4):
        repair_pillar()
        move_to_bottom()
        if front_is_clear():
            move_four()

"""
Pre: Karel's front is clear
Post: Karel is positioned so the front is clear"""
def move_to_bottom():
    while front_is_clear():
        move()
    turn_left()
"""
Karel moves 4 squares in her direction
Pre: Karel is facing east
Post: Karel is facing north to repair the pillar
"""
def move_four():
    for i in range(4):
        move()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
