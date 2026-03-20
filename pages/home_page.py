from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.logger import get_logger


class FlightsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger()

    # Locators
    FLIGHTS_TAB = (By.XPATH, "//p[@class='body-sm text-xl text-primary']")
    FROM_INPUT = (By.XPATH, "//span[text()='From']")
    TO_INPUT = (By.XPATH, "//span[text()='To']/ancestor::div[1]")
    DATE_PICK = (By.XPATH, "//p[@data-testid='departureDate']")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(.,'Search')]")

    # ---------------- POPUP HANDLING ----------------
    def remove_popup_overlay(self):
        self.logger.info("Removing popup overlay if present")
        self.driver.execute_script("""
            let backdrop = document.querySelector('.abrs-backdrop');
            if (backdrop) backdrop.remove();

            let iframe = document.querySelector('#sso-frame');
            if (iframe) iframe.remove();
        """)

    def close_login_popup_if_present(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.frame_to_be_available_and_switch_to_it((By.ID, "sso-frame"))
            )

            close_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'close')]"))
            )
            close_btn.click()

            self.driver.switch_to.default_content()
        except:
            self.driver.switch_to.default_content()

        self.remove_popup_overlay()

    # ---------------- ACTIONS ----------------

    def open_flights_tab(self):
        self.logger.info("Opening Flights tab")
        self.click_element(self.FLIGHTS_TAB)

    def select_from_city(self, city):
        self.logger.info(f"Selecting FROM city: {city}")
        self.click_element(self.FROM_INPUT)

        active_input = self.wait_for_visibility((By.XPATH, "//input"))
        active_input.clear()
        active_input.send_keys(city)

        option_xpath = f"(//span[contains(@class,'block truncate') and contains(.,'{city}')])[1]"

        for _ in range(3):
            try:
                option = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, option_xpath))
                )
                option.click()
                break
            except StaleElementReferenceException:
                self.logger.warning("Retrying FROM city selection")

        self.driver.find_element(By.TAG_NAME, "body").click()

    def select_to_city(self, city):
        self.logger.info(f"Selecting TO city: {city}")

        to_label = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='To']"))
        )
        self.driver.execute_script("arguments[0].click();", to_label)

        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.activeElement.tagName") == "INPUT"
        )

        active_input = self.driver.switch_to.active_element
        active_input.clear()
        active_input.send_keys(city)

        option_xpath = f"(//div[contains(@class,'overflow-y-scroll')]//span[contains(.,'{city}')])[1]"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()

        self.driver.find_element(By.TAG_NAME, "body").click()

    def select_date(self):
        self.logger.info("Selecting travel date")

        self.click_element(self.DATE_PICK)

        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'react-calendar')]")
        ))

        date = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'react-calendar')]//abbr[text()='22']")
        ))
        date.click()

        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

    def select_travel_class(self, travel_class):
        self.logger.info(f"Selecting travel class: {travel_class}")

        wait = WebDriverWait(self.driver, 15)

        pax = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p[@data-testid='pax']")
        ))
        pax.click()

        option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[normalize-space()='{travel_class}']")
        ))
        option.click()

        done_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Done']")
        ))
        done_btn.click()

    def click_search(self):
        self.logger.info("Clicking search button")

        self.close_login_popup_if_present()

        search_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", search_btn
        )

        try:
            search_btn.click()
        except ElementClickInterceptedException:
            self.logger.warning("Normal click failed, using JS click")
            self.driver.execute_script("arguments[0].click();", search_btn)

    def wait_for_results_to_load(self):
        self.logger.info("Waiting for flight results")
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'flight-card')]")
            )
        )