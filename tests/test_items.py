from pages.login_page import LoginPage
from pages.application_selection_page import ApplicationSelectionPage
from pages.items_page import ItemsPage


def test_items_page(page):

    # Open application
    page.goto("https://iprouk-testing.azurewebsites.net/")

    # Login
    login_page = LoginPage(page)
    login_page.login("923040217492", "1122")

    # Select Pharmacy
    application_selection = ApplicationSelectionPage(page)
    application_selection.select_pharmacy()

    # Open Items page
    page.goto(
        "https://iprouk-testing.azurewebsites.net/Pharmacy/InventoryItems/Items"
    )

    page.wait_for_timeout(3000)

    # Create Items Page object
    items_page = ItemsPage(page)

    # Verify Items page
    assert items_page.is_page_loaded(), "Items page is not loaded"
    print("Items page loaded successfully")

    # Verify Inventory Items table headers
    headers = [
        "Sr#",
        "Product Name",
        "Type",
        "Manufacturer",
        "Supplier",
        "Total Variations",
        "Near To Expire",
        "Near To Finish",
        "Stock",
        "Actions",
    ]

    for header in headers:
        locator = page.locator("table thead th").filter(has_text=header)

        assert locator.count() > 0, f"{header} column is not present"
        assert locator.first.is_visible(), f"{header} column is not visible"

    print("Inventory Items table headers verified successfully")

    # Search Inventory Item
    items_page.search_item("Imli")

    page.wait_for_timeout(2000)

    # Print visible table rows
    rows = page.locator("table tbody tr")

    print(f"Rows found after search: {rows.count()}")

    for i in range(rows.count()):
        print(f"Row {i + 1}: {rows.nth(i).inner_text()}")

    print("Inventory item search executed successfully")