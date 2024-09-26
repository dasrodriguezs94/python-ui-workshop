class Actor:
    def __init__(self, name, page):
        """Initializes the actor with a name and a Playwright page instance."""
        self.name = name
        self.page = page

    def attempts_to(self, *tasks):
        """The actor attempts to perform a sequence of tasks."""
        for task in tasks:
            task.perform_as(self)
