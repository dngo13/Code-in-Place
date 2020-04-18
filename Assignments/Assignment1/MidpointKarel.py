from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Diane Ngo
April 16, 2020
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

def main():
    check_initial_pos()
    paint_loop_up()
    move_to_opposite()
    paint_loop_down()
    place_midpoint()
    move_to_opposite()
    erase_paint()
    move_to_opposite()
    erase_down()
    move_down()

def place_midpoint():
    if front_is_blocked():
        turn_right()
        put_beeper()
        paint_corner(BLANK)

"""
Pre: karel is facing east and front is clear
Post: karel is facing east and front is blocked
Move diagonally upward and paints each square blue
"""
def paint_loop_up():
    while front_is_clear():
        paint_corner(BLUE)
        move_diagonal()
    paint_corner(BLUE)
"""
Pre: karel is facing south and front is clear
Post: karel is facing south and tile is blue
"""
def paint_loop_down():
    while corner_color_is(BLANK):
        paint_corner(BLUE)
        move_diagonal()
    if corner_color_is(BLUE):
        move_down()
        paint_corner(BLUE)


def move_down():
    if facing_south():
        while front_is_clear():
            move()

def move_diagonal():
    if front_is_clear():
        turn_left()
        move()
        turn_right()
        if corner_color_is(BLUE):
            move_down()
        if front_is_clear():
            move()

def erase_down():
    while corner_color_is(BLUE):
        paint_corner(BLANK)
        move_diagonal()


def move_to_opposite():
    if facing_east():
        turn_around()
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    for i in range (3):
        turn_left()

def erase_paint():
    turn_left()
    while front_is_clear():
        paint_corner(BLANK)
        move_diagonal()
    paint_corner(BLANK)

def check_initial_pos():
    if left_is_blocked():
        if right_is_blocked():
            put_beeper()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()