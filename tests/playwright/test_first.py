from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://playwright.dev/python/docs/api/class-playwright",
        wait_until="domcontentloaded",
    )
    print(page.title())

    browser.close()


def main():
    with sync_playwright() as playwright:
        run(playwright=playwright)


if __name__ == "__main__":
    main()
