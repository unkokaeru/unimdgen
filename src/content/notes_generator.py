"""notes_generator.py: A module for generating the note markdown files."""

import re
from logging import Logger

from cli.self_validation import run_until_satisfied
from config.paths import NOTES_PATH
from src.processing.gpt_interaction import prompt_gpt
from src.utilities.file_utilities import generate_markdown
from src.utilities.text_utilities import clean_latex


def notes(logger: Logger, notes_outline: str) -> None:
    """
    Generate note markdown files.
    :param logger: Logger object
    :param notes_outline: Notes outline
    :return: None
    """

    # Find every [[markdown link]]
    markdown_links = re.findall(r"\[\[(.*?)\]\]", notes_outline)

    logger.info(f"Markdown links: {markdown_links}")

    # Generate a note for each markdown link
    note_prompt = "You're a program that takes a topic and generates a detailed markdown note aimed at undergraduate mathematicians, including all the information that would be required to understand the topic. This should include definitions, explanations, examples, and any other relevant information - seamlessly intertwine historical context and real-life examples. Finish with three exam questions to test the reader. Return the generated note in markdown format, using LaTeX when appropriate."

    def gen_note(link: str) -> str:
        content = clean_latex(
            logger, prompt_gpt(logger, link, note_prompt), False
        )  # TODO: Include link description in prompt

        generate_markdown(
            logger,
            NOTES_PATH,
            "note_template",
            link,
            {"note_content": content},
        )

        return link

    for link in markdown_links:
        run_until_satisfied(logger, gen_note, link)
