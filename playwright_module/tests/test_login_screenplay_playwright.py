import allure
from playwright_module.utils.driver_factory_playwright import get_playwright_driver
from playwright_module.screenplay.actor import Actor
from playwright_module.screenplay.tasks.login_task_playwright import LoginTaskPlaywright

@allure.feature("Login")
def test_login_screenplay_playwright():
    browser, page = get_playwright_driver(headless=False)  # Use the helper function to initialize Playwright
    
    actor = Actor("Tester", page)

    with allure.step("Open Login Page"):
        page.goto("https://www.themoviedb.org/login")

    with allure.step("Perform Login"):
        actor.attempts_to(LoginTaskPlaywright("your_username", "your_password"))

    with allure.step("Verify Login"):
        assert "Dashboard" in page.title()

    browser.close()
