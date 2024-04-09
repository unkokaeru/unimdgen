"""Data generation module for the markdown generation."""

import ast
import os
import re
from logging import Logger
from typing import cast

from config import (
    CLASSES_PATH,
    HANDBOOK_PATH,
    INPUT_PATH,
    NOTES_PATH,
    PAPERS_PATH,
    REVISION_PATH,
    SUMMARY_PATH,
    UNI_DOMAIN,
)

#from warnings import filterwarnings
from utils import (
    clean_latex,
    generate_markdown,
    markdown_to_csv,
    name_to_email,
    pdf_to_text,
    prompt_gpt,
    run_until_satisfied,
)


def module_data_gen(logger: Logger) -> dict[str, str]:
    """
    Generate data for the main module markdown file.
    :param logger: Logger object
    :return: module name, professor name, professor email, weights, LOs, notes outline
    """

    data = {
        "module_name": None,
        "name": None,
        "email": None,
        "assessment_weighting_percentages": None,
        "learning_outcomes": None,
        "module_notes_outline": None,
    }

    # Check the existence of the handbook
    if os.listdir(f"{HANDBOOK_PATH}") == []:
        logger.error("No handbook found.")
        return data

    # Convert the PDF to text
    pdf_text = pdf_to_text(logger, f"{HANDBOOK_PATH}/{os.listdir(f"{HANDBOOK_PATH}")[0]}")
    logger.debug("PDF text: %s", pdf_text[:100] + "...")

    # Prompt the ChatGPT API to find relevant information NOTE: Add manual mode? (if GPT fails)
    gpt_response = prompt_gpt(logger, pdf_text, "You're a program that returns a Python List (and nothing else) of the following (found in the given PDF text): module name, professor name, professor email, assessment weighting percentages List (labelled as [Title (x%)], where Title is in the title of the assessment), learning outcomes List, and module content outline List. If you cannot find any of these, return None in the List.")
    gpt_response_list = cast(list[str], gpt_response)

    # Parse the GPT response
    try:
        gpt_response_list = ast.literal_eval(gpt_response)
    except ValueError as e:
        logger.error(f"Error parsing GPT response: {e}")
        gpt_response_list = []
    except SyntaxError as e:
        logger.warning(f"Error parsing GPT response: {e}")
        gpt_response_list = ast.literal_eval(gpt_response + "]")

    logger.debug(f"GPT response: {gpt_response_list}")

    # Extract and format the relevant information from the GPT response
    module_name = gpt_response_list[0]
    name = gpt_response_list[1]
    email = name_to_email(logger, name, UNI_DOMAIN) if gpt_response_list[2] == "None" else gpt_response_list[2]
    assessment_weighting_percentages = gpt_response_list[3] if isinstance(gpt_response_list[3], str) else "- [ ] " + "\n- [ ] ".join([i for i in gpt_response_list[3]])
    learning_outcomes = gpt_response_list[4] if isinstance(gpt_response_list[4], str) else "- [ ] " + "\n- [ ] ".join([re.sub(r'LO[1-9]', r'**\g<0>**', i) for i in gpt_response_list[4]])
    module_notes_outline = gpt_response_list[5] if isinstance(gpt_response_list[5], str) else "- " + "\n- ".join([i for i in gpt_response_list[5]])

    # Clean the assessment weighting percentages
    if assessment_weighting_percentages:
        prompt_gpt(logger, assessment_weighting_percentages, "You're a program that takes a Python List of assessment weighting percentages and ensures that they make sense, are in the correct format, and are properly labelled. If they are not, then fix them. Return the fixed List.")

    # Expand and detail the notes outline
    notes_outline_prompt = """
You're a program that takes an outline of lecture content and converts it into a detailed markdown outline of notes with topics, sub-topics, and descriptions of each sub-topic; such as:
1. Functions

#### 1.1 Basic Concepts

- **[[Domain and Range]]**: Understanding the set of inputs (domain) and outputs (range) for functions.
- **[[Graphs of Functions]]**: Visual representation of functions on a coordinate plane.
- **[[Vertical Line Test]]**: A method to determine if a graph represents a function.

#### 1.2 Types of Functions

- **[[Polynomial Functions]]**: Functions like $y = x^n$.
- **[[Rational Functions]]**: Functions expressed as the ratio of two polynomials.
- **[[Trigonometric Functions]]**: Functions based on angles and ratios in a right triangle.
- **[[Exponential Functions]]**: Functions where the variable appears in the exponent.
- **[[Hyperbolic Functions]]**: Functions similar to trigonometric functions but based on hyperbolas.
- **[[Even and Odd Functions]]**: Symmetry properties of functions.
- **[[Piecewise-defined Functions]]**: Functions defined by different expressions over different intervals (e.g., absolute value, signum function).
- **[[Multivariable Functions]]**: Functions with multiple variable inputs.

etc.

The generated outline should be a logical order, ignoring the original order if required.
The topics should cover everything in the original outline (apart from things like revision and overviews), but the sub-topics and descriptions should be purely generated by you as they won't be provided, usually.
Ensure that the final result is in the exact same format as above.
""" if module_name else None
    module_notes_outline = prompt_gpt(logger, module_notes_outline, notes_outline_prompt) if module_notes_outline else None

    # Clean the notes outline
    if module_notes_outline:
        module_notes_outline = re.sub(r"^(?=\d+\.)", "### ", module_notes_outline, flags=re.MULTILINE)

    # Return the data dictionary
    if gpt_response:
        data["module_name"] = module_name
        data["name"] = name
        data["email"] = email
        data["assessment_weighting_percentages"] = assessment_weighting_percentages
        data["learning_outcomes"] = learning_outcomes
        data["module_notes_outline"] = module_notes_outline

    logger.debug(f"Final data dictionary: {data}")

    return data


