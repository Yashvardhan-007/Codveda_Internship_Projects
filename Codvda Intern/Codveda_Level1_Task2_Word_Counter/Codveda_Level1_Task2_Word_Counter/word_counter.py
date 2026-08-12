"""
Codveda Technology - Python Development Internship
Level 1 - Task 2: Word Counter

Reads a text file and counts the number of words.
The implementation also provides useful text statistics while
keeping the core Codveda requirement explicit.
"""

from collections import Counter
from pathlib import Path
import re


def read_file(file_path: str) -> str:
    """Read UTF-8 text from a file.

    Raises:
        FileNotFoundError: If the requested file does not exist.
        OSError: If the file cannot be opened/read.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not path.is_file():
        raise OSError(f"Path is not a file: {file_path}")

    return path.read_text(encoding="utf-8")


def extract_words(text: str) -> list[str]:
    """Extract words from text using a Unicode-friendly regex."""
    return re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE)


def count_words(text: str) -> int:
    """Return the total number of words in the supplied text."""
    return len(extract_words(text))


def count_lines(text: str) -> int:
    """Return the number of lines in the supplied text."""
    if not text:
        return 0
    return len(text.splitlines())


def count_characters(text: str) -> int:
    """Return the number of characters, including whitespace."""
    return len(text)


def count_characters_without_spaces(text: str) -> int:
    """Return the number of non-whitespace characters."""
    return sum(not char.isspace() for char in text)


def most_common_words(text: str, limit: int = 5) -> list[tuple[str, int]]:
    """Return the most common words, case-insensitively."""
    words = [word.lower() for word in extract_words(text)]
    return Counter(words).most_common(limit)


def build_report(file_path: str, text: str) -> dict:
    """Build a dictionary containing the analysis results."""
    words = extract_words(text)

    return {
        "file": str(Path(file_path)),
        "words": len(words),
        "lines": count_lines(text),
        "characters": count_characters(text),
        "characters_without_spaces": count_characters_without_spaces(text),
        "unique_words": len(set(word.lower() for word in words)),
        "most_common": most_common_words(text),
    }


def print_report(report: dict) -> None:
    """Display analysis results in a clean CLI format."""
    print("\n" + "=" * 60)
    print("                 CODVEDA WORD COUNTER")
    print("=" * 60)
    print(f"File                       : {report['file']}")
    print(f"Total words                : {report['words']}")
    print(f"Unique words               : {report['unique_words']}")
    print(f"Lines                      : {report['lines']}")
    print(f"Characters                 : {report['characters']}")
    print(
        "Characters (without spaces): "
        f"{report['characters_without_spaces']}"
    )

    print("\nMost common words:")
    if report["most_common"]:
        for word, frequency in report["most_common"]:
            print(f"  {word:<25} {frequency}")
    else:
        print("  No words found.")

    print("=" * 60)


def main() -> None:
    """Run the interactive word-counter application."""
    print("\nCodveda Level 1 - Task 2: Word Counter")
    print("Enter the path of a .txt file to analyze.")
    print("Type 'exit' to quit.")

    while True:
        file_path = input("\nFile path: ").strip()

        if file_path.lower() == "exit":
            print("Goodbye!")
            break

        if not file_path:
            print("[ERROR] File path cannot be empty.")
            continue

        try:
            text = read_file(file_path)

            if not text.strip():
                print("[WARNING] The file is empty.")
                report = build_report(file_path, text)
            else:
                report = build_report(file_path, text)

            print_report(report)

        except FileNotFoundError as error:
            print(f"[ERROR] {error}")
        except UnicodeDecodeError:
            print(
                "[ERROR] The file is not valid UTF-8 text "
                "or uses an unsupported text encoding."
            )
        except OSError as error:
            print(f"[ERROR] Could not read the file: {error}")


if __name__ == "__main__":
    main()
