class CreateListInteractionPlaywright:
    LIST_NAME_INPUT = '#name'
    LIST_DESCRIPTION_INPUT = '#description'
    CREATE_BUTTON = '#step_1_submit'

    def __init__(self, list_name, description):
        """Initializes the interaction with the list name and description."""
        self.list_name = list_name
        self.description = description

    def perform_as(self, actor):
        """Performs the action of creating a new list."""
        page = actor.page

        # Fill in the list name
        page.locator(self.LIST_NAME_INPUT).fill(self.list_name)

        # Fill in the description
        page.locator(self.LIST_DESCRIPTION_INPUT).fill(self.description)

        # Click the create button
        page.locator(self.CREATE_BUTTON).click()
