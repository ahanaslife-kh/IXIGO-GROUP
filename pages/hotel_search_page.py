import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from pages.hotel_detail_page import HotelDetailPage

class HotelSearchPage(BasePage):

    #POPUP_CLOSE = (By.XPATH, "//div[@data-testid='bpg-home-modal-close']")
    HOTEL_CARDS = (By.XPATH, "//h2[@data-testid='hotel-name']")
    FIRST_HOTEL = (By.XPATH, "(//h2[@data-testid='hotel-name'])[1]")
    COUPLE_FRIENDLY = (By.XPATH, "//div/p[contains(text(),'Couple Friendly')]")
    USER_RATING = (By.XPATH, "//div/p[contains(text(),'Very Good: 7+')]")
    PARKING_FACILITY = (By.XPATH, "//div/p[contains(text(),'Parking')]")
    STAR_RATING = (By.XPATH, "//span[contains(text(),'3 Star')]")
    SORT_BOX = (By.XPATH, "(//p[@class='body-md truncate text-primary'])[1]")
    SORT_LOW2HIGH = (By.XPATH,"//p[contains(text(),'Low to High')]")
    SORT_HIGH_TO_LOW =(By.XPATH,"//p[contains(text(),'High to Low')]")
    PRICE_ELEMENTS = (By.XPATH, "//div[@class='h5 text-right text-primary font-medium']")
    CLEAR_FILTER = (By.XPATH, "//button[contains(text(),'Clear All')]")

    # def close_popup_if_present(self):
    #     try:
    #         close_btn = self.wait.until(
    #             EC.element_to_be_clickable(self.POPUP_CLOSE)
    #         )
    #         close_btn.click()
    #     except TimeoutException:
    #         # Popup not present — continue normally
    #         pass
    #
    # def close_popup(self):
    #     element = self.scroll_to_element(self.POPUP_CLOSE)
    #     self.wait.until(EC.element_to_be_clickable(self.POPUP_CLOSE))
    #     element.click()


    def wait_for_results(self):
        time.sleep(5)
        self.wait.until(
            EC.presence_of_all_elements_located(self.HOTEL_CARDS)
        )

    def get_hotel_count(self):
        hotels = self.wait.until(
            EC.presence_of_all_elements_located(self.HOTEL_CARDS)
        )
        return len(hotels)

    # def apply_couple_friendly(self):
    #     # element = self.wait.until(EC.element_to_be_clickable(self.COUPLE_FRIENDLY))
    #     # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    #     # element.click()
    #
    #     element = self.scroll_to_element(self.COUPLE_FRIENDLY)
    #     self.wait.until(EC.element_to_be_clickable(self.COUPLE_FRIENDLY))
    #     element.click()

    def apply_couple_friendly(self):
        element = self.wait.until(EC.element_to_be_clickable(self.COUPLE_FRIENDLY))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        element.click()
        self.wait_for_results()

    # def apply_user_rating(self):
    #     element = self.wait.until(EC.element_to_be_clickable(self.USER_RATING))
    #     self.driver.execute_script(
    #         "arguments[0].scrollIntoView({block: 'center'});",
    #         element
    #     )
    #     element.click()
    #     self.wait_for_results()

    def apply_user_rating(self):
        element = self.wait.until(EC.element_to_be_clickable(self.USER_RATING))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        element.click()
        self.wait_for_results()

    # def apply_parking_facility(self):
    #     element = self.wait.until(EC.element_to_be_clickable(self.PARKING_FACILITY))
    #     self.driver.execute_script(
    #         "arguments[0].scrollIntoView({block: 'center'});",
    #         element
    #     )
    #     element.click()
    #     self.wait_for_results()

    def apply_parking_facility(self):
        element = self.wait.until(EC.element_to_be_clickable(self.PARKING_FACILITY))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        element.click()
        self.wait_for_results()

    def apply_star_rating(self):
        element = self.wait.until(EC.element_to_be_clickable(self.STAR_RATING))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        element.click()
        self.wait_for_results()


    # def apply_user_rating(self):
    #     element = self.scroll_to_element(self.USER_RATING)
    #     self.wait.until(EC.element_to_be_clickable(self.USER_RATING))
    #     element.click()

    # def apply_parking_facility(self):
    #     element = self.scroll_to_element(self.PARKING_FACILITY)
    #     self.wait.until(EC.element_to_be_clickable(self.PARKING_FACILITY))
    #     element.click()

    # def sort_by_price_low(self):
    #     self.driver.execute_script("window.scrollTo(0, 0);")
    #     self.wait.until(EC.element_to_be_clickable(self.SORT_BOX)).click()
    #     self.wait.until(EC.element_to_be_clickable(self.SORT_LOW2HIGH)).click()
    #     self.wait.until(EC.presence_of_all_elements_located(self.HOTEL_CARDS))

    # def sort_by_price_low(self):
    #     self.driver.execute_script("window.scrollTo(0, 0);")
    #
    #     sort_box = self.wait.until(
    #         EC.element_to_be_clickable(self.SORT_BOX)
    #     )
    #     self.driver.execute_script("arguments[0].click();", sort_box)
    #
    #     low_option = self.wait.until(
    #         EC.element_to_be_clickable(self.SORT_LOW2HIGH)
    #     )
    #     self.driver.execute_script("arguments[0].click();", low_option)
    #
    #     old_element = self.driver.find_elements(*self.HOTEL_CARDS)[0]
    #     self.wait.until(EC.staleness_of(old_element))
    #     self.wait_for_results()

    def sort_by_price_low(self):
        self.wait_for_results()

        sort_box = self.wait.until(
            EC.presence_of_element_located(self.SORT_BOX)
        )

        self.driver.execute_script("arguments[0].click();", sort_box)

        low_option = self.wait.until(
            EC.presence_of_element_located(self.SORT_LOW2HIGH)
        )

        self.driver.execute_script("arguments[0].click();", low_option)

        self.wait_for_results()

    # def sort_by_price_low(self):
    #     # Locate sort box
    #     sort_box = self.wait.until(
    #         EC.presence_of_element_located(self.SORT_BOX)
    #     )
    #
    #     # Scroll element into center of screen
    #     self.driver.execute_script(
    #         "arguments[0].scrollIntoView({block: 'center'});",
    #         sort_box
    #     )
    #
    #     # Small wait for layout stabilization
    #     self.wait.until(EC.element_to_be_clickable(self.SORT_BOX))
    #
    #     # Use JS click (bypass interception)
    #     self.driver.execute_script("arguments[0].click();", sort_box)
    #
    #     # Click low to high
    #     low_option = self.wait.until(
    #         EC.element_to_be_clickable(self.SORT_LOW2HIGH)
    #     )
    #
    #     self.driver.execute_script("arguments[0].click();", low_option)
    #
    #     # Wait for results to refresh
    #     old_element = self.driver.find_elements(*self.HOTEL_CARDS)[0]
    #     self.wait.until(EC.staleness_of(old_element))
    #
    #     self.wait_for_results()








    # def click_book_now(self):
    #     # hotels = self.wait.until(EC.presence_of_all_elements_located(self.FIRST_HOTEL))
    #     # # if not hotels:
    #     # #     raise Exception("No hotels found on search page")
    #     # hotels.click()
    #     # element = self.scroll_to_element(self.BOOK_NOW)
    #     element = self.driver.find_element(self.BOOK_NOW)
    #     element.click()

    # def click_book_now(self):
    #
    #     buttons = self.wait.until(
    #         EC.presence_of_all_elements_located(self.BOOK_NOW)
    #     )
    #
    #     for btn in buttons:
    #         if btn.is_displayed():
    #             self.driver.execute_script(
    #                 "arguments[0].scrollIntoView({block:'center'});",
    #                 btn
    #             )
    #             self.driver.execute_script("arguments[0].click();", btn)
    #             break
    #it worked

    # def click_first_hotel(self):
    #     hotel = self.wait.until(
    #         EC.element_to_be_clickable(self.FIRST_HOTEL)
    #     )
    #
    #     hotel.click()

    def open_first_hotel(self):
        hotel_element = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_HOTEL)
        )
        hotel_name = hotel_element.text.strip()
        hotel_element.click()
        self.switch_to_new_tab()
        return HotelDetailPage(self.driver), hotel_name

    def sort_by_price_high(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_BOX)
        )
        dropdown.click()

        high_option = self.wait.until(
            EC.element_to_be_clickable(self.SORT_HIGH_TO_LOW)
        )
        high_option.click()

        self.wait_for_results()

    def get_all_prices(self):
        price_elements = self.wait.until(
            EC.presence_of_all_elements_located(self.PRICE_ELEMENTS)
        )
        prices = []
        for price in price_elements:
            amount = price.text.replace("₹", "").replace(",", "").strip()
            if amount.isdigit():
                prices.append(int(amount))

        return prices

    def clear_all_filters(self):
        element = self.wait.until(EC.element_to_be_clickable(self.CLEAR_FILTER))
        element.click()
        self.wait_for_results()



    # def click_book_now(self):
    #     # Scroll to book now
    #     book_btn = self.wait.until(
    #         EC.presence_of_element_located(self.BOOK_NOW)
    #     )
    #
    #     self.driver.execute_script(
    #         "arguments[0].scrollIntoView({block: 'center'});",
    #         book_btn
    #     )
    #
    #     # Wait until clickable
    #     self.wait.until(
    #         EC.element_to_be_clickable(self.BOOK_NOW)
    #     )
    #
    #     # Use JS click (safer on Ixigo)
    #     self.driver.execute_script("arguments[0].click();", book_btn)

