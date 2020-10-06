# import the time module
import time

# define the countdown func.


def countdown(t):
    converted_t = int(t) * 60

    while converted_t >= 0:
        hours, quotient = divmod(converted_t, 3600)
        mins, secs = divmod(quotient, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        converted_t -= 1

    input_complete = input('Did you complete your task? (Yes or No): ')
    if input_complete.lower() == "yes":
        task_again = print("Congrats! You've completed your task. Would you like to try again? (Yes or No): ")
        



# input time in minutes
t = input("Enter the time in minutes: ")
# function call
countdown(int(t))
