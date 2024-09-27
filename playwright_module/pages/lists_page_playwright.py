from playwright_module.pages.base_page_playwright import BasePagePlaywright


class ListPagePlaywright(BasePagePlaywright):
    CREATE_LIST_BUTTON = '.inner_content a[href*="new"]'

    def create_list(self):
        self.click(self.CREATE_LIST_BUTTON)