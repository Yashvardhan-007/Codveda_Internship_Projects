# Codveda Level 2 - Task 4: Data Scraper

A Python web-scraping application using **Requests + BeautifulSoup** to collect publicly available quote data and export it to CSV.

## Internship Requirement

The Codveda task requires:

- Use `requests` to retrieve webpage content.
- Parse HTML using BeautifulSoup.
- Extract specific data such as article titles or product details.
- Save scraped data into a CSV file.

This implementation follows that requirement and adds validation, timeout/error handling, a reusable parser, a CLI, and automated tests.

## What This Project Scrapes

The default target is:

```text
https://quotes.toscrape.com/
```

It extracts:

- Quote
- Author
- Tags
- Source URL

The project intentionally uses **Quotes to Scrape**, a public demo website designed for practicing web scraping.

## Architecture

```text
Website
   ↓
requests
   ↓
HTML Response
   ↓
BeautifulSoup
   ↓
CSS Selectors
   ↓
Data Validation
   ↓
Python Records
   ↓
CSV Export
```

## Features

- HTTP GET requests
- BeautifulSoup HTML parsing
- CSS selector-based extraction
- CSV export
- URL input
- Output filename input
- Timeout handling
- Connection-error handling
- HTTP error handling
- Missing/changed page-structure detection
- Unit tests with mocked HTTP requests
- Clean CLI

## Installation

Recommended:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```powershell
python data_scraper.py
```

Press Enter at the URL prompt to use the default demo website.

Example:

```text
Enter URL [Press Enter for https://quotes.toscrape.com/]:
Output CSV filename [Press Enter for scraped_quotes.csv]:
```

## Output

The program creates:

```text
scraped_quotes.csv
```

with columns:

```text
quote,author,tags,source_url
```

## Tests

Run:

```powershell
python -m unittest -v
```

The tests cover:

- HTML parsing
- Empty-page handling
- Successful requests
- Timeout errors
- Connection errors
- CSV generation

## Responsible Scraping

Use this project only on websites where automated access is permitted.

Before scraping a real website:

- Check its Terms of Service.
- Check `robots.txt` where appropriate.
- Respect rate limits.
- Avoid collecting sensitive personal information.
- Do not bypass authentication, CAPTCHAs, access controls, or anti-bot protections.
- Use an identifiable, reasonable User-Agent.

## Learning Outcomes

This project develops:

- HTTP fundamentals
- Requests
- HTML/DOM concepts
- CSS selectors
- BeautifulSoup
- Structured data extraction
- CSV handling
- Exception handling
- Mocking external services
- Modular Python design

## Future Enhancements

- Multi-page pagination
- CSV/JSON output selection
- Scheduled scraping
- SQLite storage
- Duplicate detection
- Retry with exponential backoff
- Configurable CSS selectors
- Flask/Django dashboard
- Data visualization

## Author

**Yashvardhan Singh**

Python Development Intern  
Codveda Technologies
