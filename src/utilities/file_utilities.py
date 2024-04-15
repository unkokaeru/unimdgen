import os
from logging import Logger
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from config.paths import TEMPLATES_PATH
from src.processing.gpt_interaction import prompt_gpt


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
    env = Environment(loader=FileSystemLoader(TEMPLATES_PATH))
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


def fetch_from_markdown(
    logger: Logger, file_path: str, data: dict[str, str]
) -> dict[str, str]:
    """
    Fetches data from a markdown file.
    :param logger: The logger object.
    :param file_path: The path to the markdown file.
    :param data: The data to fetch from the markdown file.
    :return: The fetched data.
    """

    logger.debug(f"Fetching data from markdown file ({file_path})...")

    # Read the markdown file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    logger.debug("Markdown file read successfully.")

    # Fetch the data from the markdown file
    for key in data:
        if data[key] is None:
            prompt_gpt(
                logger,
                content,
                f"You are a program to fetch {key}. Provide only the data for {key} and nothing else.",
            )
    logger.debug("Data fetched successfully.")

    return data
