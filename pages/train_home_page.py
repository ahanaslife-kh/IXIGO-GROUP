from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TrainHomePage(BasePage):


    TRAINS_TAB = (By.CSS_SELECTOR, "div.mainContainer>div>div:nth-child(2) a[href='/trains']")

    ORIGIN_BOX = (By.CSS_SELECTOR, "div.mainContainer>div>div:nth-child(2) div[data-testid='search-form-origin']")
    ORIGIN_INPUT = (By.CSS_SELECTOR, "input[placeholder='Enter Origin']")

    DEST_BOX = (By.CSS_SELECTOR, "div.mainContainer>div>div:nth-child(2) div[data-testid='search-form-destination']")
    DEST_INPUT = (By.CSS_SELECTOR, "input[placeholder='Enter Destination']")

    SWAP_ICON = (By.CSS_SELECTOR, "div.mainContainer>div>div:nth-child(2) div[data-testid='swapIcon']")

    DAY_AFTER_TOMORROW = (
            By.CSS_SELECTOR,
            "div.mainContainer>div>div:nth-child(2) div[data-testid='day-after-tomorrow']")

    TOMORROW = (
            By.CSS_SELECTOR,
            "div.mainContainer>div>div:nth-child(2) div[data-testid='tomorrow']")

    CALENDAR_ICON = (
            By.CSS_SELECTOR,
            "div.mainContainer>div>div:nth-child(2) div[data-testid='search-form-calendar']")

    SEARCH_BUTTON = (
            By.CSS_SELECTOR,
            "div.mainContainer>div>div:nth-child(2) button[data-testid='book-train-tickets']")

    SUGGESTIONS = (By.CSS_SELECTOR, "div[role='listitem']")



    def open_trains_module(self):
        self.logger.info(f"Opening train module: {self.TRAINS_TAB}")
        self.click_element(self.TRAINS_TAB)

    def select_origin(self, prefix, city):
        self.logger.info(f"Select origin: {prefix}")
        self.click_element(self.ORIGIN_BOX)
        self.enter_text(self.ORIGIN_INPUT, prefix)
        self._select_city(city)

    def select_destination(self, prefix, city):
        self.logger.info(f"Select destination: {prefix}")
        self.click_element(self.DEST_BOX)
        self.enter_text(self.DEST_INPUT, prefix)
        self._select_city(city)

    def _select_city(self, city):
        self.logger.info(f"Select city: {city}")
        suggestions = self.get_elements(self.SUGGESTIONS)
        for item in suggestions:
            if city in item.text:
                item.click()
                break
    def swap_locations(self):
        self.logger.info(f"Swap locations: {self.SWAP_ICON}")
        self.click_element(self.SWAP_ICON)

    def select_quick_dates(self):
        self.logger.info("Select quick dates")
        self.click_element(self.DAY_AFTER_TOMORROW)
        self.click_element(self.TOMORROW)

    def open_calendar(self):
        self.logger.info(f"Opening calendar: {self.CALENDAR_ICON}")
        self.click_element(self.CALENDAR_ICON)

    def click_search(self):
        self.logger.info("Click search button")
        self.click_element(self.SEARCH_BUTTON)
