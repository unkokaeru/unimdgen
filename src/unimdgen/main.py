"""main.py: The main script for generating the module content documents."""

import os
from pathlib import Path
from time import time

from unimdgen.cli.cli import interface
from unimdgen.utilities.log_manager import get_logger
from unimdgen.processing.data_parsing import calculate_stats

"""
Things to implement:
- Use lecture slides to supplement the notes, including links to the slides
    (by reading each lecture slides,
    tagging them with their content,
    then organising into the main contents).
- Question-based revision note generation (cheat sheet).
- Create predicted papers.
- Anki flashcard generation.
- Include link description in prompt for note generation.

Things to fix:
- Update documentation.
- Update comments, TODOs etc. throughout the code.
- Further GPT data generation cleaning, incl. UK spelling.
    (to increase success percentage, hence decrease generation time).
"""


def main() -> None:
    """
    The main function.
    :return: None
    """

    # Initalise the script
    logger = get_logger()
    os.chdir(Path(__file__).parent.parent)
    start_time = time()

    # Run the main interface
    interface(logger)

    # Calculate the statistics of the document generation
    calculate_stats(logger, time() - start_time)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        get_logger().info("Program terminated by user.")
    except Exception as e:
        get_logger().exception(e)
        raise
