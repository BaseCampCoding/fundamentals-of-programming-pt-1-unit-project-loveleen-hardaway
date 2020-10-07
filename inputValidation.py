valid_inputs = [
    "shake",
    "start",
]


def is_valid_input(start: str) -> bool:
    for input in valid_inputs:
        if start.lower() == input:
            return True
    return False


def input_complete_valid(input_complete: str) -> str:
    """Return if the input is valid.
    """
    if input_complete == "yes":
        print("Congrats! You've completed your task. Would you like to try again? (Yes or No): ")
    elif input_complete == "no":
        print("Would you like to try again")


def input_shake_valid(shake: str) -> str:
    """Return if the input is shake
    """
    if shake.lower() == "shake":
        print(random.choice(tasks))
    else:
        print("Invalid input. No problem, have a good day!")


while True:
    input_name = input("What is your name? ")
    is_valid = is_valid_input(input_name)
    if is_valid:
        print("If your name is valid. ")
        break
    else:
        print("If your name is invalid.")
