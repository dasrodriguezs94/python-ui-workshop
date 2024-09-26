class Actor:
    def __init__(self, name, driver):
        """Initializes the actor with a name and a Selenium WebDriver instance."""
        self.name = name
        self.driver = driver

    def attempts_to(self, *tasks):
        """The actor attempts to perform a sequence of tasks."""
        for task in tasks:
            task.perform_as(self)