def class_data_gen(logger: Logger, class_name: str, practical: bool) -> dict[str, str]:
    """
    Generate data for the tutorial and practical class markdown files.
    :param logger: Logger object
    :param class_name: Name of the practical/tutorial class
    :param practical: Whether the class is a practical class
    :return: class questions
    """

    data = {
        "class_questions": None,
    }

    # Suppress SyntaxWarning - ast.literal_eval() raises this warning, benign in this case
    # filterwarnings("ignore", category=SyntaxWarning)

    # Find the class PDF
    file_path = f"{INPUT_PATH}{'practicals' if practical else 'tutorials'}/{class_name}"

    # Convert the PDF to text
    pdf_text = pdf_to_text(logger, file_path)

    # Prompt the ChatGPT API to convert the PDF text into a list of questions
    gen_prompt = "You're a program that returns a Python List of the questions in a given PDF text, giving each question by itself and formatting each question with LaTeX where appropriate (equations, numbers, general mathematical notation, etc.), using things like \\frac and \\mathbb, surrounding all LaTeX with $ for inline equations and $$ for block equations. Return nothing else other than the Python List - if you cannot find any questions, return None. Each element of the Python List should be an entire question with its respesctive sub-questions."
    gpt_response = prompt_gpt(logger, pdf_text, gen_prompt)

    #logger.info(f"GPT response BEFORE: {gpt_response}")

    # Prompt the ChatGPT API to fix its own mistakes
    mistake_prompt = "You're a program that takes a Python list of questions and fixes any mistakes in the formatting of the questions, such as improperly escaped characters (so escape them), incorrectly written LaTeX (so guess what it should be - as long as it works then it's okay), or unknown characters (replace them with known ones, or remove them). If parts of questions (e.g. 1a, 1b) are separate from their main part (e.g. 1), then combine them into one element. Return the fixed Python list of questions."
    gpt_response = prompt_gpt(logger, gpt_response, mistake_prompt)

    #logger.info(f"GPT response MIDWAY: {gpt_response}")

    # Clean the GPT response
    gpt_response = clean_latex(logger, gpt_response, True)

    # Parse the GPT response
    try:
        gpt_response_list = ast.literal_eval(gpt_response)
    except ValueError as e:
        logger.error(f"Error parsing GPT response: {e}")
        gpt_response_list = []
    except SyntaxError as e:
        logger.warning(f"Error parsing GPT response: {e}")
        gpt_response_list = []

    # Combine sub-questions with their main questions, e.g. if an item in a list begins with "(" then combine it with the previous item
    if gpt_response_list:
        i = 1
        while i < len(gpt_response_list):
            if gpt_response_list[i].startswith("("):
                gpt_response_list[i-1] += "\n" + gpt_response_list[i]
                gpt_response_list.pop(i)
            else:
                i += 1

    logger.debug(f"GPT response: {gpt_response_list}")

    # Format the questions
    class_questions = None if not gpt_response_list else "\n\n".join([f"### Question {i+1}\n\n#### Question\n\n{question}\n\n#### Solution\n\n..." for i, question in enumerate(gpt_response_list)])

    # Return the data dictionary
    if gpt_response:
        data["class_questions"] = class_questions

    return data


