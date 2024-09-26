import os
from dotenv import load_dotenv
import allure
from playwright_module.utils.driver_factory_playwright import get_playwright_driver
from playwright_module.pages.login_page_playwright import LoginPagePlaywright

load_dotenv()

@allure.feature("Login")
def test_login_pom_playwright():
    browser, page = get_playwright_driver(headless=False)  # Use the helper function to initialize Playwright
    
    login_page = LoginPagePlaywright(page)

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    
    with allure.step("Open Login Page"):
        login_page.open("https://www.themoviedb.org/login")

    with allure.step("Perform Login"):
        login_page.login(username, password)

    with allure.step("Verify Login"):
        assert "My Profile" in login_page.get_title()

    browser.close()
