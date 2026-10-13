# pages/sidebar_page.py
from playwright.sync_api import Page, expect

class SidebarPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Parent Menu Locators
        self.contacts_menu = page.locator("a.nav-link").filter(has_text="Contacts").first
        self.inventory_menu = page.locator("a.nav-link").filter(has_text="Inventory").first
        self.sales_menu = page.locator("a.nav-link").filter(has_text="Sales").first
        self.purchases_menu = page.locator("a.nav-link").filter(has_text="Purchases").first
        self.orders_menu = page.locator("a.nav-link").filter(has_text="Orders").first
        self.reports_menu = page.locator("a.nav-link").filter(has_text="Reports").first

        # Submenu Links Locators
        self.invoices_link = page.locator('a[href*="/Pharmacy/Sales/ManageInvoice"]').first
        self.inventory_items_link = page.locator('a[href*="/Pharmacy/InventoryItems/Index"]').first
        self.suppliers_link = page.locator('a[href*="/Pharmacy/Contacts/Suppliers"]').first
        self.purchase_orders_link = page.locator('a[href*="/Pharmacy/Purchases/PurchaseOrders"]').first

    def _click_submenu(self, parent, child):
        """Generic helper to handle menu expansion & sub-link click smoothly"""
        parent.scroll_into_view_if_needed()
        parent.dispatch_event("click")
        self.page.wait_for_timeout(300)
        
        if child.is_visible():
            child.click()
        else:
            child.dispatch_event("click")

    # Specific Module Navigations
    def navigate_to_invoices(self):
        self._click_submenu(self.sales_menu, self.invoices_link)

    def navigate_to_inventory_items(self):
        self._click_submenu(self.inventory_menu, self.inventory_items_link)

    def navigate_to_suppliers(self):
        self._click_submenu(self.contacts_menu, self.suppliers_link)