def summaryquestions_data_gen(logger: Logger) -> dict[str, str]:
    """
    Generate data for the summary questions markdown files.
    :param logger: Logger object
    :return: class hyperlinks, summary questions
    """

    data = {
        "class_hyperlink_list": None,
        "summary_questions": None,
    }

    # Initialise the required variables
    data["class_hyperlink_list"] = ""
    summary_questions: list[str] = []

    # Loop through the classes folder
    for file in os.listdir(CLASSES_PATH):
        # Generate the class hyperlinks
        data["class_hyperlink_list"] += f"- [[{re.sub('.md', '', file)}]]\n"

        # Generate the summary questions
        with open(f"{CLASSES_PATH}{file}", "r", encoding='utf-8') as f:
            content = f.read()
            questions = re.findall(r"#### Question\n\n(.*?)\n\n#### Solution", content, re.DOTALL)
            summary_questions.extend(questions)
    
    data["summary_questions"] = "\n\n".join([f"{i}. {question}" for i, question in enumerate(summary_questions, start=1)])


    return data


def tests_data_gen(logger: Logger) -> dict[str, str]:
    """
    Generate data for the practice tests markdown files.
    :param logger: Logger object
    :return: practice tests hyperlinks
    """

    data = {
        "practice_test_hyperlink_list": None,
    }

    data["practice_test_hyperlink_list"] = ""

    if os.listdir(PAPERS_PATH) == []:
        logger.error("No papers found.")
        return data
    
    for file in os.listdir(PAPERS_PATH):
        data["practice_test_hyperlink_list"] += f"- [[{re.sub('.pdf', '', file)}]]\n"

    # TODO: Generate predicted papers (that look the exact same) that will also be appended to this list.

    return data


def summarynotes_data_gen(logger: Logger) -> dict[str, str]:
    """
    Generate data for the summary notes markdown files.
    :param logger: Logger object
    :return: summary notes
    """

    data = {
        "summary_notes": None,
    }

    # Find the summary questions markdown file (ends in "Summary Questions.md")
    file_path = None
    for file in os.listdir(SUMMARY_PATH):
        if file.endswith("Summary Questions.md"):
            file_path = f"{SUMMARY_PATH}{file}"
            break

    # Read the summary questions markdown file
    with open(file_path, "r", encoding='utf-8') as f:
        content = f.read()

    # Generate notes that explain how to solve every type of question in the summary questions
    gpt_response = prompt_gpt(logger, content, "You're a program that takes a list of questions and generates a detailed explanation of how to solve each type of question, including the steps, methods, and reasoning behind each step. Use a logical order and bullet points to quickly convey the information. Return the generated notes in markdown format, using LaTeX when appropriate (as in the questions given). Only return the bullet points and nothing else. If you cannot find any questions, return None.")

    # Clean the GPT response
    gpt_response = re.sub(r'```markdown\n', '', gpt_response)
    gpt_response = re.sub(r'```', '', gpt_response)

    # Return the data dictionary
    if gpt_response:
        data["summary_notes"] = gpt_response

    return data


def flashcards_data_gen(logger: Logger) -> dict[str, str]:
    """
    Generate data for the flashcards markdown files.
    :param logger: Logger object
    :return: flashcards and anki flashcards
    """

    data = {
        "flashcards": None,
        "anki_flashcards": None,
    }

    # Loop through each note markdown file and generate flashcards
    flashcards = """"""
    card_format = """
### Question

QUESTION

### Answer

ANSWER

---

"""

    for file in os.listdir(NOTES_PATH):
        with open(f"{NOTES_PATH}{file}", "r", encoding='utf-8') as f:
            content = f.read()
            flashcard = prompt_gpt(logger, content, f"You're a program that takes a markdown note and generates a list of flashcards from it, each flashcard containing a question on one side and the answer on the other. Return the list of flashcards in the following format: {card_format}")
            logger.info(f"Flashcard: {flashcard}")
            flashcards += flashcard

    data["flashcards"] = flashcards.replace("---###", r"---\n\n###")
    data["anki_flashcards"] = f"[{markdown_to_csv(logger, flashcards, "flashcards")}]({REVISION_PATH}flashcards.csv)"

    return data


def revision_data_gen(logger: Logger, module_name: str) -> dict[str, str]:
    """
    Generate data for the question-based revision markdown files.
    :param logger: Logger object
    :param module_name: Name of the module
    :return: module name, question-based revision
    """

    data = {
        "module_name": module_name,
        "question_based_revision": None,
    }

    # TODO: No idea how to generate this yet

    return data


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
        content = clean_latex(logger, prompt_gpt(logger, link, note_prompt), False) # TODO: Include link description in prompt

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
