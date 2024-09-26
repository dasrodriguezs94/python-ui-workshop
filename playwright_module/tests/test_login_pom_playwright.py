import allure
from playwright_module.utils.driver_factory_playwright import get_playwright_driver
from playwright_module.pages.login_page_playwright import LoginPagePlaywright

@allure.feature("Login")
def test_login_pom_playwright():
    browser, page = get_playwright_driver(headless=False)  # Use the helper function to initialize Playwright
    
    login_page = LoginPagePlaywright(page)
    
    with allure.step("Open Login Page"):
        login_page.open("https://www.themoviedb.org/login")

    with allure.step("Perform Login"):
        login_page.login("your_username", "your_password")

    with allure.step("Verify Login"):
        assert "Dashboard" in login_page.get_title()

    browser.close()
