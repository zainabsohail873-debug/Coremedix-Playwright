from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username = page.get_by_label("Username / Mobile No.")
        self.password = page.locator("#Password")       
        self.sign_in_button = page.get_by_role("button", name="Sign in")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.sign_in_button.click()