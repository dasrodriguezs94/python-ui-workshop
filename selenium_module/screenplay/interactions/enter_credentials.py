from selenium.webdriver.common.by import By

class EnterCredentials:
    EMAIL_INPUT = (By.ID, "username")  # Locator for username/email input
    PASSWORD_INPUT = (By.ID, "password")  # Locator for password input
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")  # Locator for the login button

    def __init__(self, username, password):
        """Initializes the interaction with the username and password."""
        self.username = username
        self.password = password

    def perform_as(self, actor):
        """The actor performs the interaction of entering credentials and submitting the form."""
        driver = actor.driver

        # Find and fill the username
        email_input = driver.find_element(*self.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(self.username)

        # Find and fill the password
        password_input = driver.find_element(*self.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(self.password)

        # Click the login button
        login_button = driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
