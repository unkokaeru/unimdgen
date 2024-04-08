"""Utility module."""

import os
import re
from winsound import Beep
from logging import Logger, basicConfig, getLogger
from pathlib import Path
from typing import Callable, Iterable, cast

import fitz
from jinja2 import Environment, FileSystemLoader
from openai import OpenAI

from config import LOGGING_CONFIG


def markdown_to_csv(logger: Logger, input: str, output_file: str, delimiter=";") -> str:
    """
    Converts a markdown file with questions and answers to a CSV file.
    :param logger: The logger object.
    :param input: The input markdown file.
    :param output_file: The output CSV file.
    :param delimiter: The delimiter to use in the CSV file.
    :return: The output CSV file name.
    """
    # Split content into blocks separated by "---"
    blocks = input.strip().split("\n---\n")

    # Extract questions and answers
    qa_pairs = []
    for block in blocks:
        question_match = re.search(r"### Question\n(.+)", block)
        answer_match = re.search(r"### Answer\n(.+)", block)
        if question_match and answer_match:
            qa_pairs.append((question_match.group(1), answer_match.group(1)))

    # Write to CSV
    with open(
        "C:/Users/wills/Documents/GitHub/module-generation/output/revision/"
        + output_file
        + ".csv",
        "w",
        encoding="utf-8",
    ) as file:
        for question, answer in qa_pairs:
            file.write(f"{question}{delimiter}{answer}\n")

    return output_file


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
        logger.info(f"Function ({func.__name__}) output: {result}")

        # Ask the user if they are satisfied with the output.
        user_input = (
            input("Are you satisfied with the output? (yes/no): ").strip().lower()
        )
        Beep(1000, 1000)  # Beep at 1000 Hz for 1000 ms

        # Log the user input in a text file.
        with open(
            "C:/Users/wills/Documents/GitHub/module-generation/log.txt", "a"
        ) as file:
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


def clean_latex(logger: Logger, text: str, strict: bool) -> str:
    """
    Cleans common GPT generation errors in LaTeX code.
    :param logger: The logger object.
    :param text: The text to clean.
    :param strict: Whether to use strict cleaning.
    :return: The cleaned text.
    """

    logger.debug("Starting to clean LaTeX code.")

    logger.debug(f"Starting text: {text}")

    if strict:
        # Remove patterns like "Problem 1 " and "1. "
        text = re.sub(r"Problem\s\d+\.\s", "", text)
        text = re.sub(r"\d+\.\s", "", text)

        logger.debug(f"Text after removing patterns: {text}")

    # Remove ```python and ```
    text = text.replace("```python", "").replace("```", "")

    logger.debug(f"Text after removing code blocks: {text}")

    if strict:
        # Remove unnecessary LaTeX markers
        # List of roman numerals as strings
        roman_numerals = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]

        # Looping through each numeral to replace the text
        for numeral in roman_numerals:
            # Building the pattern dynamically based on the numeral
            pattern = r"\\\\" + r"\(" + numeral + r"\)"
            replacement = f"({numeral})"
            text = re.sub(pattern, replacement, text)

    logger.debug(f"Text after removing unnecessary LaTeX markers: {text}")

    # Convert \( \) to $ $ and \[ \] to $$ $$
    text = text.replace(r"\(", "$").replace(r"\)", "$")
    text = text.replace(r"\[", "$$").replace(r"\]", "$$")

    logger.debug(f"Text after converting brackets: {text}")

    if strict:
        # Escape unescaped tabs in matrices
        text = text.replace(r"\s\\\\\s", r"\s\\\\\\\\\s")

        logger.debug(f"Text after escaping tabs in matrices: {text}")

    # Remove whitespace around $...
    # text = re.sub(r"\$\s+([^$]+)\s+\$", r"$\1$", text)
    # This pattern looks for math expressions and removes internal spaces, preserving the readability
    def adjust_math_whitespace(match):
        math_content = match.group(0)
        # Remove only internal spaces that don't affect readability
        cleaned_math = re.sub(r"\s+(?=[^\s\w]|$)", "", math_content)
        return cleaned_math

    text = re.sub(r"\$(\$?[^$]+\$?)\$", adjust_math_whitespace, text)

    logger.debug(f"Text after removing whitespace around $: {text}")

    if strict:
        # Remove escaped dollar signs
        text = text.replace(r"\\\$", r"\$")

        logger.debug(f"Text after removing escaped dollar signs: {text}")

        # Escape characters
        def ensure_correct_latex_backslashes(latex_str):
            # Pattern to find single backslashes followed by common LaTeX command starts
            # Adjust this list based on the commands you use
            common_latex_commands = [
                "begin",
                "end",
                "frac",
                "textit",
                "textbf",
                "left",
                "right",
                "mathbb",
                "mathbf",
                "mathscr",
            ]
            pattern = re.compile(r"(?<!\\)\\(" + "|".join(common_latex_commands) + r")")

            def replacement(match):
                # Since the match includes a single backslash, we add another to correctly escape it
                return "\\\\" + match.group(1)

            # Correctly escape single backslashes before LaTeX commands
            corrected_str = pattern.sub(replacement, latex_str)

            return corrected_str

        text = ensure_correct_latex_backslashes(text)

        logger.debug(f"Text after escaping characters: {text}")

    # Subscript when there is a number after a letter, without a space
    text = re.sub(r"([a-zA-Z])(\d)", r"\1_{\2}", text)

    logger.debug(f"Text after subscripting numbers after letters: {text}")

    if strict:
        # Remove escaped dollar signs
        text = text.replace(r"\\\$", r"\$")

        logger.debug(f"Text after removing escaped dollar signs (again): {text}")

        # Remove additional edge cases TODO
        # \\text -> \text
        # text = text.replace(r"\\\\text", "\\text")
        # \- -> \\
        # text = text.replace(r"\\\-", "\\\\")
        # \ -> \\
        # text = text.replace(r"\\\s", "\\\\")
        # \\end -> \end
        # text = text.replace(r"\\\\end", "\\end")

    return text


