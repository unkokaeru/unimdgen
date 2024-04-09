"""The main module."""

import os
import re
from logging import Logger
from pathlib import Path
from time import time

from config import (
    CLASSES_PATH,
    INPUT_COST,
    INPUT_PATH,
    LOG_PATH,
    OUTPUT_COST,
    OUTPUT_PATH,
    PAPERS_PATH,
    REVISION_PATH,
    SUMMARY_PATH,
    TOKENS_PATH,
)
from data_gen import (
    class_data_gen,
    flashcards_data_gen,
    module_data_gen,
    notes,
    revision_data_gen,
    summarynotes_data_gen,
    summaryquestions_data_gen,
    tests_data_gen,
)
from utils import currency_converter, generate_markdown, get_logger, run_until_satisfied

"""
Things to implement:
- Use lecture slides to supplement the notes, including links to the slides
    (by reading each lecture slides,
    tagging them with their content,
    then organising into the main contents).
- GUI?
- Question-based revision note generation (cheat sheet).
- Create predicted papers.
- Include link description in prompt for note generation.

Things to fix:
- Code layout, file structure, and naming conventions.
- Documentation (update).
- Further GPT data generation cleaning.
- Flashcard tweaking & user checking.
- Change Anki flashcard generation.
- Refine summary notes prompt.
- UK spelling.
"""


def module_page(logger: Logger) -> dict[str, str]:
    """
    Generate the main module markdown file.
    :param logger: The logger object.
    :return: The module data for other functions to access.
    """

    logger.info("Generating main module markdown file...")

    attempts = 0
    while attempts < 5:
        try:
            module_data = module_data_gen(logger)
            break
        except IndexError as e:
            logger.warning(f"IndexError: {e}. Retrying...")
            attempts += 1
            if attempts == 5:
                logger.error("Failed to generate module data.")
                raise
        except TypeError as e:
            logger.warning(f"TypeError: {e}. Retrying...")
            attempts += 1
            if attempts == 5:
                logger.error("Failed to generate module data.")
                raise

    generate_markdown(
        logger,
        OUTPUT_PATH,
        "module_template",
        module_data["module_name"],
        module_data,
    )

    logger.info("Main module markdown file generated successfully.")

    return module_data


class ClassGenerator:
    def __init__(self, logger: Logger, module_data: dict[str, str]):
        """
        Initialize the ModuleContentGenerator with a logger and module data.
        :param logger: The logger object for logging information.
        :param module_data: A dictionary containing module-specific data.
        """
        self.logger = logger
        self.module_data = module_data
        self.input_base_path = INPUT_PATH
        self.class_output_path = CLASSES_PATH
        self.paper_output_path = PAPERS_PATH

    def generate_all(self, content_type: str) -> None:
        """
        Generate markdown files for the specified content type (tutorial, practical, or paper).
        :param content_type: A string specifying the content type ('tutorial', 'practical', or 'paper').
        :return: None
        """
        content_path = os.path.join(self.input_base_path, f"{content_type}s")
        self.logger.info(f"Generating {content_type} {"(exam)" if content_path == "paper" else "class"} markdown files...")

        def generate(item: str) -> None:
            attempts, item_questions = 0, None
            while attempts < 3:
                item_questions = class_data_gen(
                    self.logger, item, content_type
                )
                if item_questions["class_questions"] is not None:
                    break
                else:
                    attempts += 1

            if item_questions:
                file_title = (
                    f"{self.module_data['module_name']} {"Exam" if content_type == "paper" else f"{content_type.capitalize()} Class"} "
                    + re.sub(".pdf", "", item)
                )
                generate_markdown(
                    self.logger,
                    self.paper_output_path if content_type == "paper" else self.class_output_path,
                    "class_template",
                    file_title,
                    item_questions,
                )

        for item in os.listdir(content_path):
            run_until_satisfied(self.logger, generate, item)

        self.logger.info(
            f"{content_type.capitalize()} {"(exam)" if content_path == "paper" else "class"} markdown files generated successfully."
        )


def summaries(logger: Logger, module_data: dict[str, str]) -> None:
    """
    Generate the summary markdown files.
    :param logger: The logger object.
    :param module_data: The module data.
    :return: None
    """

    logger.info("Generating summary markdown files...")

    generate_markdown(
        logger,
        SUMMARY_PATH,
        "module_summary_questions",
        module_data["module_name"] + " Summary Questions",
        summaryquestions_data_gen(logger),
    )

    generate_markdown(
        logger,
        SUMMARY_PATH,
        "module_practice_tests",
        module_data["module_name"] + " Practice Tests",
        tests_data_gen(logger),
    )

    run_until_satisfied(
        logger,
        generate_markdown,
        logger,
        SUMMARY_PATH,
        "module_summary_notes",
        module_data["module_name"] + " Summary Notes",
        summarynotes_data_gen(logger),
    )

    logger.info("Summary markdown files generated successfully.")


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


def main() -> None:
    """
    The main function.
    :return: None
    """

    # Initialise logger
    logger = get_logger()

    # Change working directory
    os.chdir(Path(__file__).parent.parent)

    # Start timer
    start_time = time()

    # Generate main markdown file
    module_data = run_until_satisfied(logger, module_page, logger)

    # Generate class markdown files
    classes = ClassGenerator(logger, module_data)
    classes.generate_all("practical")
    classes.generate_all("tutorial")

    # Generate summary markdown files
    summaries(logger, module_data)

    # Generate paper markdown files
    classes.generate_all("paper")

    # Generate notes markdown files
    notes(logger, module_data["module_notes_outline"])

    # Generate revision markdown files
    revision(logger, module_data)

    # End timer
    time_taken = time() - start_time
    if time_taken < 60:
        logger.info(f"Time taken: {time_taken:.2f} seconds")
    elif time_taken < 3600:
        logger.info(f"Time taken: {time_taken / 60:.2f} minutes")
    elif time_taken < 86400:
        logger.info(f"Time taken: {time_taken / 3600:.2f} hours")
    else:
        logger.info(f"Time taken: {time_taken / 86400:.2f} days")

    # Calculate success percentage in input
    with open(LOG_PATH, "r") as f:
        log = f.read()

    yes = log.count("yes")
    no = log.count("no")

    if yes + no != 0:
        logger.info(f"Success percentage: {yes / (yes + no) * 100:.2f}%")

    os.remove(LOG_PATH)

    # Calculate cost to run
    with open(TOKENS_PATH, "r") as f:
        tokens = f.read()

    lines = tokens.split("\n")

    cost = 0

    for line in lines:
        line = line.split(", ")
        try:
            cost += int(line[0]) * INPUT_COST + int(line[1]) * OUTPUT_COST
        except ValueError:
            logger.warning("Encountered a line with unexpected format:", line)

    os.remove(TOKENS_PATH)

    logger.info(f"Cost to run: ${cost:.2f}, £{currency_converter(logger, cost, "USD", "GBP"):.2f}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        get_logger().info("Program terminated by user.")
    except Exception as e:
        get_logger().exception(e)
        raise
