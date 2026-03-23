import time
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException
)

# --------------------------------------------------
# Retry clicking on flaky elements
# --------------------------------------------------

def retry_click(element, retries=3, delay=1):
    """
    Retries clicking an element in case of stale or intercepted exceptions.
    """
    for attempt in range(retries):
        try:
            element.click()
            return True
        except (StaleElementReferenceException,
                ElementClickInterceptedException):
            time.sleep(delay)
    return False



def wait_seconds(seconds):
    time.sleep(seconds)