def generate_markdown(
    logger: Logger,
    sav_loc: str,
    template_title: str,
    doc_title: str,
    data: dict[str, str],
) -> None:
    """
    Generates markdown files.
    :param logger: The logger object.
    :param sav_loc: The location to save the markdown files.
    :param template_title: The title of the markdown template.
    :param doc_title: The title of the saved markdown document.
    :param data: The data to render in the markdown file.
    :return: None
    """

    logger.debug(f"Generating markdown file ({str}.md)...")

    # Set the working directory to the script's parent directory
    os.chdir(Path(__file__).resolve().parent.parent)
    logger.debug(f"Changed working directory to {os.getcwd()}")

    # Initialize Jinja2 environment and load template
    env = Environment(
        loader=FileSystemLoader(
            "C:/Users/wills/Documents/GitHub/module-generation/templates"
        )
    )
    template = env.get_template(f"{template_title}.md")
    logger.debug("Template loaded successfully.")

    # Render the template with the data
    rendered_content = template.render(data)
    logger.debug("Document rendered successfully.")

    # Build the file path
    file_path = Path(sav_loc) / f"{doc_title}.md"

    # Create any missing directories
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Write the rendered content to the file
    with open(
        file_path,
        "w",
        encoding="utf-8",
    ) as file:
        file.write(rendered_content)
    logger.debug(f"Markdown file ({doc_title}.md) generated successfully.")


def get_logger() -> Logger:
    """
    Get the logger for the application.

    :return: The logger for the application.
    """

    # Get logging configuration
    level = cast(str, LOGGING_CONFIG["level"])
    format = cast(str, LOGGING_CONFIG["format"])
    datefmt = cast(str, LOGGING_CONFIG["datefmt"])
    handlers = cast(Iterable, LOGGING_CONFIG["handlers"])

    # Set up logging
    basicConfig(
        level=level,
        format=format,
        datefmt=datefmt,
        handlers=handlers,
    )
    logger = getLogger("rich")

    return logger


def pdf_to_text(
    logger: Logger,
    pdf_path: str,
) -> str:
    """
    A function to convert a PDF file to text.
    :param logger: The logger object.
    :param pdf_path: The path to the PDF file.
    :return: The text from the PDF file.
    """

    logger.debug("Starting to convert the PDF to text.")

    try:
        text = ""
        with fitz.open(pdf_path) as doc:
            logger.debug(f"Reading the PDF file at: '{pdf_path}'.")
            for page in doc:
                text += page.get_text()
            logger.debug("PDF file read.")

        logger.debug("PDF converted to text.")
        return text
    except Exception as e:
        logger.error(f"Error: {e}")
        return ""


def prompt_gpt(
    logger: Logger,
    user_message: str,
    system_message: str = "You are a helpful assistant.",
    api_key: str = os.getenv("OPENAI_API_KEY"),
) -> str:
    """
    A function to prompt the ChatGPT API to generate a response to a user message.
    :param logger: The logger object.
    :param api_key: The API key for the OpenAI API.
    :param user_message: The user's message to respond to.
    :param system_message: The system's message to respond to.
    :return: The response from the ChatGPT API.
    """

    logger.debug("Starting to prompt the ChatGPT API.")

    try:
        client = OpenAI(api_key=api_key)
        logger.debug("Client initialized.")

        logger.debug(f"Prompting the ChatGPT API with: '{user_message}'.")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
            ],
        )
        logger.debug("Response received.")

        # Log tokens used in a text file
        with open(
            "C:/Users/wills/Documents/GitHub/module-generation/tokens.txt", "a"
        ) as file:
            file.write(
                f"{response.usage.prompt_tokens}, {response.usage.completion_tokens}\n"
            )

        return cast(str, response.choices[0].message.content)
    except Exception as e:
        logger.error(f"Error: {e}")
        return "..."
