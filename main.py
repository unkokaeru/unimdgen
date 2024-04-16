"""main.py: The main script for generating the module content documents."""

import os
from pathlib import Path
from time import time

from cli.cli import interface
from logs.log_manager import get_logger
from src.processing.data_parsing import calculate_stats

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
- Documentation (update).
- Further GPT data generation cleaning.
- Flashcard tweaking & user checking.
- Change Anki flashcard generation.
- Refine summary notes prompt.
- UK spelling.
- Prompts into a new config.prompts file.
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
