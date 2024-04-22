import os
from logging import Logger
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from src.config.paths import TEMPLATES_PATH


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
