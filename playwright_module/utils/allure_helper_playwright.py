import allure

def capture_screenshot(page, step_name="Screenshot"):
    """Captures a screenshot of the current state of the page and attaches it to the Allure report."""
    screenshot = page.screenshot()
    allure.attach(screenshot, name=step_name, attachment_type=allure.attachment_type.PNG)

def log_step(step_description):
    """Logs a custom step in Allure reports."""
    allure.step(step_description)
