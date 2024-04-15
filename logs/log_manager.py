"""log_manager.py: A module for managing the application's logging."""

from logging import Logger, basicConfig, getLogger, WARNING
from typing import Iterable, cast

from config.logging import LOGGING_CONFIG


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

    # Make logging rich
    logger = getLogger("rich")

    # Set the HTTP client logging level to WARNING, to reduce verbosity
    getLogger("http.client").setLevel(WARNING)

    return logger
