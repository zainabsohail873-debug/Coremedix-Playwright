from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

    def is_dashboard_loaded(self):
        # Explicit wait taake page redirect hone ka wait kare
        try:
            expect(self.page.get_by_text("Pharmacy", exact=True).first).to_be_visible(timeout=5000)
            return True
        except AssertionError:
            return False

    def get_card_locator(self, card_name: str):
        # Card container ko text se locate karna bina specific class par hardcoded depend huwe
        return self.page.locator("div").filter(
            has=self.page.get_by_text(card_name, exact=True)
        ).last

    def is_card_visible(self, card_name: str) -> bool:
        card = self.get_card_locator(card_name)
        try:
            expect(card).to_be_visible(timeout=3000)
            return True
        except AssertionError:
            return False

    def get_card_value(self, card_name: str) -> str:
        card = self.get_card_locator(card_name)
        # Inner text se overall string extract karna jab tag dynamic ho
        expect(card).to_be_visible()
        raw_text = card.inner_text()
        
        # Card label text remove karke sirf numeric value / status nikalna
        value = raw_text.replace(card_name, "").strip()
        return value