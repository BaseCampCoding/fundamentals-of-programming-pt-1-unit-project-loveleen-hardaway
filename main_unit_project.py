import random
import inputValidation
import time

print("\nWhat's up everybody! Welcome to MagicCheck")
spacebar = input("\nHit enter to proceed. ")
print("\nHere, you will enter tasks needed to be done in a Magic 8-ball.")

spacebar = input("\nHit enter to proceed. ")


print("\nShake the Magic 8-ball to randomly pick which task to do next, and it will start your timer.")
print("Set the timer for however many minutes you would like.")
print("Once your time is up, click \"Yes\" or \"No\" to check off the task.")

spacebar = input("\nHit enter to proceed. ")
num_tasks = int(input("\nHow many tasks will you be completing today? "))

tasks = []
for i in range(num_tasks):
    task = str(input("\nWhat would you like to get done today? "))
    tasks.append(task)

for i in range(num_tasks):
    shake = input("\nEnter shake to choose a task: ")

    # shake command validation
    shake_validation = inputValidation.input_shake_valid(shake.lower())
    while shake_validation == False:
        print("Invalid input. Try Again.")
        shake = input("Enter shake to choose a task: ")
        shake_validation = inputValidation.input_shake_valid(shake.lower())
    task_shook = random.choice(tasks)
    print(task_shook)




    # function call
    
    while True:
        t = input("How many minutes/ seconds?: ")
        if t.isdigit():
            t = int(t)
            break
        else:
            print("Please enter an integer.")


    def countdown():
        global t
        choice = input("Do you want seconds or minutes counting down? ")
        
        if choice == "seconds":
            converted_t = int(t)
        elif choice == "minutes":
            converted_t = int(t) * 60


        while converted_t >= 0:
            hours, quotient = divmod(converted_t, 3600)
            mins, secs = divmod(quotient, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            converted_t -= 1

    countdown()


    input_complete = input('Did you complete your task? (Yes or No): ')
    input_complete_validation = inputValidation.input_complete_valid(input_complete.lower())
    while input_complete_validation == False:
        print("Invalid input. Try Again.")
        input_complete = input('Did you complete your task? (Yes or No): ')
        input_complete_validation = inputValidation.input_complete_valid(input_complete.lower())
        
    if input_complete.lower() == "yes":
        # NEEDS TO REMOVE TASK JUST DONE RIGHT HERE
        updated_tasks = tasks.remove(task_shook)

        # i==0 means you are the first place
        # t is overwritten each time
        # task_shook is overwritten each time
        # task_shook will always be associated with it's t because it is in the same iteration
        if i == 0:
            minimum_time = t
            minimum_task = task_shook
        else:
            if t < minimum_time:
                minimum_time = t
                minimum_task = task_shook

        task_again = input(f"Congrats! {minimum_task} is the fastest task you've completed so far. You have {tasks} left to do. Would you like to try again? (Yes or No): ")
        if task_again.lower() == "yes":
            continue
        elif task_again.lower() == "no":
            break
    elif input_complete.lower() == "no":
        try_same_task_again = input("Would you like to try the same task again? (Yes or No): ")
        try_again = inputValidation.try_again_input(try_same_task_again)
        # starts over the same task 
        if try_again == "yes":
            # input time in minutes
            t = input("Enter the time in minutes: ")

            start_countdown = str(input("Enter 'Start' to begin countdown: "))
            # start command input validation
            start_command_validation = inputValidation.is_valid_input(start.lower())
            while start_command_validation == False:
                print("Invalid input. Try Again.")
                start = str(input("Enter 'Start' to begin countdown: "))
                start_command_validation= inputValidation.is_valid_input(start.lower())

            # function call
            countdown.countdown(int(t))   

            # check again
            input_complete = input('Did you complete your task? (Yes or No): ')
            input_complete_validation = inputValidation.input_complete_valid(input_complete.lower())
            while input_complete_validation == False:
                print("Invalid input. Try Again.")
                input_complete = input('Did you complete your task? (Yes or No): ')
                input_complete_validation = inputValidation.input_complete_valid(input_complete.lower())

                if input_complete.lower() == "yes":
                    # NEEDS TO REMOVE TASK JUST DONE RIGHT HERE
                    updated_tasks = tasks.remove(task_shook)

                    task_again = input(f"Congrats! You've completed your task. You have {tasks} left to do. Would you like to try again? (Yes or No): ")
                    if task_again.lower() == "yes":
                        continue
                    elif task_again.lower() == "no":
                        break
                elif input_complete.lower() == "no":
                    try_same_task_again = input("Would you like to try the same task again? (Yes or No): ")
                    try_again = inputValidation.try_again_input(try_same_task_again)
        elif try_again == "no":
            continue

print("See you later!")
# results of fastest task vs. slowest task





# how to store stopwatch time
# begin = time.time()
# end = time.time()
# time_elapsed = int(begin - end)ye