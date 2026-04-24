from playwright.sync_api import sync_playwright, Playwright


def test_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com")
        page.fill("textarea[name='q']", "stripe.com")
        page.press("textarea[name='q']", "Enter")

        assert "Stripe" in page.title()
        browser.close()


if __name__ == "__main__":
    test_google()
