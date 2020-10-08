valid_inputs = [
    "shake",
    "start",
]


def is_valid_input(start: str) -> bool:
    for input in valid_inputs:
        if start.lower() in valid_inputs[1]:
            return True
        else:
            return False


def input_complete_valid(input_complete: str) -> bool:
    """Return if the input is valid.
    """
    if input_complete == "yes" or "no":
        return True
    else:
        return False


def input_shake_valid(shake: str) -> bool:
    """Return if the input is shake
    """
    for input in valid_inputs:
        if shake.lower() == "shake":
            return True
        else:
            return False



# input validation loop for trying the same task again.
def try_again_input(try_same_task_again: str) -> bool:
    if try_same_task_again == "yes":
        return False
    elif try_same_task_again == "no":
        return True