# tests/test_dashboard.py
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.application_selection_page import ApplicationSelectionPage
from pages.dashboard_page import DashboardPage


def test_pharmacy_dashboard_data_integrity(page: Page):
    # Bypass DNS resolution/cache delays
    page.context.set_extra_http_headers({"Cache-Control": "no-cache"})
    
    # 1. Open Application with Retry Strategy & Login
    try:
        page.goto("https://iprouk-testing.azurewebsites.net/", wait_until="domcontentloaded", timeout=30000)
    except Exception:
        page.reload()

    login_page = LoginPage(page)
    login_page.login("923040217492", "1122")

    # 2. Intercept exact Dashboard API call
    with page.expect_response("**/Pharmacy/InventoryItems/GetInventoryItemsInfo") as response_info:
        application_selection = ApplicationSelectionPage(page)
        application_selection.select_pharmacy()

    # 3. Extract JSON Payload
    response = response_info.value
    assert response.status == 200, "Dashboard API call failed"
    json_response = response.json()
    
    assert json_response["Status"] is True, "API Status returned False"
    api_data = json_response["Data"]

    print("\n--- [API DATA VERIFIED] ---")
    print(f"API Total Items: {api_data['TotalItems']}")
    print(f"API Low Stock Items: {api_data['LowStockItems']}")
    print(f"API New Arrival Items: {api_data['NewArrivalItems']}")

    # 4. Verify UI Cards against API Response
    dashboard = DashboardPage(page)
    assert dashboard.is_dashboard_loaded(), "Dashboard layout not loaded"

    # UI Values Extract
    ui_total_items = dashboard.get_card_value("Total Items")
    ui_low_stock = dashboard.get_card_value("Low Stock Items")
    ui_new_arrival = dashboard.get_card_value("New Arrival Items")

    # Assertions: Compare UI Card Strings with API Numbers
    assert str(api_data["TotalItems"]) in ui_total_items, f"Mismatch: UI ({ui_total_items}) != API ({api_data['TotalItems']})"
    assert str(api_data["LowStockItems"]) in ui_low_stock, f"Mismatch: UI ({ui_low_stock}) != API ({api_data['LowStockItems']})"
    assert str(api_data["NewArrivalItems"]) in ui_new_arrival, f"Mismatch: UI ({ui_new_arrival}) != API ({api_data['NewArrivalItems']})"

    print("\n✅ DATA INTEGRITY SUCCESS: UI cards dynamically match Backend API Payload!")