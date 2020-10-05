# import the time module
import time

# define the countdown func.


def countdown(t):

    while t:
        hours, remainder = divmod(t, 3600)
        mins, secs = divmod(remainder, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


# input time in minutes
t = input("Enter the time in minutes: ")

# function call
countdown(int(t))
