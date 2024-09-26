import allure

def capture_screenshot(driver, step_name="Screenshot"):
    """Captures a screenshot and attaches it to the Allure report."""
    allure.attach(driver.get_screenshot_as_png(), name=step_name, attachment_type=allure.attachment_type.PNG)

def log_step(step_description):
    """Logs a step in Allure reports."""
    allure.step(step_description)
