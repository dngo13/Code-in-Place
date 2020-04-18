# File: StepUp.py
# This tells PyCharm who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

# this program executes in a special function called main
def main():
    # Commands in the run method are executed one at a time
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    # Have Karel turn right
    turn_right()
    move()
    put_beeper()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# This is "boilerplate" code which launches your code
# when you type "python StepUp.py" in the terminal
if __name__ == "__main__" :
    run_karel_program()

