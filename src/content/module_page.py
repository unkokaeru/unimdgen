"""module_page.py: A module for generating the main module markdown file."""

import ast
import os
import re
from logging import Logger
from typing import cast

from src.config.constants import MODULE_FOLDER, UNI_DOMAIN
from src.config.paths import HANDBOOK_PATH, OUTPUT_PATH
from src.config.prompts import NOTES_OUTLINE_PROMPT
from src.processing.gpt_interaction import prompt_gpt
from src.utilities.conversion_utilities import name_to_email, pdf_to_text
from src.utilities.file_utilities import generate_markdown


def module_data_gen(logger: Logger) -> dict[str, str]:
    """
    Generate data for the main module markdown file.
    :param logger: Logger object
    :return: module name, professor name, professor email, weights, LOs, notes outline
    """

    data = {
        "module_name": None,
        "name": None,
        "email": None,
        "assessment_weighting_percentages": None,
        "learning_outcomes": None,
        "module_notes_outline": None,
    }

    # Check the existence of the handbook
    if os.listdir(f"{HANDBOOK_PATH}") == []:
        logger.error("No handbook found.")
        return data

    # Convert the PDF to text
    pdf_text = pdf_to_text(logger, f"{HANDBOOK_PATH}/{os.listdir(f"{HANDBOOK_PATH}")[0]}")
    logger.debug("PDF text: %s", pdf_text[:100] + "...")

    # Prompt the ChatGPT API to find relevant information NOTE: Add manual mode? (if GPT fails)
    gpt_response = prompt_gpt(logger, pdf_text, "You're a program that returns a Python List (and nothing else) of the following (found in the given PDF text): module name, professor name, professor email, assessment weighting percentages List (labelled as [Title (x%)], where Title is in the title of the assessment), learning outcomes List, and module content outline List. If you cannot find any of these, return None in the List.")
    gpt_response_list = cast(list[str], gpt_response)

    # Parse the GPT response
    try:
        gpt_response_list = ast.literal_eval(gpt_response)
    except ValueError as e:
        logger.error(f"Error parsing GPT response: {e}")
        gpt_response_list = []
    except SyntaxError as e:
        logger.warning(f"Error parsing GPT response: {e}")
        gpt_response_list = ast.literal_eval(gpt_response + "]")

    logger.debug(f"GPT response: {gpt_response_list}")

    # Extract and format the relevant information from the GPT response
    module_name = gpt_response_list[0]
    name = gpt_response_list[1]
    email = name_to_email(logger, name, UNI_DOMAIN) if gpt_response_list[2] == "None" else gpt_response_list[2]
    assessment_weighting_percentages = gpt_response_list[3] if isinstance(gpt_response_list[3], str) else "- [ ] " + "\n- [ ] ".join([i for i in gpt_response_list[3]])
    learning_outcomes = gpt_response_list[4] if isinstance(gpt_response_list[4], str) else "- [ ] " + "\n- [ ] ".join([re.sub(r'LO[1-9]', r'**\g<0>**', i) for i in gpt_response_list[4]])
    module_notes_outline = gpt_response_list[5] if isinstance(gpt_response_list[5], str) else "- " + "\n- ".join([i for i in gpt_response_list[5]])

    # Clean the assessment weighting percentages
    if assessment_weighting_percentages:
        prompt_gpt(logger, assessment_weighting_percentages, "You're a program that takes a Python List of assessment weighting percentages and ensures that they make sense, are in the correct format, and are properly labelled. If they are not, then fix them. Return the fixed List.")

    # Expand and detail the notes outline
    notes_outline_prompt = NOTES_OUTLINE_PROMPT if module_name else None
    module_notes_outline = prompt_gpt(logger, module_notes_outline, notes_outline_prompt) if module_notes_outline else None

    # Clean the notes outline
    if module_notes_outline:
        module_notes_outline = re.sub(r"^(?=\d+\.)", "### ", module_notes_outline, flags=re.MULTILINE)

    # Return the data dictionary
    if gpt_response:
        data["module_name"] = MODULE_FOLDER if None else module_name
        data["name"] = name
        data["email"] = email
        data["assessment_weighting_percentages"] = assessment_weighting_percentages
        data["learning_outcomes"] = learning_outcomes
        data["module_notes_outline"] = module_notes_outline

    logger.debug(f"Final data dictionary: {data}")

    return data


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
