"""cli_interface.py: Command-Line Interface Interface File"""

from logging import Logger

from unimdgen.cli.self_validation import run_until_satisfied
from unimdgen.config.constants import MODULE_FOLDER
from unimdgen.content.class_generator import ClassGenerator
from unimdgen.content.module_page import module_page
from unimdgen.content.notes_generator import fetch_notes_outline, notes
from unimdgen.content.revision_generator import revision
from unimdgen.content.summary_generator import summaries


def ask_to_run(logger: Logger, function: callable, *args):
    """
    Asks the user if they would like to run a function.
    :param logger: The logger object.
    :param function: The function to run.
    :param args: The arguments to pass to the function.
    """

    run = ""
    while run != "y" and run != "n":
        run = input(f"Run {function.__name__}? (y/n): ").strip().lower()
        if run == "y":
            return function(*args)
        elif run == "n":
            logger.info(f"Skipping {function.__name__}.")
            if function.__name__ == "module_gen":
                data = {
                    "module_name": MODULE_FOLDER,
                    "name": None,
                    "email": None,
                    "assessment_weighting_percentages": None,
                    "learning_outcomes": None,
                    "module_notes_outline": fetch_notes_outline(logger),
                }

                return data
        else:
            logger.error("Invalid input. Please try again.")


def interface(logger: Logger) -> None:
    """
    The command-line interface for the program.
    :param logger: The logger object.
    :return: None
    """

    # Generate the main module page
    def module_gen():
        return run_until_satisfied(logger, module_page, logger)

    module_data = ask_to_run(logger, module_gen)

    # Generate the class pages
    classes = ClassGenerator(logger, module_data)
    ask_to_run(logger, classes.generate_all, "practical")
    ask_to_run(logger, classes.generate_all, "tutorial")

    # Genearte the summary pages
    ask_to_run(logger, summaries, logger, module_data)

    # Generate the test papers
    ask_to_run(logger, classes.generate_all, "paper")

    # Generate the notes
    ask_to_run(logger, notes, logger, module_data["module_notes_outline"])

    # Generate the revision pages
    ask_to_run(logger, revision, logger, module_data)
