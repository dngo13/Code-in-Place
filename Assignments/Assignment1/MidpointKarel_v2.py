from karel.stanfordkarel import *

"""
File: MidpointKarel.py
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
    # put_beeper()
    paint_edges()
    move()
    while corner_color_is(BLANK):
        move()
    turn_around()
    move()
    check_paint()
    while corner_color_is(BLANK):
        move()
        check_paint()
        if corner_color_is(BLUE):
            turn_around()
            move()
            move()
            if corner_color_is(BLUE):
                turn_around()
                move()
                if corner_color_is(BLANK):
                    put_beeper()
                    move()
    erase_paint()

def erase_paint():
    while corner_color_is(BLUE):
        while front_is_clear():
            paint_corner(BLANK)
            move()
        turn_around()
    move()
def paint_edges():
    paint_corner(BLUE)
    while front_is_clear():
        move()
    paint_corner(BLUE)
    turn_around()

def turn_around():
    turn_left()
    turn_left()

def check_paint():
    if corner_color_is(BLANK):
        paint_corner(BLUE)
        move()



def check_block():
    move()
    while front_is_clear():
        while no_beepers_present():
            move()
            if beepers_present():
                turn_around()
                move()
                put_beeper()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()


