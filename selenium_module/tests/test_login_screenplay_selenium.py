import os
from dotenv import load_dotenv
import allure
from selenium_module.screenplay.actor import Actor
from selenium_module.screenplay.tasks.login_task import LoginTask
from selenium_module.utils.driver_factory import get_selenium_driver

load_dotenv()

@allure.feature("Login")
def test_login_screenplay_selenium():
    driver = get_selenium_driver()
    actor = Actor("Tester", driver)

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    with allure.step("Open Login Page"):
        driver.get("https://www.themoviedb.org/login")

    with allure.step("Perform Login"):
        actor.attempts_to(LoginTask(username, password))

    with allure.step("Verify Login"):
        assert "Dashboard" in driver.title

    driver.quit()
