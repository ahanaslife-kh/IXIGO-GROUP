

import time
from selenium.common import StaleElementReferenceException, ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.logger = get_logger()

    # ---------- WAIT METHODS ----------

    def wait_for_visibility(self, locator, timeout=15):
        self.logger.info(f"Waiting for visibility of element: {locator}")
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=15):
        self.logger.info(f"Waiting for element to be clickable: {locator}")
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    # ---------- ACTION METHODS ----------

    def click_element(self, locator, timeout=15):
        for attempt in range(3):
            try:
                element = self.wait_for_clickable(locator, timeout)

                # Scroll into view
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", element
                )

                self.logger.info(f"Clicking element: {locator}")

                try:
                    element.click()
                except ElementClickInterceptedException:
                    self.logger.warning("Normal click failed, using JS click fallback")
                    self.driver.execute_script("arguments[0].click();", element)

                return

            except StaleElementReferenceException:
                self.logger.warning("Retrying click due to stale element...")
                time.sleep(1)

        raise Exception(f"Unable to click element after retries: {locator}")

    def enter_text(self, locator, text, timeout=15):
        for attempt in range(3):
            try:
                element = self.wait_for_visibility(locator, timeout)
                self.logger.info(f"Entering text '{text}' into: {locator}")
                element.clear()
                element.send_keys(text)
                return

            except StaleElementReferenceException:
                self.logger.warning("Retrying send_keys due to stale element...")
                time.sleep(1)

        raise Exception(f"Unable to enter text after retries: {locator}")

    # ---------- UTILITY METHODS ----------

    def get_element_text(self, locator, timeout=15):
        element = self.wait_for_visibility(locator, timeout)
        text = element.text
        self.logger.info(f"Text from {locator}: {text}")
        return text

    def scroll_into_view(self, locator):
        element = self.wait_for_visibility(locator)
        self.logger.info(f"Scrolling to element: {locator}")
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        return element

    def js_click(self, locator):
        self.logger.warning(f"Using JS click for: {locator}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @staticmethod
    def validate_text(actual, expected):
        logger = get_logger()
        logger.info(f"Validating text. Expected: {expected} | Actual: {actual}")
        assert expected in actual, f"Expected '{expected}' not found in '{actual}'"