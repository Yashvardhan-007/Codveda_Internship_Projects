"""
Codveda Technology - Python Development Internship
Level 2 - Task 4: Data Scraper

A reusable command-line web scraper using requests and BeautifulSoup.
It extracts article titles from a public demo website and saves them
to CSV, satisfying the internship task while demonstrating practical
Python web-data collection.
"""

import csv
from dataclasses import dataclass
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


DEFAULT_URL = "https://quotes.toscrape.com/"
DEFAULT_TIMEOUT = 10
DEFAULT_OUTPUT = "scraped_quotes.csv"


class ScraperError(Exception):
    """Raised when scraping cannot be completed."""


@dataclass
class QuoteRecord:
    quote: str
    author: str
    tags: str
    source_url: str


def fetch_html(url: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    """Download HTML and handle common network/HTTP failures."""
    headers = {
        "User-Agent": "Codveda-Python-Data-Scraper/1.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.exceptions.Timeout as exc:
        raise ScraperError("The request timed out.") from exc
    except requests.exceptions.ConnectionError as exc:
        raise ScraperError("Could not connect to the website.") from exc
    except requests.exceptions.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else "unknown"
        raise ScraperError(f"Website returned HTTP status {status}.") from exc
    except requests.exceptions.RequestException as exc:
        raise ScraperError(f"Request failed: {exc}") from exc


def parse_quotes(html: str, source_url: str) -> list[QuoteRecord]:
    """Parse quote, author, and tags from the page HTML."""
    soup = BeautifulSoup(html, "html.parser")
    records = []

    for item in soup.select("div.quote"):
        quote_node = item.select_one("span.text")
        author_node = item.select_one("small.author")
        tag_nodes = item.select("a.tag")

        if not quote_node or not author_node:
            continue

        tags = ", ".join(tag.get_text(strip=True) for tag in tag_nodes)

        records.append(
            QuoteRecord(
                quote=quote_node.get_text(strip=True),
                author=author_node.get_text(strip=True),
                tags=tags,
                source_url=source_url,
            )
        )

    return records


def scrape_quotes(url: str = DEFAULT_URL) -> list[QuoteRecord]:
    """Fetch and parse quote records from a website."""
    html = fetch_html(url)
    records = parse_quotes(html, url)

    if not records:
        raise ScraperError(
            "No quote records were found. The page structure may have changed."
        )

    return records


def save_to_csv(records: list[QuoteRecord], output_file: str) -> None:
    """Save scraped records to a CSV file."""
    with open(output_file, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["quote", "author", "tags", "source_url"],
        )
        writer.writeheader()

        for record in records:
            writer.writerow({
                "quote": record.quote,
                "author": record.author,
                "tags": record.tags,
                "source_url": record.source_url,
            })


def print_preview(records: list[QuoteRecord], limit: int = 5) -> None:
    """Display a small preview of the scraped data."""
    print("\n" + "=" * 75)
    print("                    SCRAPED DATA PREVIEW")
    print("=" * 75)

    for index, record in enumerate(records[:limit], start=1):
        print(f"\n[{index}] {record.quote}")
        print(f"    Author: {record.author}")
        print(f"    Tags  : {record.tags or 'None'}")

    if len(records) > limit:
        print(f"\n... and {len(records) - limit} more records.")


def main() -> None:
    print("\n" + "=" * 75)
    print("             CODVEDA LEVEL 2 - DATA SCRAPER")
    print("=" * 75)
    print("Demo site: Quotes to Scrape")
    print("Purpose  : Extract publicly available quote data and save it to CSV.")

    url = input(f"\nEnter URL [Press Enter for {DEFAULT_URL}]: ").strip()
    url = url or DEFAULT_URL

    output_file = input(
        f"Output CSV filename [Press Enter for {DEFAULT_OUTPUT}]: "
    ).strip()
    output_file = output_file or DEFAULT_OUTPUT

    try:
        records = scrape_quotes(url)
        save_to_csv(records, output_file)
    except (ScraperError, OSError) as error:
        print(f"\n[ERROR] {error}")
        return

    print_preview(records)
    print("\n" + "-" * 75)
    print(f"Successfully scraped : {len(records)} records")
    print(f"CSV saved as         : {output_file}")
    print("-" * 75)


if __name__ == "__main__":
    main()
