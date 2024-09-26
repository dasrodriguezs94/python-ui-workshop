from selenium_module.screenplay.interactions.enter_credentials import EnterCredentials

class LoginTask:
    def __init__(self, username, password):
        """Initializes the task with the username and password."""
        self.username = username
        self.password = password

    def perform_as(self, actor):
        """The actor performs the login task by entering credentials."""
        actor.attempts_to(
            EnterCredentials(self.username, self.password)
        )
