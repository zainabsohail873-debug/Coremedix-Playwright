# CoreMedix - Pharmacy Playwright Automation

Playwright automation framework developed using Python and Pytest for testing the CoreMedix HIMS Pharmacy module.

## Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)

## Automated Areas

### Login
- Valid login
- Application selection
- Pharmacy selection

### Pharmacy Dashboard
- Dashboard loading verification
- Dashboard KPI card visibility
- Dashboard KPI value presence
- 16 dashboard KPI cards validation

## Project Structure

tests/
├── pages/
│   ├── login_page.py
│   ├── application_selection_page.py
│   └── dashboard_page.py
│
├── test_login.py
└── test_dashboard.py

## Test Execution

Run login test:

pytest tests/test_login.py -v --headed

Run dashboard test:

pytest tests/test_dashboard.py -v --headed -s
