from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.default_timeout = timeout

    def wait_for_visibility(self, locator, timeout=None):
        wait_time = timeout if timeout else self.default_timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=None):
        wait_time = timeout if timeout else self.default_timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(locator)
        )