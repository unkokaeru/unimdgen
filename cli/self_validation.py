"""self_validation.py: A collection of utility functions for self-validation."""

import os
from logging import Logger
from typing import Callable
from winsound import Beep

from gtts import gTTS

from config.paths import LOG_PATH


def run_until_satisfied(logger: Logger, func: Callable, *args, **kwargs):
    """
    Repeatedly runs the given function with the specified arguments and keyword arguments,
    asking the user after each execution if they are satisfied with the output.
    :param logger: The logger object.
    :param func: The function to be run.
    :param args: The arguments to pass to the function.
    :param kwargs: The keyword arguments to pass to the function.
    """

    while True:
        # Execute the function with the provided arguments and keyword arguments.
        result = func(*args, **kwargs)

        # Display the result to the user.
        result_display = f"Function ({func.__name__}) output: {result}"
        logger.info(result_display)

        # Ask the user if they are satisfied with the output.
        Beep(1000, 1000)  # Beep at 1000 Hz for 1000 ms
        audio_obj = gTTS(text=result_display, lang="en", slow=False)
        audio_obj.save("output.mp3")
        os.system("start output.mp3")
        os.remove("output.mp3")

        user_input = (
            input("Are you satisfied with the output? (yes/no): ").strip().lower()
        )

        # Log the user input in a text file.
        with open(LOG_PATH, "a") as file:
            file.write(user_input + "\n")

        # If the user is satisfied, break the loop and stop executing the function.
        if user_input == "yes":
            logger.info(
                "Function execution stopped as you are satisfied with the output."
            )
            return result
        elif user_input == "no":
            logger.info("Function will be run again.")
        else:
            logger.warning(
                "Unrecognized input. Please type 'yes' to stop or 'no' to run the function again."
            )
