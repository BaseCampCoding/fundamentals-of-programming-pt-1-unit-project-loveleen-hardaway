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

   


# input validation loop for trying the same task again.
def try_again_input(try_same_task_again: str) -> bool:
    if try_same_task_again == "yes":
        return False
    elif try_same_task_again == "no":
        return True