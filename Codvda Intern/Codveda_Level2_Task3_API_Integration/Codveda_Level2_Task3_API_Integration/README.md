# Codveda Level 2 - Task 3: API Integration

A command-line REST API client developed in Python for the Codveda Technology Python Development Internship.

## Internship Requirement
- Use Python's `requests` library.
- Make a GET request to a public API.
- Parse returned JSON.
- Display selected information.
- Handle request/response errors.

## API
JSONPlaceholder:
`https://jsonplaceholder.typicode.com/users`

The application displays user ID, name, username, and email.

## Features
- REST API GET request
- JSON parsing
- HTTP, connection, timeout, and invalid-JSON error handling
- Response validation
- Search user by ID
- Refresh API data
- Unit tests with mocked requests
- Clean CLI

## Setup

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```powershell
python api_client.py
```

## Test

```powershell
python -m unittest -v
```

## Project Structure
```text
Codveda_Level2_Task3_API_Integration/
├── api_client.py
├── test_api_client.py
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
└── TEST_RESULTS.txt
```

## Author
Yashvardhan Singh — Python Development Intern, Codveda Technologies
