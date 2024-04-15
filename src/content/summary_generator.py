"""summary_generator.py: A module for generating the summary markdown files."""

import os
import re
from logging import Logger

from cli.self_validation import run_until_satisfied
from config.paths import CLASSES_PATH, PAPERS_PATH, SUMMARY_PATH
from src.processing.gpt_interaction import prompt_gpt
from src.utilities.file_utilities import generate_markdown


def summaryquestions_data_gen(logger: Logger) -> dict[str, str]:
    """
    Generate data for the summary questions markdown files.
    :param logger: Logger object
    :return: class hyperlinks, summary questions
    """

    data = {
        "class_hyperlink_list": None,
        "summary_questions": None,
    }

    # Initialise the required variables
    data["class_hyperlink_list"] = ""
    summary_questions: list[str] = []

    # Loop through the classes folder
    for file in os.listdir(CLASSES_PATH):
        # Generate the class hyperlinks
        data["class_hyperlink_list"] += f"- [[{re.sub('.md', '', file)}]]\n"

        # Generate the summary questions
        with open(f"{CLASSES_PATH}{file}", "r", encoding="utf-8") as f:
            content = f.read()
            questions = re.findall(
                r"#### Question\n\n(.*?)\n\n#### Solution", content, re.DOTALL
            )
            summary_questions.extend(questions)

    data["summary_questions"] = "\n\n".join(
        [f"{i}. {question}" for i, question in enumerate(summary_questions, start=1)]
    )

    return data


def tests_data_gen(logger: Logger) -> dict[str, str]:
    """
    Generate data for the practice tests markdown files.
    :param logger: Logger object
    :return: practice tests hyperlinks
    """

    data = {
        "practice_test_hyperlink_list": None,
    }

    data["practice_test_hyperlink_list"] = ""

    if os.listdir(PAPERS_PATH) == []:
        logger.error("No papers found.")
        return data

    for file in os.listdir(PAPERS_PATH):
        data["practice_test_hyperlink_list"] += f"- [[{re.sub('.pdf', '', file)}]]\n"

    # TODO: Generate predicted papers (that look the exact same) that will also be appended to this list.

    return data


def summarynotes_data_gen(logger: Logger) -> dict[str, str]:
    """
    Generate data for the summary notes markdown files.
    :param logger: Logger object
    :return: summary notes
    """

    data = {
        "summary_notes": None,
    }

    # Find the summary questions markdown file (ends in "Summary Questions.md")
    file_path = None
    for file in os.listdir(SUMMARY_PATH):
        if file.endswith("Summary Questions.md"):
            file_path = f"{SUMMARY_PATH}{file}"
            break

    # Read the summary questions markdown file
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Generate notes that explain how to solve every type of question in the summary questions
    gpt_response = prompt_gpt(
        logger,
        content,
        "You're a program that takes a list of questions and generates a detailed explanation of how to solve each type of question, including the steps, methods, and reasoning behind each step. Use a logical order and bullet points to quickly convey the information. Return the generated notes in markdown format, using LaTeX when appropriate (as in the questions given). Only return the bullet points and nothing else. If you cannot find any questions, return None.",
    )

    # Clean the GPT response
    gpt_response = re.sub(r"```markdown\n", "", gpt_response)
    gpt_response = re.sub(r"```", "", gpt_response)

    # Return the data dictionary
    if gpt_response:
        data["summary_notes"] = gpt_response

    return data


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
