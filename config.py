"""Configuration file"""

from rich.logging import RichHandler

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(message)s",
    "datefmt": "[%X]",
    "handlers": [RichHandler(rich_tracebacks=True)],
}

# Token Cost Configuration
INPUT_COST = 0.0000005  # $ per token
OUTPUT_COST = 0.0000015  # $ per token

# API Configuration (free API, so no need to change this)
EXCHANGE_API_KEY = "d22354212680daf1d45a64d1"

# Domain Configuration
UNI_DOMAIN = "lincoln.ac.uk"

# Path Configuration
SCRIPT_PATH = "C:/Users/wills/Documents/GitHub/module-generation/"
MODULE_FOLDER = input(
    "Enter the module folder name (e.g. MTH1005 Probability and Statistics): "
)  # Bad practice but easier for now

INPUT_PATH = f"{SCRIPT_PATH}input/{MODULE_FOLDER}/"
OUTPUT_PATH = f"{SCRIPT_PATH}output/{MODULE_FOLDER}/"
TEMPLATES_PATH = f"{SCRIPT_PATH}templates/"
LOG_PATH = f"{SCRIPT_PATH}log.txt"
TOKENS_PATH = f"{SCRIPT_PATH}tokens.txt"
HANDBOOK_PATH = f"{INPUT_PATH}handbook/"
PAPERS_PATH = f"{INPUT_PATH}papers/"
CLASSES_PATH = f"{OUTPUT_PATH}classes/"
NOTES_PATH = f"{OUTPUT_PATH}notes/"
REVISION_PATH = f"{OUTPUT_PATH}revision/"
SUMMARY_PATH = f"{OUTPUT_PATH}summaries/"
