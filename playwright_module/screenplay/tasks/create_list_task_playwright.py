from playwright_module.screenplay.interactions.create_list_playwright import CreateListInteractionPlaywright

class CreateListTaskPlaywright:
    def __init__(self, list_name, description):
        """Initializes the task with the list name and description."""
        self.list_name = list_name
        self.description = description

    def perform_as(self, actor):
        """The actor performs the task of creating a new list."""
        actor.attempts_to(
            CreateListInteractionPlaywright(self.list_name, self.description)
        )
