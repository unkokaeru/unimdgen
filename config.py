"""Configuration file"""

from rich.logging import RichHandler

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(message)s",
    "datefmt": "[%X]",
    "handlers": [RichHandler(rich_tracebacks=True)],
}

# Path Configuration
SCRIPT_PATH = "C:/Users/wills/Documents/GitHub/module-generation/"

INPUT_PATH = f"{SCRIPT_PATH}input/"
OUTPUT_PATH = f"{SCRIPT_PATH}output/"
TEMPLATES_PATH = f"{SCRIPT_PATH}templates/"
LOG_PATH = f"{SCRIPT_PATH}log.txt"
TOKEN_PATH = f"{SCRIPT_PATH}tokens.txt"
HANDBOOK_PATH = f"{INPUT_PATH}handbook/"
PAPERS_PATH = f"{INPUT_PATH}papers/"
CLASSES_PATH = f"{OUTPUT_PATH}classes/"
NOTES_PATH = f"{OUTPUT_PATH}notes/"
REVISION_PATH = f"{OUTPUT_PATH}revision/"
SUMMARY_PATH = f"{OUTPUT_PATH}summaries/"

# Token Cost Configuration
INPUT_COST = 0.0000005  # $ per token
OUTPUT_COST = 0.0000015  # $ per token
