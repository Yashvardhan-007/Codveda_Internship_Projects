import csv
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import requests

from data_scraper import (
    ScraperError,
    fetch_html,
    parse_quotes,
    save_to_csv,
)


SAMPLE_HTML = """
<html>
<body>
<div class="quote">
    <span class="text">“First sample quote.”</span>
    <small class="author">Author One</small>
    <a class="tag">life</a>
    <a class="tag">test</a>
</div>
<div class="quote">
    <span class="text">“Second sample quote.”</span>
    <small class="author">Author Two</small>
    <a class="tag">python</a>
</div>
</body>
</html>
"""


class TestDataScraper(unittest.TestCase):

    def test_parse_quotes(self):
        records = parse_quotes(SAMPLE_HTML, "https://example.com")
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0].author, "Author One")
        self.assertEqual(records[0].tags, "life, test")

    def test_parse_empty_page(self):
        self.assertEqual(parse_quotes("<html></html>", "https://example.com"), [])

    @patch("data_scraper.requests.get")
    def test_fetch_html_success(self, mock_get):
        response = Mock()
        response.raise_for_status.return_value = None
        response.text = SAMPLE_HTML
        mock_get.return_value = response

        self.assertIn("First sample quote", fetch_html("https://example.com"))

    @patch("data_scraper.requests.get")
    def test_fetch_timeout(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout
        with self.assertRaises(ScraperError):
            fetch_html("https://example.com")

    @patch("data_scraper.requests.get")
    def test_fetch_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError
        with self.assertRaises(ScraperError):
            fetch_html("https://example.com")

    def test_save_to_csv(self):
        records = parse_quotes(SAMPLE_HTML, "https://example.com")

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "output.csv"
            save_to_csv(records, str(path))

            with path.open(encoding="utf-8-sig", newline="") as file:
                rows = list(csv.DictReader(file))

            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["author"], "Author One")
            self.assertEqual(rows[1]["tags"], "python")


if __name__ == "__main__":
    unittest.main()
