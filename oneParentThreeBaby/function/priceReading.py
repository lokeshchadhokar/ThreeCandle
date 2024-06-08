from oneParentThreeBaby.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class Action:
    @staticmethod
    def actionchain(driver):
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

        return open_close