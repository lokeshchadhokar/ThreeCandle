from oneParentThreeBaby.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import datetime


class Action:
    @staticmethod
    def actionchain(driver):
        print("Price reading from functon".center(60, "-"))
        base_page = BasePage(driver)

        # XPath for the table cells containing price values
        price_values_xpath = (By.XPATH, '//div[@class="sc-eRjRog jVyewk"]/table/tbody/tr/td')

        # Wait for the "Opening of the trade" element and perform an action chain on it
        opening = base_page.wait_for_element((By.XPATH, "//span[text()='Opening of the trade']"))

        ac = ActionChains(driver)
        ac.move_to_element(opening).perform()
        # Wait for the elements that contain price values
        open_close = base_page.wait_for_elements(price_values_xpath)

        # Check if elements are found
        print("Number of price values found:", len(open_close))
        if len(open_close) == 0:
            print("No price values found, retrying...")
            open_close = Action.actionchain(driver)  # Retry fetching the elements
        print("Price reading End".center(60, "="))
        return open_close

    @staticmethod
    def actionchain_withtime(driver):
        print("Price reading from functon".center(60, "-"))
        base_page = BasePage(driver)
        d = datetime.datetime.now()
        H = d.strftime('%H')
        m = int(d.strftime('%M')) - 2
        price_values_xpath = (By.XPATH, '//div[@class="sc-eRjRog jVyewk"]/table/tbody/tr/td')
        time_str = f"{H}:{m:02d}"
        print(f"Searching for time element: {time_str}")
        loc =(By.XPATH, f"//div[@class='sc-cyVxgd cVSasU'and text()='{time_str}']")
        by_time = base_page.wait_for_element(loc)
        ac = ActionChains(driver)
        ac.move_to_element(by_time).perform()
        with_time = base_page.wait_for_elements(price_values_xpath)
        print("Price reading End".center(60, "="))
        return with_time