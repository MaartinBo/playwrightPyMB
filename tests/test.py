from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://mb-qa.eu/")
    cart_button = page.get_by_role("link", name="Cart")
    cart_button.click()
    print("Cart:", page.url)
    browser.close()
