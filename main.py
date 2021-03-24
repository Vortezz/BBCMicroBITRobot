#################################
# This code was made by Vortezz #
# and edited by Thebloodshadow  #
# NOTICE : Some value has to be #
#   edited before use           #
#################################
from microbit import *

#For test purpose

from basic import pause
from motorbit import forward as forward_test
from motorbit import back as back_test
from motorbit import right as left_test
from motorbit import left as right_test

#End what is needed for the test

seconds_launch = 0
seconds = 0

display.off()


def command_mot1(direction, speed):
    pin8.write_digital(direction)
    pin1.write_analog(speed)


def command_mot2(direction, speed):
    pin12.write_digital(direction)
    pin2.write_analog(speed)


def forward():
    command_mot1(0, 1023)
    command_mot2(1, 1023)

def stop():
    command_mot1(0, 0)
    command_mot2(1, 0)

def left():
    command_mot1(0, 1023)
    command_mot2(1, 0)
    
def right():
    command_mot1(0, 0)
    command_mot2(1, 1023)


def catapult_launch(): # Will send a pulse to your catpult after a certain amount of time
    stop()
    global seconds_launch
    if seconds_launch < 2:
        seconds_launch += 1
        pause(1000)
    else:
        pin3.write_digital(1)


while True:
    seconds += 1
    if seconds == 5:
        catapult_launch()
    elif pin7.read_digital() and pin6.read_digital():
        forward()
    elif pin6.read_digital():
        left()
    elif pin7.read_digital():
        right()
    else:
        stop()
    pause(1000)

# Test to see something (Motorbit may be more simple than sending a pulse to a pin)

forward_test(100)
pause(2000)
back_test(100)
pause(2000)
right_test(100)
pause(2000)
left_test(100)


