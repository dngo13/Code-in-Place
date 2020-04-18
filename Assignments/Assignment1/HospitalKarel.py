from karel.stanfordkarel import *

def main():
    build_all_hospitals()

def move_to_hospital():
    if facing_east():
        while no_beepers_present():
            move()
        turn_left()

def build_hospital():
    move()
    for i in range(2):
        put_beeper()
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
        put_beeper()
    turn_left()

def build_all_hospitals():
    for i in range(3):
        move_to_hospital()
        build_hospital()
        if front_is_clear():
            move()

def turn_right():
    for i in range(3):
        turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()