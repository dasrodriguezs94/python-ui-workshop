from playwright.sync_api import sync_playwright

def get_playwright_driver(browser_type="chromium", headless=True):
    """Initializes and returns a Playwright browser instance."""
    playwright = sync_playwright().start()
    
    if browser_type.lower() == "chromium":
        browser = playwright.chromium.launch(headless=headless)
    elif browser_type.lower() == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_type.lower() == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:
        raise ValueError(f"Browser type '{browser_type}' is not supported.")
    
    page = browser.new_page()
    return browser, page
