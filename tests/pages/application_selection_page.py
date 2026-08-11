from playwright.sync_api import Page


class ApplicationSelectionPage:

    def __init__(self, page: Page):
        self.page = page

        self.pharmacy = page.get_by_text("Pharmacy", exact=True)

    def select_pharmacy(self):
        self.pharmacy.click()