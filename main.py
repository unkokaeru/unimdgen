"""The main module."""

import os
import re
from logging import Logger
from pathlib import Path
from time import time

from data_gen import (
    class_data_gen,
    flashcards_data_gen,
    module_data_gen,
    revision_data_gen,
    notes,
    summarynotes_data_gen,
    summaryquestions_data_gen,
    tests_data_gen,
)
from utils import generate_markdown, get_logger, run_until_satisfied

"""
Things to implement:
- Use lecture slides to supplement the notes, including links to the slides
    (by reading each lecture slides,
    tagging them with their content,
    then organising into the main contents).

Things to fix:
- Code layout, file structure, and naming conventions.
- Error handling.
- Logging.
- Documentation.
- Further GPT data generation cleaning.
- Edge cases.
- Flashcard tweaking & user checking.
- Change Anki flashcard generation.
"""


def module_page(logger: Logger) -> dict[str, str]:
    """
    Generate the main module markdown file.
    :param logger: The logger object.
    :return: The module data for other functions to access.
    """

    logger.info("Generating main module markdown file...")

    module_data = module_data_gen(logger)

    generate_markdown(
        logger,
        "C:/Users/wills/Documents/GitHub/module-generation/output/",
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
        self.input_base_path = (
            "C:/Users/wills/Documents/GitHub/module-generation/input/"
        )
        self.output_path = (
            "C:/Users/wills/Documents/GitHub/module-generation/output/classes/"
        )

    def generate_all(self, content_type: str) -> None:
        """
        Generate markdown files for the specified content type (tutorial or practical).
        :param content_type: A string specifying the content type ('tutorial' or 'practical').
        :return: None
        """
        content_path = os.path.join(self.input_base_path, f"{content_type}s")
        self.logger.info(f"Generating {content_type} class markdown files...")

        def generate(item: str) -> None:
            attempts, item_questions = 0, None
            while attempts < 3:
                item_questions = class_data_gen(
                    self.logger, item, practical=content_type == "practical"
                )
                if item_questions["class_questions"] is not None:
                    break
                else:
                    attempts += 1

            if item_questions:
                file_title = (
                    f"{self.module_data['module_name']} {content_type.capitalize()} Class "
                    + re.sub(".pdf", "", item)
                )
                generate_markdown(
                    self.logger,
                    self.output_path,
                    "class_template",
                    file_title,
                    item_questions,
                )

        for item in os.listdir(content_path):
            run_until_satisfied(self.logger, generate, item)

        self.logger.info(
            f"{content_type.capitalize()} class markdown files generated successfully."
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
        "C:/Users/wills/Documents/GitHub/module-generation/output/summaries/",
        "module_summary_questions",
        module_data["module_name"] + " Summary Questions",
        summaryquestions_data_gen(logger),
    )

    generate_markdown(
        logger,
        "C:/Users/wills/Documents/GitHub/module-generation/output/summaries/",
        "module_practice_tests",
        module_data["module_name"] + " Practice Tests",
        tests_data_gen(logger),
    )

    run_until_satisfied(
        logger,
        generate_markdown,
        logger,
        "C:/Users/wills/Documents/GitHub/module-generation/output/summaries/",
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
        "C:/Users/wills/Documents/GitHub/module-generation/output/revision/",
        "module_flashcards",
        module_data["module_name"] + " Flashcards",
        flashcards_data_gen(logger),
    )

    generate_markdown(
        logger,
        "C:/Users/wills/Documents/GitHub/module-generation/output/revision/",
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
    os.chdir(Path(__file__).parent.parent)  # Set the working directory

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

    # Generate notes markdown files
    notes(logger, module_data["module_notes_outline"])

    # Generate revision markdown files
    revision(logger, module_data)

    # End timer
    end_time = time()
    logger.info(f"Time taken: {end_time - start_time:.2f} seconds.")

    # Calculate success percentage in input
    with open("C:/Users/wills/Documents/GitHub/module-generation/log.txt", "r") as f:
        log = f.read()

    yes = log.count("yes")
    no = log.count("no")

    if yes + no != 0:
        logger.info(f"Success percentage: {yes / (yes + no) * 100:.2f}%")

    os.remove("C:/Users/wills/Documents/GitHub/module-generation/log.txt")

    # Calculate cost to run
    with open("C:/Users/wills/Documents/GitHub/module-generation/tokens.txt", "r") as f:
        tokens = f.read()

    lines = tokens.split("\n")

    cost = 0

    for line in lines:
        line = line.split(", ")
        cost += int(line[0]) * 0.0000005 + int(line[1]) * 0.0000015

    os.remove("C:/Users/wills/Documents/GitHub/module-generation/tokens.txt")

    logger.info(f"Cost to run: ${cost:.2f}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        get_logger().info("Program terminated by user.")
    except Exception as e:
        get_logger().exception(e)
        raise
