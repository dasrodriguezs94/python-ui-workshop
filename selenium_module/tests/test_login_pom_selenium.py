import allure
from selenium_module.pages.login_page import LoginPage
from selenium_module.utils.driver_factory import get_selenium_driver

@allure.feature("Login")
def test_login_pom_selenium():
    driver = get_selenium_driver()
    login_page = LoginPage(driver)

    with allure.step("Open Login Page"):
        login_page.open("https://www.themoviedb.org/login")

    with allure.step("Perform Login"):
        login_page.login("your_username", "your_password")

    with allure.step("Verify Login"):
        assert "Dashboard" in login_page.get_title()

    driver.quit()
