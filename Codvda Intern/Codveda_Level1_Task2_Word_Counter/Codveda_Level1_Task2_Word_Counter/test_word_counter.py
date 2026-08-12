"""Unit tests for Codveda Level 1 Task 2."""

import tempfile
import unittest
from pathlib import Path

from word_counter import (
    build_report,
    count_characters,
    count_characters_without_spaces,
    count_lines,
    count_words,
    extract_words,
    most_common_words,
    read_file,
)


class TestWordCounter(unittest.TestCase):

    def test_extract_words(self):
        text = "Hello, Python! This is a test."
        self.assertEqual(
            extract_words(text),
            ["Hello", "Python", "This", "is", "a", "test"]
        )

    def test_count_words(self):
        self.assertEqual(count_words("Python is powerful and Python is easy"), 7)

    def test_count_lines(self):
        self.assertEqual(count_lines("line one\nline two\nline three"), 3)

    def test_count_lines_empty(self):
        self.assertEqual(count_lines(""), 0)

    def test_character_count(self):
        self.assertEqual(count_characters("Hello World"), 11)

    def test_character_count_without_spaces(self):
        self.assertEqual(count_characters_without_spaces("Hello World"), 10)

    def test_most_common_words(self):
        result = most_common_words("Python python Java python java")
        self.assertEqual(result[0], ("python", 3))
        self.assertEqual(result[1], ("java", 2))

    def test_read_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_text("Python development is fun.", encoding="utf-8")
            self.assertEqual(read_file(str(path)), "Python development is fun.")

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            read_file("this_file_does_not_exist.txt")

    def test_build_report(self):
        text = "Python is great.\nPython is useful."
        report = build_report("sample.txt", text)

        self.assertEqual(report["words"], 6)
        self.assertEqual(report["lines"], 2)
        self.assertEqual(report["characters"], len(text))
        self.assertEqual(report["unique_words"], 4)


if __name__ == "__main__":
    unittest.main()
