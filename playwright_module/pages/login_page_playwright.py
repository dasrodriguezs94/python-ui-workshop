from playwright_module.pages.base_page_playwright import BasePagePlaywright

class LoginPagePlaywright(BasePagePlaywright):
    # Locators for the login page
    EMAIL_INPUT = 'input#username'  # CSS selector for the email/username input
    PASSWORD_INPUT = 'input#password'  # CSS selector for the password input
    LOGIN_BUTTON = 'button[type="submit"]'  # CSS selector for the login button
    ERROR_MESSAGE = 'div.error'  # CSS selector for login error message (if applicable)

    def login(self, username, password):
        """Performs login by filling the credentials and clicking the login button."""
        self.enter_text(self.EMAIL_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_error_message_displayed(self):
        """Checks if an error message is displayed after a failed login attempt."""
        return self.page.locator(self.ERROR_MESSAGE).is_visible()
