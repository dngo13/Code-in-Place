from karel.stanfordkarel import *
"""
File: RoombaKarel.py
-------------------------
Pick up all the beepers in the world.
"""

def main():
    while left_is_clear():
        # Pre: Karel is facing east, start of row
        clear_row()
        next_row()
        # Post: Karel is facing East, start of row
    clear_row()

# Pre: Karel is at the start of a messy row
# Post: Karel is at the start of a clean row
def clear_row():
    while front_is_clear():
        safe_pick()
        move()
    safe_pick()

# Pick up, but only if there is a beeper
def safe_pick():
    if beepers_present():
        pick_beeper()

# Pre: Karel is at the end of a row
# Post: karel is at the start of the next messy row
def next_row():
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()
