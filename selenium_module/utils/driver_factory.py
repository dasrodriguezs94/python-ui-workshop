from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def get_selenium_driver(browser="chrome"):
    """Initializes and returns a WebDriver instance based on the specified browser."""
    if browser.lower() == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")

    driver.maximize_window()
    return driver
