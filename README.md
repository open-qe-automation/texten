# TEXTEN - TEXT Extraction Node

TEXTEN is a robust and efficient application designed to automate the process of extracting text from various file formats, detecting Personally Identifiable Information (PII), and managing the results effectively. This tool is particularly useful for organizations that handle large volumes of documents and need to ensure compliance with data privacy regulations.

Key Features
- Text Extraction: Supports multiple file formats including DOCX, PDF, XLSX, CSV, PPTX, HTML, RTF.
- PII Detection: Uses configurable regex patterns to identify and flag sensitive information such as SSNs and credit card numbers.
- File Hashing: Implements file hashing to detect changes and avoid reprocessing files unnecessarily.
- Exclusion Patterns: Allows configuration of file and directory exclusion patterns.
- Logging and Reporting: Maintains comprehensive logs of processing activities.
- Configurable Output: Saves processed text and PII-flagged content to designated output directories.

## Git Repositories
- https://github.com/open-qe-automation/texten.git
- https://github.com/open-qe-automation/webtexten.git
- https://github.com/open-qe-automation/chunken.git
- https://github.com/open-qe-automation/datamyn.git

## Related Packages
- https://github.com/open-qe-automation/package.utils.git
- https://github.com/open-qe-automation/package.data.loaders.git
- https://github.com/open-qe-automation/package.helpers.git

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.12 or later
- pip

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/open-qe-automation/texten.git
    cd texten
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    For local development, use dev-requirements.txt:
    ```bash
    pip install -r dev-requirements.txt
    ```

## Usage

To run the TEXTEN application, use the following command:

```bash
python app.py
```

### Configuration

The configuration is managed through a `config.json` file:

```json
{
  "input_directories": ["../share/input"],
  "text_output_directory": "../share/text_output",
  "pii_output_directory": "../share/pii_output",
  "hash_file_path": "file_hashes.json",
  "patterns": {
    "credit_card_numbers": "\\b(?:\\d{4}[ -]?){3}\\d{4}\\b",
    "social_security_numbers": "\\b\\d{3}-\\d{2}-\\d{4}\\b"
  },
  "exclusions": ["*.tmp", "*.log"],
  "scheduler_interval": 60
}
```

## Output

TEXTEN extracts text from input files and saves them to the text output directory. Files are processed only if they have changed (based on hash).

## Testing

Run tests with pytest:

```bash
pip install -r dev-requirements.txt
pytest
```

Tests are located in the `tests/` directory.