from playwright_module.pages.base_page_playwright import BasePagePlaywright


class ProfilePagePlaywright(BasePagePlaywright):
    LIST_BUTTON = '.inner_content a[href*="lists"]'

    def go_to_lists(self):
        self.click(self.LIST_BUTTON)