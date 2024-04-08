# Module Content Generation Tool

## Overview
The Module Content Generation Tool is designed to automate the creation of educational content, specifically tailored for university modules. Utilizing Python, it generates markdown files for module pages, classes, summaries, and revision materials, streamlining the process of content creation for educators and students alike.

## Features
- **Automated Markdown Generation**: Creates markdown files for module overviews, class content, summary questions, summary notes, practice tests, and flashcards.
- **Comprehensive Data Handling**: Parses and generates content from various data sources, including lecture slides, notes, and PDFs, ensuring a wide range of educational materials are covered.
- **Customizable Output**: Offers flexibility in the generated content, allowing for adjustments to fit specific module requirements or teaching styles.
- **Enhanced Logging and Error Handling**: Incorporates advanced logging for monitoring the generation process and robust error handling mechanisms for a smooth operation.

## Getting Started

### Prerequisites
Ensure you have Python 3.8 or higher installed on your system. Dependencies include:
- `fitz` for PDF reading,
- `Jinja2` for templating markdown files,
- `OpenAI` for utilizing GPT models in content generation.

### Installation
1. Clone the repository to your local machine.
2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

### Usage
1. Place your input files (lecture slides, notes, etc.) in the designated input directory, ensuring to number classes as "1.pdf", "2.pdf", etc.
2. Run `main.py` to start the content generation process:
   ```
   python main.py
   ```
3. Follow the prompts and logs for any required manual inputs or corrections.
4. Generated markdown files will be available in the output directory, ready for review and use.

## Contributing
Contributions to the Module Content Generation Tool are welcome. Please follow the standard fork, branch, and pull request workflow.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments
- Utilizes GPT models from OpenAI for content generation.
- Inspired by the need for efficient educational content creation.