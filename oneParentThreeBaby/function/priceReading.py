from oneParentThreeBaby.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import datetime
from oneParentThreeBaby.strategy.dict_value_arranger import valueDistribute

class Action:
    @staticmethod
    def actionchain(driver):
        print("Price reading from function".center(60, "-"))
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
    def actionchain_withtime(driver, text):
        print("Price reading from function".center(60, "-"))
        base_page = BasePage(driver)
        d = datetime.datetime.now()
        H = d.strftime('%H')
        m = int(d.strftime('%M'))  # -1

        price_values_xpath = (By.XPATH, '//div[@class="sc-eRjRog jVyewk"]/table/tbody/tr/td')
        time_str = f"{H}:{m:02d}"
        print(f"Searching for time element: {time_str}")
        loc = (By.XPATH, f"//div[@class='sc-cyVxgd cVSasU' and text()='{time_str}']")
        by_time = base_page.wait_for_element(loc)
        ac = ActionChains(driver)
        ac.move_to_element(by_time).perform()
        driver.save_screenshot(f'{text}screenshot.png')
        with_time = base_page.wait_for_elements(price_values_xpath)
        print("Price reading End".center(60, "="))
        return with_time

    @staticmethod
    def get_candle_data_at_time(driver, time_str, price_values_xpath):
        base_page = BasePage(driver)
        loc = (By.XPATH, f"//div[@class='sc-cyVxgd cVSasU' and text()='{time_str}']")
        by_time = base_page.wait_for_element(loc)
        ac = ActionChains(driver)
        ac.move_to_element(by_time).perform()
        candle_data = base_page.wait_for_elements(price_values_xpath)
        return valueDistribute.arrangeValues_Three_time(candle_data, time_str)

    @staticmethod
    def actionchain_withtime_three_candle_data_at_time(driver, text):
        base_page = BasePage(driver)
        d = datetime.datetime.now()
        H = d.strftime('%H')
        m1 = int(d.strftime('%M')) - 2  # two minutes earlier
        m2 = int(d.strftime('%M')) - 1  # one minute earlier
        m3 = int(d.strftime('%M'))  # current time

        price_values_xpath = (By.XPATH, '//div[@class="sc-eRjRog jVyewk"]/table/tbody/tr/td')
        time_str1 = f"{H}:{m1:02d}"
        time_str2 = f"{H}:{m2:02d}"
        time_str3 = f"{H}:{m3:02d}"

        candle1 = Action.get_candle_data_at_time(driver, time_str1, price_values_xpath)
        candle2 = Action.get_candle_data_at_time(driver, time_str2, price_values_xpath)
        candle3 = Action.get_candle_data_at_time(driver, time_str3, price_values_xpath)

        print("openClose compare c1,2", float(candle1["Open"]) == float(candle2["Open"]) and float(candle1["Close"]) == float(candle2["Close"]))
        print("c2 c3", float(candle2["Open"]) == float(candle3["Open"]) and float(candle2["Close"]) == float(candle3["Close"]))

        if len(candle1) == 0 or (float(candle1["Open"]) == float(candle2["Open"]) and float(candle1["Close"]) == float(candle2["Close"])) or (float(candle2["Open"]) == float(candle3["Open"]) and float(candle2["Close"]) == float(candle3["Close"])):
            print(f"Candle1 ={candle1} \n Candle2 ={candle2}\n Candle3 ={candle3}")
            print("1No price values found DUPLICATE, retrying...")
            candle1, candle2, candle3 = Action.actionchain_withtime_three_candle_data_at_time(driver, text)  # Retry fetching the elements

        print("Price reading End".center(60, "="))
        return candle1, candle2, candle3
