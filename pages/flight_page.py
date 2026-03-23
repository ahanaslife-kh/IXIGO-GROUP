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

    def open_flights_tab(self):
        self.click_element(self.FLIGHTS_TAB)

    def select_from_city(self, city):
        self.click_element(self.FROM_INPUT)

        active_input = self.wait_for_visibility((By.XPATH, "//input"))
        active_input.clear()
        active_input.send_keys(city)

        option_xpath = f"(//span[contains(@class,'block truncate') and contains(.,'{city}')])[1]"

        for _ in range(3):
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, option_xpath))
                ).click()
                break
            except StaleElementReferenceException:
                continue

    def select_to_city(self, city):
        to_label = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='To']"))
        )
        self.driver.execute_script("arguments[0].click();", to_label)

        active_input = self.driver.switch_to.active_element
        active_input.clear()
        active_input.send_keys(city)

        option_xpath = f"(//span[contains(.,'{city}')])[1]"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()

    def select_date(self):
        self.click_element(self.DATE_PICK)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@class,'react-calendar')]")
        ))

        date = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//abbr[text()='22']")
        ))
        date.click()

        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

    def select_travel_class(self, travel_class):
        wait = WebDriverWait(self.driver, 10)

        pax = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p[@data-testid='pax']")
        ))
        pax.click()

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[text()='{travel_class}']")
        )).click()

    def click_search(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )

        try:
            btn.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", btn)

    def wait_for_results_to_load(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'flight-card')]")
            )
        )