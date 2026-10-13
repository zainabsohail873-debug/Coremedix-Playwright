import time

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.application_selection_page import ApplicationSelectionPage
from pages.items_page import ItemsPage


def test_create_new_inventory_item(page: Page):

    # =========================
    # Login
    # =========================

    page.goto(
        "https://iprouk-testing.azurewebsites.net/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    login_page = LoginPage(page)

    login_page.login(
        "923040217492",
        "1122"
    )

    # =========================
    # Select Pharmacy
    # =========================

    application_selection = ApplicationSelectionPage(page)

    application_selection.select_pharmacy()

    # =========================
    # Open Items Page
    # =========================

    page.goto(
        "https://iprouk-testing.azurewebsites.net/Pharmacy/InventoryItems/Items",
        wait_until="domcontentloaded",
        timeout=60000
    )

    items_page = ItemsPage(page)

    # =========================
    # Open Add Item
    # =========================

    items_page.open_create_item_form()

    print(
        "\n✅ Add Item form opened"
    )

    # =========================
    # Unique Item Name
    # =========================

    unique_item_name = (
        f"Test_Item_{int(time.time())}"
    )

    # =========================
    # Create Item
    # =========================

    items_page.create_new_item(
        name=unique_item_name,
        manufacturer="GSK"
    )

    print(
        f"✅ Item '{unique_item_name}' created"
    )

    # =========================
    # Add Variation
    # =========================

    items_page.add_variation(
        unique_item_name
    )

    print(
        f"✅ Variation added for "
        f"'{unique_item_name}'"
    )

    # =========================
    # Go Back To Items
    # =========================

    page.goto(
        "https://iprouk-testing.azurewebsites.net/Pharmacy/InventoryItems/Items",
        wait_until="domcontentloaded",
        timeout=60000
    )

    # =========================
    # Search Item
    # =========================

    items_page.search_item(
        unique_item_name
    )

    # =========================
    # Verify Item
    # =========================

    expect(
        page.locator(
            "table tbody tr"
        ).first
    ).to_contain_text(
        unique_item_name,
        timeout=10000
    )

    print(
        f"✅ Verified: Item "
        f"'{unique_item_name}' "
        f"successfully created!"
    )