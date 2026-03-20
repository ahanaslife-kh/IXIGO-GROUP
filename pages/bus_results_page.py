from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BusResultsPage(BasePage):

    RESULT_TEXT = (By.XPATH, "//span[contains(text(),'Showing')]")

    SORT_DEPARTURE = (By.XPATH, "//span[text()='Departure Time']")

    # Sort
    SORT_PRICE = (By.XPATH, "//span[text()='Price']")

    # Filters
    AC_FILTER = (By.XPATH, "//span[text()='AC']")

    FIRST_SHOW_SEATS = (
        By.XPATH,
        "(//button[contains(.,'Show Seats')])[1]"
    )

    # Seat container
    AVAILABLE_SEATS = (
        By.XPATH,
        "//button[contains(@class,'seat') and not(contains(@class,'booked'))]"
    )

    # Boarding & Dropping lists
    BOARDING_OPTIONS = (
        By.XPATH,
        "//div[contains(@id,'place-container')]//input[@type='checkbox']"
    )

    DROPPING_OPTIONS = (
        By.XPATH,
        "//div[contains(@id,'place-container')]//input[@type='checkbox']"
    )

    CONTINUE_BTN = (
        By.XPATH,
        "//button[contains(.,'Continue')]"
    )

    # Seat container (used for validation)
    SEAT_CONTAINER = (By.XPATH, "//button[contains(@class,'seat')]")

    def results_visible(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.RESULT_TEXT)
            )
            return True
        except:
            return False

    def sort_by_price(self):
        self.click_element(self.SORT_PRICE)

    def apply_ac_filter(self):
        self.click_element(self.AC_FILTER)

    def click_show_seats(self):
        buttons = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[contains(.,'Show Seats')]"))
        )

        for btn in buttons:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)

                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(btn)
                )

                self.driver.execute_script("arguments[0].click();", btn)

                #  wait for seat layout to load
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(self.SEAT_CONTAINER)
                )

                print(" Show seats clicked")
                return

            except:
                continue

        raise Exception(" No bus found to open seats")

    def select_any_available_seat(self):
        for i in range(5):
            try:
                seats = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_all_elements_located(self.AVAILABLE_SEATS)
                )

                if len(seats) == 0:
                    continue

                seat = seats[0]  #  ONLY FIRST SEAT

                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", seat
                )

                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(seat)
                )

                self.driver.execute_script("arguments[0].click();", seat)

                print(" Seat selected")
                return

            except Exception as e:
                print(f"Retry seat selection {i + 1}: {e}")

        raise Exception(" Seat not selected")

    def continue_button_clickable(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.CONTINUE_BTN)
            )
            return True
        except:
            return False

    def select_boarding_point(self):
        try:
            # If already selected (card visible)
            selected = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[contains(text(),'Boarding Point')]")
                )
            )
            print("Boarding already selected")
            return

        except:
            print(" Boarding not auto-selected, trying manual selection")

        # fallback (if checkbox UI appears)
        try:
            options = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((
                    By.XPATH, "//input[@type='checkbox']"
                ))
            )

            if options:
                self.driver.execute_script("arguments[0].click();", options[0])
                print("Boarding selected manually")

        except:
            raise Exception("Boarding not found")

    def select_dropping_point(self):
        try:
            # Check if already selected
            selected = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[contains(text(),'Dropping Point')]")
                )
            )
            print("Dropping already selected")
            return

        except:
            print(" Dropping not auto-selected, trying manual")

        # fallback (only if checkbox UI appears)
        try:
            options = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((
                    By.XPATH, "//input[@type='checkbox']"
                ))
            )

            if options:
                self.driver.execute_script("arguments[0].click();", options[0])
                print(" Dropping selected manually")

        except:
            raise Exception(" Dropping not found")

    def click_continue(self):

        for i in range(5):
            try:
                btn = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(self.CONTINUE_BTN)
                )

                # Scroll properly
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", btn
                )

                # Small wait for React render (IMPORTANT)
                WebDriverWait(self.driver, 2).until(
                    lambda d: btn.is_displayed()
                )

                # FORCE CLICK (bypass all Selenium checks)
                self.driver.execute_script("arguments[0].click();", btn)

                print("Continue clicked")
                return

            except Exception as e:
                print(f"Retry continue click {i + 1}: {e}")

        raise Exception("Continue button click failed")

    def continue_button_visible(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.CONTINUE_BTN)
            )
            return True
        except:
            return False

    def sort_by_departure(self):
        self.click_element(self.SORT_DEPARTURE)


    def seats_visible(self):
        try:
            self.wait_for_visibility(self.SEAT_CONTAINER, timeout=20)
            return True
        except:
            return False
