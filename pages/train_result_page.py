import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TrainResultPage(BasePage):


    RESULT_DATES = (
        By.XPATH,
        "//div[@aria-label='Available dates']/button"
    )

    TATKAL_FILTER = (By.XPATH, "//p[text()='Tatkal Only']")
    BEST_AVAILABLE_FILTER = (By.XPATH, "//p[text()='Best Available']")
    AC_ONLY_FILTER = (By.XPATH, "//p[text()='AC Only']")

    TRAIN_LIST = (By.CSS_SELECTOR, "#train-card-list>div")

    COACH_LIST = (By.CSS_SELECTOR, "#tg-available-row>div")

    QUOTA_TABS = (By.CSS_SELECTOR, "button[role='tab']")

    QUOTA_DATES = (By.CSS_SELECTOR, "div[role='tabpanel']>div")

    BOOK_BUTTON = (By.TAG_NAME,"button")

    RESULTS_SECTION = (By.ID, "train-card-list")
    LOGIN_CROSS=(By.CSS_SELECTOR,"div[role='dialog']>div svg[data-testid='CloseIcon']")



    def select_result_date(self, date_text):
        self.logger.info(f"Selecting result date: {date_text}")
        dates = self.get_elements(self.RESULT_DATES)
        for d in dates:
            if date_text in d.text:
                self.logger.info(f"Result date found: {d.text}")
                d.click()
                time.sleep(1)
                return True
        self.logger.warning(f"Result date not found: {date_text}")
        return False

    def apply_filters(self):

        self.logger.info("Applying filters")

        # Check if Tatkal filter is present
        if self.is_element_present(self.TATKAL_FILTER):
            self.logger.info("Tatkal filter present → Clicking Tatkal")
            self.click_element(self.TATKAL_FILTER)
            return "Tatkal applied"

        # If Tatkal not present, apply both Best Available and AC Only
        else:
            self.logger.info("Tatkal not present → Applying Best Available and AC Only")

            if self.is_element_present(self.BEST_AVAILABLE_FILTER):
                self.logger.info("Clicking Best Available filter")
                self.click_element(self.BEST_AVAILABLE_FILTER)

            if self.is_element_present(self.AC_ONLY_FILTER):
                self.logger.info("Clicking AC Only filter")
                self.click_element(self.AC_ONLY_FILTER)

            return "Best Available and AC Only applied"

    def scroll_to_results(self):
        self.logger.info("Scrolling to train results section")
        self.scroll_into_view(self.RESULTS_SECTION)

    def select_train(self, train_name):
        self.logger.info(f"Selecting train: {train_name}")
        trains = self.get_elements(self.TRAIN_LIST)
        for train in trains:
            if train_name in train.text:
                self.logger.info(f"Train found: {train.text}")
                print(train.text)
                time.sleep(1)
                return True
        self.logger.warning(f"Train not found: {train_name}")
        return False

    def select_coach(self, coach_name):
        self.logger.info(f"Selecting coach: {coach_name}")
        coaches = self.get_elements(self.COACH_LIST)
        for coach in coaches:
            if coach_name in coach.text:
                self.logger.info(f"Coach found: {coach.text}")
                coach.click()
                time.sleep(1)
                return True
        self.logger.warning(f"Coach not found: {coach_name}")
        return False

    def select_quota(self, quota_name):
        self.logger.info(f"Selecting quota: {quota_name}")
        quotas = self.get_elements(self.QUOTA_TABS)
        for q in quotas:
            if quota_name in q.text:
                self.logger.info(f"Quota found: {q.text}")
                q.click()
                time.sleep(1)
                return True
        self.logger.warning(f"Quota not found: {quota_name}")
        return False

    def select_quota_date(self, date_text):
        self.logger.info(f"Selecting quota date: {date_text}")
        dates = self.get_elements(self.QUOTA_DATES)
        for d in dates:
            if date_text in d.text:
                self.logger.info(f"Quota date found: {d.text}")
                print(d.text)
                return True
        self.logger.warning(f"Quota date not found: {date_text}")
        return False

    def select_quota_date_and_book(self, date_text):
        self.logger.info(f"Searching quota date containing: {date_text}")

        dates = self.get_elements(self.QUOTA_DATES)

        for d in dates:
            if date_text in d.text:
                self.logger.info(f"Quota date found: {d.text}")
                print(d.text)

                # Click BOOK button after date is found
                self.logger.info("Clicking Book button")
                self.click_element(self.BOOK_BUTTON)

                return True

        self.logger.warning(f"Quota date not found: {date_text}")
        return False

    def click_book(self):
        self.logger.info("Clicking Book button")
        self.click_element(self.BOOK_BUTTON)
    def close_login(self):
        self.logger.info("Closing login page")
        self.click_element(self.LOGIN_CROSS)