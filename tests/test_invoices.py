from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.application_selection_page import ApplicationSelectionPage
from pages.dashboard_page import DashboardPage


def test_pharmacy_invoices_navigation(page: Page):
    # 1. Login & Select Pharmacy
    page.goto("https://iprouk-testing.azurewebsites.net/")
    login_page = LoginPage(page)
    login_page.login("923040217492", "1122")

    application_selection = ApplicationSelectionPage(page)
    application_selection.select_pharmacy()

    # 2. Verify Dashboard
    dashboard = DashboardPage(page)
    assert dashboard.is_dashboard_loaded(), "Dashboard failed to load"

    # 3. Direct Navigation to Manage Invoices Page
    target_url = "https://iprouk-testing.azurewebsites.net/Pharmacy/Sales/ManageInvoice"
    page.goto(target_url)

    # 4. Assert Navigation Success
    expect(page).to_have_url(target_url)
    
    # 5. Verify Invoices UI components loaded
    # Header or Create Button Check
    create_btn = page.locator("button, a").filter(has_text="Create").first
    expect(create_btn).to_be_visible(timeout=10000)

    print("\n✅ Successfully navigated and verified Manage Invoices page!")