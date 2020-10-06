import random
import countdown


print("What's up everybody! Welcome to MagicCheck")
print("Here, you will enter tasks needed to be done in a Magic 8-ball.")
print("Shake the Magic 8-ball to randomly pick which task to do next, and it will start your timer.")
print("Set the timer for however many minutes you would like.")
print("Once your time is up, click \"Yes\" or \"No\" to check off the task.")

num_tasks = int(input("How many tasks will you be completing today? "))
tasks = []
for i in range(num_tasks):
    task = str(input("What would you like to get done today? "))
    tasks.append(task)

shake = input("Enter shake to choose a task: ")
if shake.lower() == "shake":
    print(random.choice(tasks))
else: 
    print("Invalid input. No problem, have a good day!")



input_complete = input('Did you complete your task? (Yes or No): ')
if input_complete.lower() == "yes":
    task_again = input("Congrats! You've completed your task. Would you like to try again? (Yes or No): ")
        
        


