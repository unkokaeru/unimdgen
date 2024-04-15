"""revision_generator.py: A module for generating the revision markdown files."""

import os
from logging import Logger

from processing.gpt_interaction import prompt_gpt
from utilities.conversion_utilities import markdown_to_csv
from utilities.file_utilities import generate_markdown
from sudoku_generator import sudoku_gen

from cli.self_validation import run_until_satisfied
from config.paths import NOTES_PATH, REVISION_PATH


def flashcards_data_gen(logger: Logger) -> dict[str, str]:
    """
    Generate data for the flashcards markdown files.
    :param logger: Logger object
    :return: flashcards and anki flashcards
    """

    data = {
        "flashcards": None,
        "anki_flashcards": None,
    }

    # Loop through each note markdown file and generate flashcards
    flashcards = """"""
    card_format = """
### Question

QUESTION

### Answer

ANSWER

---

"""

    for file in os.listdir(NOTES_PATH):
        with open(f"{NOTES_PATH}{file}", "r", encoding='utf-8') as f:
            content = f.read()
            flashcard = prompt_gpt(logger, content, f"You're a program that takes a markdown note and generates a list of flashcards from it, each flashcard containing a question on one side and the answer on the other. Return the list of flashcards in the following format: {card_format}")
            logger.info(f"Flashcard: {flashcard}")
            flashcards += flashcard

    data["flashcards"] = flashcards.replace("---###", r"---\n\n###")
    data["anki_flashcards"] = f"[{markdown_to_csv(logger, flashcards, "flashcards")}]({REVISION_PATH}flashcards.csv)"

    return data


def revision_data_gen(logger: Logger, module_name: str) -> dict[str, str]:
    """
    Generate data for the question-based revision markdown files.
    :param logger: Logger object
    :param module_name: Name of the module
    :return: module name, question-based revision
    """

    data = {
        "module_name": module_name,
        "question_based_revision": None, # TODO: No idea how to generate this yet
        "sudoku_orig": None,
        "sudoku_sol": None,
    }

    data["sudoku_orig"], data["sudoku_sol"] = sudoku_gen()

    return data


def revision(logger: Logger, module_data: dict[str, str]) -> None:
    """
    Generate the revision markdown files.
    :param logger: The logger object.
    :param module_data: The module data.
    :return: None
    """

    logger.info("Generating revision markdown files...")

    run_until_satisfied(
        logger,
        generate_markdown,
        logger,
        REVISION_PATH,
        "module_flashcards",
        module_data["module_name"] + " Flashcards",
        flashcards_data_gen(logger),
    )

    generate_markdown(
        logger,
        REVISION_PATH,
        "module_question_based_revision",
        module_data["module_name"] + " Question-Based Revision",
        revision_data_gen(logger, module_data["module_name"]),
    )

    logger.info("Revision markdown files generated successfully.")
