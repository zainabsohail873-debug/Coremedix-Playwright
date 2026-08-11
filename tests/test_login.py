from pages.login_page import LoginPage


def test_valid_login(page):

    page.goto("https://iprouk-testing.azurewebsites.net/")

    login_page = LoginPage(page)

    login_page.login(
        "923040217492",
        "1122"
    )

    page.wait_for_timeout(5000)

    print("Current URL:", page.url)

    page.screenshot(path="dashboard.png", full_page=True)