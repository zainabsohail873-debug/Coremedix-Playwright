# tests/test_navigation.py
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.application_selection_page import ApplicationSelectionPage
from pages.sidebar_page import SidebarPage

def test_full_pharmacy_sidebar_navigation(page: Page):
    # 1. Login & App Select
    page.goto("https://iprouk-testing.azurewebsites.net/")
    login = LoginPage(page)
    login.login("923040217492", "1122")

    app = ApplicationSelectionPage(page)
    app.select_pharmacy()

    sidebar = SidebarPage(page)

    # 2. Navigate -> Sales: Invoices
    sidebar.navigate_to_invoices()
    expect(page).to_have_url("**/Pharmacy/Sales/ManageInvoice")
    print("\n✅ Navigation to Invoices: PASS")

    # 3. Navigate -> Inventory: Items
    sidebar.navigate_to_inventory_items()
    expect(page).to_have_url("**/Pharmacy/InventoryItems/Index")
    print("✅ Navigation to Inventory Items: PASS")

    # 4. Navigate -> Contacts: Suppliers
    sidebar.navigate_to_suppliers()
    expect(page).to_have_url("**/Pharmacy/Contacts/Suppliers")
    page.pause()
    print("✅ Navigation to Suppliers: PASS")