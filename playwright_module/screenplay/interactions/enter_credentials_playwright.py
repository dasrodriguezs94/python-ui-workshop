class EnterCredentialsPlaywright:
    EMAIL_INPUT = 'input#username'  # CSS selector for the email/username input
    PASSWORD_INPUT = 'input#password'  # CSS selector for the password input
    LOGIN_BUTTON = 'button[type="submit"]'  # CSS selector for the login button

    def __init__(self, username, password):
        """Initializes the interaction with the username and password."""
        self.username = username
        self.password = password

    def perform_as(self, actor):
        """The actor performs the interaction of entering credentials and submitting the form."""
        page = actor.page

        # Find and fill the username
        page.locator(self.EMAIL_INPUT).fill(self.username)

        # Find and fill the password
        page.locator(self.PASSWORD_INPUT).fill(self.password)

        # Click the login button
        page.locator(self.LOGIN_BUTTON).click()
