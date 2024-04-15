"""log_manager.py: A module for managing the application's logging."""

from logging import Logger, basicConfig, getLogger, Filter
from typing import Iterable, cast

from config.logging import LOGGING_CONFIG


class NoPostFilter(Filter):
    def filter(self, record):
        # Exclude POST requests logs from 'http.client'
        return "POST" not in record.getMessage()


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

    # Get the http.client logger and add the NoPostFilter to it
    http_client_logger = getLogger("http.client")
    http_client_logger.addFilter(NoPostFilter())

    return logger
