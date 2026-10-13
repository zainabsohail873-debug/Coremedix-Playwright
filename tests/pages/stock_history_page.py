from playwright.sync_api import Page


class StockHistoryPage:

    def __init__(self, page: Page):
        self.page = page

        # Page sections
        self.filters = page.get_by_text(
            "Filters",
            exact=True
        )

        self.inventory_items = page.get_by_text(
            "Inventory Items",
            exact=True
        )

    def is_page_loaded(self):
        return (
            self.filters.is_visible()
            and self.inventory_items.is_visible()
        )