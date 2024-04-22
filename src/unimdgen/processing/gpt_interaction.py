"""gpt_interaction.py: A module for interacting with the ChatGPT API."""

import os
from logging import Logger
from typing import cast

from openai import OpenAI

from unimdgen.config.paths import TOKENS_PATH


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
        with open(TOKENS_PATH, "a") as file:
            file.write(
                f"{response.usage.prompt_tokens}, {response.usage.completion_tokens}\n"
            )

        return cast(str, response.choices[0].message.content)
    except Exception as e:
        logger.error(f"Error: {e}")
        return "..."
