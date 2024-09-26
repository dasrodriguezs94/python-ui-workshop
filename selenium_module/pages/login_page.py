from selenium.webdriver.common.by import By
from selenium_module.pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators for the login page
    EMAIL_INPUT = (By.ID, "username")  # Locator for the username/email input field
    PASSWORD_INPUT = (By.ID, "password")  # Locator for the password input field
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")  # Locator for the login button
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error")  # Locator for login error message

    def login(self, username, password):
        """Performs login action by entering credentials and submitting the form."""
        self.enter_text(self.EMAIL_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_error_message_displayed(self):
        """Checks if an error message is displayed after a failed login attempt."""
        try:
            error_element = self.find_element(self.ERROR_MESSAGE)
            return error_element.is_displayed()
        except:
            return False
