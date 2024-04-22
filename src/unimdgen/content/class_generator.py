"""class_generator.py: A module for generating the class markdown files."""

import ast
import os
import re
from logging import Logger

from unimdgen.cli.self_validation import run_until_satisfied
from unimdgen.config.paths import CLASSES_PATH, INPUT_PATH, PAPERS_PATH
from unimdgen.config.prompts import CLASS_PROMPT, MISTAKE_PROMPT
from unimdgen.processing.gpt_interaction import prompt_gpt
from unimdgen.utilities.conversion_utilities import pdf_to_text
from unimdgen.utilities.file_utilities import generate_markdown
from unimdgen.utilities.text_utilities import clean_latex


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


def class_data_gen(logger: Logger, class_name: str, content_type: str) -> dict[str, str]:
    """
    Generate data for the tutorial and practical class markdown files.
    :param logger: Logger object
    :param class_name: Name of the practical/tutorial class
    :param content_type: Type of content (tutorial, practical, or paper)
    :return: class questions
    """

    data = {
        "class_questions": None,
    }

    # Suppress SyntaxWarning - ast.literal_eval() raises this warning, benign in this case
    # filterwarnings("ignore", category=SyntaxWarning)

    # Find the class PDF
    file_path = f"{INPUT_PATH}{content_type}s/{class_name}"

    # Convert the PDF to text
    pdf_text = pdf_to_text(logger, file_path)

    # Prompt the ChatGPT API to convert the PDF text into a list of questions
    gen_prompt = CLASS_PROMPT
    gpt_response = prompt_gpt(logger, pdf_text, gen_prompt)

    #logger.info(f"GPT response BEFORE: {gpt_response}")

    # Prompt the ChatGPT API to fix its own mistakes
    mistake_prompt = MISTAKE_PROMPT
    gpt_response = prompt_gpt(logger, gpt_response, mistake_prompt)

    #logger.info(f"GPT response MIDWAY: {gpt_response}")

    # Clean the GPT response
    gpt_response = clean_latex(logger, gpt_response, True)

    # Parse the GPT response
    try:
        gpt_response_list = ast.literal_eval(gpt_response)
    except ValueError as e:
        logger.error(f"Error parsing GPT response: {e}")
        gpt_response_list = []
    except SyntaxError as e:
        logger.warning(f"Error parsing GPT response: {e}")
        gpt_response_list = []

    # Combine sub-questions with their main questions, e.g. if an item in a list begins with "(" then combine it with the previous item
    if gpt_response_list:
        i = 1
        while i < len(gpt_response_list):
            if gpt_response_list[i].startswith("("):
                gpt_response_list[i-1] += "\n" + gpt_response_list[i]
                gpt_response_list.pop(i)
            else:
                i += 1

    logger.debug(f"GPT response: {gpt_response_list}")

    # Format the questions
    class_questions = None if not gpt_response_list else "\n\n".join([f"### Question {i+1}\n\n#### Question\n\n{question}\n\n#### Solution\n\n..." for i, question in enumerate(gpt_response_list)])

    # Return the data dictionary
    if gpt_response:
        data["class_questions"] = class_questions

    return data
