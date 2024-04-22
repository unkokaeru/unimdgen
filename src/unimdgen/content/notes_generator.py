"""notes_generator.py: A module for generating the note markdown files."""

import re
from logging import Logger

from unimdgen.cli.self_validation import run_until_satisfied
from unimdgen.config.constants import MODULE_FOLDER
from unimdgen.config.paths import NOTES_PATH, OUTPUT_PATH
from unimdgen.config.prompts import NOTE_PROMPT
from unimdgen.processing.gpt_interaction import prompt_gpt
from unimdgen.utilities.file_utilities import generate_markdown
from unimdgen.utilities.text_utilities import clean_latex


def fetch_notes_outline(logger: Logger) -> str:
    """
    Fetch the notes outline.
    :param logger: Logger object
    :return: Notes outline
    """

    with open(f"{OUTPUT_PATH}{MODULE_FOLDER}.md", "r") as file:
        content = file.read()

    notes_outline = content.split("## Notes")[1]

    logger.debug(f"Fetched notes outline: {notes_outline}")

    return notes_outline


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
    note_prompt = NOTE_PROMPT

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
