"""conversion_utilities.py: A module for conversion utilities."""

import os
import re
from logging import Logger

import fitz
import requests

from config.api import EXCHANGE_API_KEY
from config.paths import REVISION_PATH


def currency_converter(
    logger: Logger, amount: float, from_currency: str, to_currency: str
) -> float:
    """
    Converts an amount from one currency to another.
    :param logger: The logger object.
    :param amount: The amount to convert.
    :param from_currency: The currency to convert from.
    :param to_currency: The currency to convert to.
    :return: The converted amount.
    """

    url = (
        f"https://api.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/{from_currency}"
    )

    response = requests.get(url)
    data = response.json()
    exchange_rate = data["conversion_rates"][to_currency]

    converted_amount = amount * exchange_rate

    return converted_amount


def name_to_email(logger: Logger, name: str, email_domain: str) -> str:
    """
    Converts a name to an email address.
    :param logger: The logger object.
    :param name: The name to convert.
    :param email_domain: The email domain to use.
    :return: The email address.
    """

    parts = name.split()

    if len(parts) == 2:
        first_name, last_name = parts
        # Construct the email
        email = f"{first_name[0]}{last_name}@{email_domain}".lower()
    else:
        raise ValueError("Name must be in the format 'First Last'")

    return email


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
    csv_path = REVISION_PATH + output_file + ".csv"
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    with open(
        csv_path,
        "w",
        encoding="utf-8",
    ) as file:
        for question, answer in qa_pairs:
            file.write(f"{question}{delimiter}{answer}\n")

    return output_file


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
