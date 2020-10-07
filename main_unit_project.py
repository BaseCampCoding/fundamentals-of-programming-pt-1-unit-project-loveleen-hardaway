import random
import countdown


print("What's up everybody! Welcome to MagicCheck")
spacebar = input("Hit spacebar to proceed. ")
if spacebar == " ":
    print("Here, you will enter tasks needed to be done in a Magic 8-ball.")

spacebar = input("Hit spacebar to proceed. ")

if spacebar == " ":
    print("Shake the Magic 8-ball to randomly pick which task to do next, and it will start your timer.")
    print("Set the timer for however many minutes you would like.")
    print("Once your time is up, click \"Yes\" or \"No\" to check off the task.")

num_tasks = int(input("How many tasks will you be completing today? "))
tasks = []
for i in range(num_tasks):
    task = str(input("What would you like to get done today? "))
    tasks.append(task)

for i in range(num_tasks):
    shake = input("Enter shake to choose a task: ")
    shake_validation == countdown.is_valid(shake.lower())
    # shake command validation
    while shake_validation == False:
        print("Invalid input. Try Again.")
        shake = input("Enter shake to choose a task: ")

    # input time in minutes
    t = input("Enter the time in minutes: ")

    start_countdown = str(input("Enter 'Start' to begin countdown: "))
    while 
    # function call
    countdown(int(t))


    input_complete = input('Did you complete your task? (Yes or No): ')
    if input_complete.lower() == "yes":
        task_again = input(f"Congrats! You've completed your task. You have {tasks} left to do. Would you like to try again? (Yes or No): ")
        if task_again.lower() == "yes":
            continue
        elif task_again.lower() == "no":
            break
    elif input_complete.lower() == "no":
        try_same_task_again = input("Would you like to try the same task again? (Yes or No): ")
        try_again = countdown.try_again_input(try_same_task_again)
        # starts over the same task 
        while try_again == False:
            # input time in minutes
            t = input("Enter the time in minutes: ")

            start_countdown = str(input("Enter 'Start' to begin countdown: "))
            # function call
            countdown(int(t))
            # check again
            input_complete = input('Did you complete your task? (Yes or No): ')
            if input_complete.lower() == "yes":
                task_again = input("Congrats! You've completed your task. You have {tasks} left to do. Would you like to try again? (Yes or No): ")
                if task_again.lower() == "yes":
                    continue
                elif task_again.lower() == "no":
                    break
            elif input_complete.lower() == "no":
                try_same_task_again = input("Would you like to try the same task again? (Yes or No): ")
                try_again = countdown.try_again_input(try_same_task_again)

print("See you later!")
