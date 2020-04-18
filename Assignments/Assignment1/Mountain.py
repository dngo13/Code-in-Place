from karel.stanfordkarel import *

"""
File: Mountain.py
--------------------------
Karel climbs a mountain of any size
and plants a beeper at the top
"""
def main():
    ascend_mountain()
    put_beeper()
    descend_mountain()
# Pre: Karel is at the top of a mountain
# Post: Karel is on the east side of the mountain
def descend_mountain():
    while front_is_clear():
        step_down()

def step_down():
    move()
    turn_right()
    move()
    turn_left()

# Pre: Karel is facing a mountain
# Post: Karel is on top of said mountain

def ascend_mountain():
    while front_is_blocked():
        step_up()

# Pre: Karel is facing a step of the mountain
# Post: Karel is up one step also facing the mountain

def step_up():
    turn_left()
    move()
    turn_right()
    move()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()