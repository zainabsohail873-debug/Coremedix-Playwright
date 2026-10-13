from playwright.sync_api import Page, expect

class InvoicesPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.page_heading = page.get_by_role("heading", name="Invoices")
        self.create_invoice_btn = page.get_by_role("button", name="Create Invoice")
        self.search_invoice_input = page.locator("input[type='search'], input[placeholder*='Search']").first
        self.invoices_table = page.locator("table")

    def is_page_loaded(self) -> bool:
        try:
            expect(self.page).to_have_url("https://iprouk-testing.azurewebsites.net/Pharmacy/Sales/ManageInvoice")
            return True
        except Exception:
            return False

    def open_create_invoice_form(self):
        expect(self.create_invoice_btn).to_be_visible()
        self.create_invoice_btn.click()