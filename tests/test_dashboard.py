from pages.login_page import LoginPage
from pages.application_selection_page import ApplicationSelectionPage
from pages.dashboard_page import DashboardPage


def test_pharmacy_dashboard(page):

    page.goto("https://iprouk-testing.azurewebsites.net/")

    # Login
    login_page = LoginPage(page)

    login_page.login(
        "923040217492",
        "1122"
    )

    # Select Pharmacy
    application_selection = ApplicationSelectionPage(page)

    application_selection.select_pharmacy()

    # Wait for Dashboard
    page.wait_for_timeout(5000)

    dashboard = DashboardPage(page)

    # Dashboard loaded
    assert dashboard.is_dashboard_loaded()

    # Verify all dashboard cards
    cards = [
        "Total Gross Sale",
        "Total Receivables Today",
        "Average Order Value",
        "Total Profit",
        "Total Customers Today",
        "Stock Value",
        "Near Expiry Value",
        "Dead Stock Value",
        "Expiring Soon",
        "Total Items",
        "New Arrival Items",
        "Gross Profit %",
        "Sales Growth %",
        "Low Stock Items",
        "Out of Stock Items",
        "Return Invoices"
    ]

    for card in cards:
        assert dashboard.is_card_visible(card), f"{card} card is not visible"

        value = dashboard.get_card_value(card)

        print(f"{card}: {value}")

        assert value != "", f"{card} value is blank"