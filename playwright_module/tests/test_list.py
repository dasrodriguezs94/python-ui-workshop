import os
import time
from dotenv import load_dotenv
import allure
from playwright_module.pages.create_list_page_playwright import CreateListPagePlaywright
from playwright_module.pages.lists_page_playwright import ListPagePlaywright
from playwright_module.pages.login_page_playwright import LoginPagePlaywright
from playwright_module.pages.profile_page_playwright import ProfilePagePlaywright
from playwright_module.screenplay.actor import Actor
from playwright_module.screenplay.tasks.create_list_task_playwright import CreateListTaskPlaywright
from playwright_module.screenplay.tasks.login_task_playwright import LoginTaskPlaywright
from playwright_module.utils.allure_helper_playwright import capture_screenshot
from playwright_module.utils.driver_factory_playwright import get_playwright_driver


load_dotenv()

@allure.feature("Create New List")
def test_create_list_pom_playwright():
    browser, page = get_playwright_driver(headless=False)
    
    login_page = LoginPagePlaywright(page)
    login_page.open("https://www.themoviedb.org/login")
    login_page.login(username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))

    profile_page = ProfilePagePlaywright(page)

    with allure.step("Navigate to create list"):
        profile_page.go_to_lists()
        list_page = ListPagePlaywright(page)
        list_page.create_list()
        create_list_page = CreateListPagePlaywright(page)

    with allure.step("Create a new list"):
        create_list_page.set_list_name("My Favorite Movies")
        create_list_page.set_description("A list of my all-time favorite movies.")
        time.sleep(2)
        create_list_page.submit_list()
        assert "My Favorite Movies" in create_list_page.get_list_title()
        capture_screenshot(page, "After List Creation")

    # Add assertions to verify if the list was created successfully, such as checking for a success message

    browser.close()


@allure.feature("Create New List")
def test_create_list_screenplay_playwright():
    browser, page = get_playwright_driver(headless=False)
    
    actor = Actor("Tester", page)

    page.goto("https://www.themoviedb.org/login")
    actor.attempts_to(LoginTaskPlaywright(os.getenv("USERNAME"), os.getenv("PASSWORD")))
    time.sleep(2)

    with allure.step("Open Create List Page"):
        page.goto("https://www.themoviedb.org/list/new")  # Replace with the actual create list page URL
        capture_screenshot(page, "Create List Page Loaded")

    with allure.step("Create a new list"):
        actor.attempts_to(CreateListTaskPlaywright("My Favorite Movies", "A list of my all-time favorite movies."))
        capture_screenshot(page, "After List Creation")

    # Add assertions to verify if the list was created successfully, such as checking for a success message

    browser.close()
