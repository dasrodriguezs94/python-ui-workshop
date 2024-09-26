from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """Opens the provided URL in the browser."""
        self.driver.get(url)

    def find_element(self, locator):
        """Finds a single element on the page."""
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Clicks an element on the page."""
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        """Enters text into a field."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_title(self):
        """Returns the title of the current page."""
        return self.driver.title
