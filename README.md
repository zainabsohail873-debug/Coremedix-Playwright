
# CoreMedix – Playwright Automation Testing

UI automation testing project for the CoreMedix healthcare management system using Python, Playwright, and pytest.

## About the Project

This project contains automated UI test scripts developed to practice and validate key workflows in the CoreMedix application. It follows the Page Object Model (POM) approach to keep test code organized and maintainable.

## Tech Stack

- Python
- Playwright
- pytest
- Page Object Model (POM)
- Git and GitHub

## Project Structure

```text
Coremedix/
├── tests/
│   ├── pages/
│   │   ├── dashboard_page.py
│   │   ├── invoices_page.py
│   │   ├── items_page.py
│   │   ├── sidebar_page.py
│   │   └── stock_history_page.py
│   ├── test_create_item.py
│   ├── test_dashboard.py
│   ├── test_invoices.py
│   ├── test_items.py
│   ├── test_navigation.py
│   └── test_stock_history.py
├── .gitignore
└── README.md
```

## Automated Test Areas

- Dashboard
- Navigation
- Inventory Items
- Item Creation
- Invoices
- Stock History

## Prerequisites

- Python installed
- Git installed
- Access to the application test environment

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/zainabsohail873-debug/Coremedix-Playwright.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Coremedix-Playwright
   ```

3. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

4. Install the required packages:

   ```bash
   pip install pytest pytest-playwright
   playwright install
   ```

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_dashboard.py
```

Run tests with a detailed summary:

```bash
pytest -v
```

## Project Goals

- Practice UI automation using Playwright and Python.
- Improve test coverage for important application workflows.
- Use reusable page objects and maintainable test scripts.
- Strengthen practical QA automation skills.

## Author

**Zainab Sohail**

QA Engineer | Software Quality Assurance | Learning Test Automation