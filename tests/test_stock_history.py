from pages.login_page import LoginPage
from pages.application_selection_page import ApplicationSelectionPage
from pages.stock_history_page import StockHistoryPage


def test_stock_history_page(page):

    # Open application
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

    # Open Stock History
    page.goto(
        "https://iprouk-testing.azurewebsites.net/Pharmacy/InventoryItems/StockHistory"
    )

    # Wait for page
    page.wait_for_timeout(3000)

    # Create page object
    stock_history = StockHistoryPage(page)

    # Verify page loaded
    assert stock_history.is_page_loaded(), (
        "Stock History page is not loaded"
    )

    print("Stock History page loaded successfully")

    # Verify table headers
    headers = [
        "Item Name",
        "Variation Name",
        "Qty",
        "Old Qty",
        "Latest Qty",
        "Status",
        "Date & Time"
    ]

    for header in headers:

        locator = page.locator(
            "table thead th"
        ).filter(
            has_text=header
        )

        assert locator.count() > 0, (
            f"{header} column is not present"
        )

        assert locator.first.is_visible(), (
            f"{header} column is not visible"
        )

    print("Stock History table headers verified successfully")