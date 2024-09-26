from playwright_module.screenplay.interactions.enter_credentials_playwright import EnterCredentialsPlaywright

class LoginTaskPlaywright:
    def __init__(self, username, password):
        """Initializes the task with the username and password."""
        self.username = username
        self.password = password

    def perform_as(self, actor):
        """The actor performs the login task by entering credentials."""
        actor.attempts_to(
            EnterCredentialsPlaywright(self.username, self.password)
        )
