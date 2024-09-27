from playwright_module.pages.base_page_playwright import BasePagePlaywright


class CreateListPagePlaywright(BasePagePlaywright):
    NAME_INPUT = '#name'
    DESCRIPTION_INPUT = '#description'
    CONTINUE_BUTTON = '#step_1_submit'
    LIST_TITLE = '.title_block a'

    def set_list_name(self, name):
        self.enter_text(self.NAME_INPUT, name)
        
    def set_description(self, description):
        self.enter_text(self.DESCRIPTION_INPUT, description)

    def submit_list(self):
        self.click(self.CONTINUE_BUTTON)

    def get_list_title(self):
        return self.get_text(self.LIST_TITLE)