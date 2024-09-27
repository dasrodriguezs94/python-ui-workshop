class BasePagePlaywright:
    def __init__(self, page):
        """Initializes the BasePage with a Playwright page instance."""
        self.page = page

    def open(self, url):
        """Navigates to the specified URL."""
        self.page.goto(url)

    def find_element(self, locator):
        """Finds a single element using a Playwright locator."""
        return self.page.locator(locator)

    def click(self, locator):
        """Clicks an element."""
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        """Fills an input field with the provided text."""
        self.find_element(locator).fill(text)

    def get_title(self):
        """Returns the title of the current page."""
        return self.page.title()
    
    def get_text(self, locator):
        return self.find_element(locator).inner_text()
