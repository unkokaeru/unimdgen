"""data_parsing.py: A module for parsing data."""

import os
from logging import Logger

from src.config.constants import INPUT_COST, OUTPUT_COST
from src.config.paths import LOG_PATH, TOKENS_PATH
from src.utilities.conversion_utilities import currency_converter


def calculate_stats(logger: Logger, time_taken: float) -> None:
    """
    Calculate and log statistics about the program's execution.
    :param logger: The logger object.
    :param time_taken: The time taken for the program to execute.
    :return: None
    """
    
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
