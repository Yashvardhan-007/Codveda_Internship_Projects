# Codveda Level 1 - Task 2: Word Counter

A professional command-line **Word Counter and Text Analyzer** developed in Python for the **Codveda Technology Python Development Internship**.

## Internship Requirement

The official task requires a Python program that:

- Reads a text file
- Splits the content into words
- Counts the words
- Handles exceptions such as a file not being found

This project satisfies those requirements and extends them with useful text-analysis features.

## Features

### Required functionality
- Read a text file
- Extract words
- Count total words
- Handle missing files

### Additional functionality
- Count lines
- Count total characters
- Count characters excluding whitespace
- Count unique words
- Display the five most common words
- UTF-8 handling
- Clean command-line interface
- Automated unit tests

## Technologies

- Python 3
- Standard Library only
- `pathlib`
- `re`
- `collections.Counter`
- `unittest`

No external packages are required.

## Project Structure

```text
Codveda_Level1_Task2_Word_Counter/
│
├── word_counter.py
├── test_word_counter.py
├── sample.txt
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Requirements

Python 3.9+ recommended.

Check:

```bash
python --version
```

## Run the Application

```bash
python word_counter.py
```

On Linux/macOS:

```bash
python3 word_counter.py
```

When prompted, enter the path of a text file:

```text
File path: sample.txt
```

## Example Output

```text
============================================================
                 CODVEDA WORD COUNTER
============================================================
File                       : sample.txt
Total words                : 27
Unique words               : 23
Lines                      : 3
Characters                 : ...
Characters (without spaces): ...

Most common words:
  python                    3
  is                        2
  ...
============================================================
```

## Error Handling

### Missing file

```text
File path: missing.txt
[ERROR] File not found: missing.txt
```

### Empty path

```text
File path:
[ERROR] File path cannot be empty.
```

### Unsupported text encoding

The program catches UTF-8 decoding errors and reports them instead of terminating unexpectedly.

## Run Unit Tests

```bash
python -m unittest -v
```

The test suite covers:

- Word extraction
- Word counting
- Line counting
- Character counting
- Common-word analysis
- File reading
- Missing-file handling
- Report generation

## Learning Outcomes

This project demonstrates:

- Functions
- File handling
- `pathlib`
- Regular expressions
- Lists and sets
- Dictionaries
- `Counter`
- Exception handling
- Input validation
- Modular design
- Unit testing
- Command-line application development

## Future Enhancements

Possible future versions could include:

- GUI using Tkinter
- Web interface using Flask/Django
- PDF/DOCX support
- Export reports to JSON/CSV
- Language-specific tokenization
- Stop-word filtering
- Word-frequency visualization
- Batch processing of directories

## Author

**Yashvardhan Singh**

Python Development Intern  
Codveda Technologies
