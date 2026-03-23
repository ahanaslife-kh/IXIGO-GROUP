from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):

    HOTELS_TAB = (By.XPATH, "(//p[text()='Hotels'])[2]")
    CITY_INPUT = (By.XPATH, "//input[@placeholder='Enter city, area or property name']")
    FIRST_CITY = (By.CSS_SELECTOR, "div.flex.min-w-0.items-center.gap-10")
    CALENDAR_DATES = (By.CSS_SELECTOR, "button.react-calendar__tile")
    ROOM_GUEST_BTN = (By.XPATH, "//p[@data-testid='adult-increment']")
    SEARCH_BTN = (By.XPATH, "//div[@class='flex items-center gap-5 font-medium']")

    def open_hotels(self):
        self.driver.find_element(*self.HOTELS_TAB).click()

    def enter_city(self, city):
        city_input = self.wait.until(EC.visibility_of_element_located(self.CITY_INPUT))
        city_input.clear()
        city_input.send_keys(city)

        cities = self.wait.until(EC.presence_of_all_elements_located(self.FIRST_CITY))
        if not cities:
            raise Exception("No city suggestions appeared")

        cities[0].click()

    def select_date(self, day, month, year):
        target = f"{month} {day}, {year}"

        dates = self.wait.until(EC.presence_of_all_elements_located(self.CALENDAR_DATES))
        for date in dates:
            try:
                abbr = date.find_element(By.TAG_NAME, "abbr")
                if target in abbr.get_attribute("aria-label"):
                    date.click()
                    return
            except:
                continue

        raise Exception(f"Date not found: {target}")

    def select_guests(self):
        self.wait.until(EC.element_to_be_clickable(self.ROOM_GUEST_BTN)).click()

    def search(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN)).click()

    def close_popup_if_present(self):
        try:
            close_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@data-testid='bpg-home-modal-close']")
                )
            )
            close_btn.click()
        except:
            pass