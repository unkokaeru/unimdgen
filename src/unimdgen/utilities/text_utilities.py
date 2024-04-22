"""text_utilities.py: A collection of utility functions for text processing."""

import re
from logging import Logger


def clean_latex(logger: Logger, text: str, strict: bool) -> str:
    """
    Cleans common GPT generation errors in LaTeX code.
    :param logger: The logger object.
    :param text: The text to clean.
    :param strict: Whether to use strict cleaning.
    :return: The cleaned text.
    """

    logger.debug("Starting to clean LaTeX code.")

    logger.debug(f"Starting text: {text}")

    if strict:
        # Remove patterns like "Problem 1 " and "1. "
        text = re.sub(r"Problem\s\d+\.\s", "", text)
        text = re.sub(r"\d+\.\s", "", text)

        logger.debug(f"Text after removing patterns: {text}")

    # Remove ```python and ```
    text = text.replace("```python", "").replace("```", "")

    logger.debug(f"Text after removing code blocks: {text}")

    if strict:
        # Remove unnecessary LaTeX markers
        # List of roman numerals as strings
        roman_numerals = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]

        # Looping through each numeral to replace the text
        for numeral in roman_numerals:
            # Building the pattern dynamically based on the numeral
            pattern = r"\\\\" + r"\(" + numeral + r"\)"
            replacement = f"({numeral})"
            text = re.sub(pattern, replacement, text)

    logger.debug(f"Text after removing unnecessary LaTeX markers: {text}")

    # Convert \( \) to $ $ and \[ \] to $$ $$
    text = text.replace(r"\(", "$").replace(r"\)", "$")
    text = text.replace(r"\[", "$$").replace(r"\]", "$$")

    logger.debug(f"Text after converting brackets: {text}")

    if strict:
        # Escape unescaped tabs in matrices
        text = text.replace(r"\s\\\\\s", r"\s\\\\\\\\\s")

        logger.debug(f"Text after escaping tabs in matrices: {text}")

    # Remove whitespace around $...
    # text = re.sub(r"\$\s+([^$]+)\s+\$", r"$\1$", text)
    # This pattern looks for math expressions and removes internal spaces, preserving the readability
    def adjust_math_whitespace(match):
        math_content = match.group(0)
        # Remove only internal spaces that don't affect readability
        cleaned_math = re.sub(r"\s+(?=[^\s\w]|$)", "", math_content)
        return cleaned_math

    text = re.sub(r"\$(\$?[^$]+\$?)\$", adjust_math_whitespace, text)

    logger.debug(f"Text after removing whitespace around $: {text}")

    if strict:
        # Remove escaped dollar signs
        text = text.replace(r"\\\$", r"\$")

        logger.debug(f"Text after removing escaped dollar signs: {text}")

        # Escape characters
        def ensure_correct_latex_backslashes(latex_str):
            # Pattern to find single backslashes followed by common LaTeX command starts
            # Adjust this list based on the commands you use
            common_latex_commands = [
                "begin",
                "end",
                "frac",
                "textit",
                "textbf",
                "left",
                "right",
                "mathbb",
                "mathbf",
                "mathscr",
            ]
            pattern = re.compile(r"(?<!\\)\\(" + "|".join(common_latex_commands) + r")")

            def replacement(match):
                # Since the match includes a single backslash, we add another to correctly escape it
                return "\\\\" + match.group(1)

            # Correctly escape single backslashes before LaTeX commands
            corrected_str = pattern.sub(replacement, latex_str)

            return corrected_str

        text = ensure_correct_latex_backslashes(text)

        logger.debug(f"Text after escaping characters: {text}")

    # Subscript when there is a number after a letter, without a space
    text = re.sub(r"([a-zA-Z])(\d)", r"\1_{\2}", text)

    logger.debug(f"Text after subscripting numbers after letters: {text}")

    if strict:
        # Remove escaped dollar signs
        text = text.replace(r"\\\$", r"\$")

        logger.debug(f"Text after removing escaped dollar signs (again): {text}")

        # Remove additional edge cases TODO
        # \\text -> \text
        # text = text.replace(r"\\\\text", "\\text")
        # \- -> \\
        # text = text.replace(r"\\\-", "\\\\")
        # \ -> \\
        # text = text.replace(r"\\\s", "\\\\")
        # \\end -> \end
        # text = text.replace(r"\\\\end", "\\end")

    return text
