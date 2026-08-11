from playwright.sync_api import Page


class DashboardPage:

    def __init__(self, page: Page):
        self.page = page

    def is_dashboard_loaded(self):
        return self.page.get_by_text("Pharmacy", exact=True).is_visible()

    def is_card_visible(self, card_name):
        card = self.page.locator(".kpi-card").filter(
            has=self.page.get_by_text(card_name, exact=True)
        )
        return card.is_visible()

    def get_card_value(self, card_name):
        card = self.page.locator(".kpi-card").filter(
            has=self.page.get_by_text(card_name, exact=True)
        )

        value = card.locator("h4").inner_text()

        return value.strip()