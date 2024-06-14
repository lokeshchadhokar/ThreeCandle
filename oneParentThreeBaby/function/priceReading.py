from oneParentThreeBaby.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import datetime
from oneParentThreeBaby.strategy.dict_value_arranger import valueDistribute


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
    def actionchain_withtime(driver,text):
        print("Price reading from functon".center(60, "-"))
        base_page = BasePage(driver)
        d = datetime.datetime.now()
        H = d.strftime('%H')
        m = int(d.strftime('%M'))#-1
        price_values_xpath = (By.XPATH, '//div[@class="sc-eRjRog jVyewk"]/table/tbody/tr/td')
        time_str = f"{H}:{m:02d}"
        print(f"Searching for time element: {time_str}")
        loc =(By.XPATH, f"//div[@class='sc-cyVxgd cVSasU'and text()='{time_str}']")
        by_time = base_page.wait_for_element(loc)
        ac = ActionChains(driver)
        ac.move_to_element(by_time).perform()
        driver.save_screenshot(f'{text}screenshot.png')
        with_time = base_page.wait_for_elements(price_values_xpath)
        print("Price reading End".center(60, "="))
        return with_time

    @staticmethod
    def actionchain_withtime_three_candle_data_at_time(driver,text):
        # print("Price reading from functon".center(60, "-"))
        base_page = BasePage(driver)
        d = datetime.datetime.now()
        H = d.strftime('%H')
        m1 = int(d.strftime('%M')) - 2#two minute late
        m2 = int(d.strftime('%M')) - 1# one minute late
        m3 = int(d.strftime('%M'))# current time
        price_values_xpath = (By.XPATH, '//div[@class="sc-eRjRog jVyewk"]/table/tbody/tr/td')
        time_str1 = f"{H}:{m1:02d}"
        time_str2 = f"{H}:{m2:02d}"
        time_str3 = f"{H}:{m3:02d}"
        # print(f"Searching for time element: {time_str1}")
        # print(f"Searching for time element: {time_str2}")
        # print(f"Searching for time element: {time_str3}")
        loc1 = (By.XPATH, f"//div[@class='sc-cyVxgd cVSasU'and text()='{time_str1}']")
        loc2 = (By.XPATH, f"//div[@class='sc-cyVxgd cVSasU'and text()='{time_str2}']")
        loc3 =(By.XPATH, f"//div[@class='sc-cyVxgd cVSasU'and text()='{time_str3}']")
        by_time1 = base_page.wait_for_element(loc1)
        ac = ActionChains(driver)
        ac.move_to_element(by_time1).perform()
        candlee1 = base_page.wait_for_elements(price_values_xpath)
        candle1=valueDistribute.arrangeValues_Three_time(candlee1,time_str1)
        # print(f"candle1 :{candle1}")
        by_time2 = base_page.wait_for_element(loc2)
        bc = ActionChains(driver)
        bc.move_to_element(by_time2).perform()
        candlee2 = base_page.wait_for_elements(price_values_xpath)
        candle2 = valueDistribute.arrangeValues_Three_time(candlee2,time_str2)
        # print(f"candle2 :{candle2}")
        by_time3 = base_page.wait_for_element(loc3)
        cc = ActionChains(driver)
        cc.move_to_element(by_time3).perform()
        candlee3 = base_page.wait_for_elements(price_values_xpath)
        candle3 = valueDistribute.arrangeValues_Three_time(candlee3,time_str3)
        # print(f"candle3 :{candle3}")
        print("openClose compair",float(candle1["Open"])==float(candle2["Open"]) and float(candle1["Close"])==float(candle2["Close"]))
        # print("open", float(candle1["Open"]) ,float(candle2["Close"]))
        if len(candle1) == 0 or float(candle1["Open"])==float(candle2["Open"]) and float(candle1["Close"])==float(candle2["Close"]):
            print(f"Candle1 ={candle1} \n candle2 ={candle2}\n candle3 ={candle3}")
            print("1No price values found DUBLICATE, retrying...")
            candle1,candle2,candle3 = Action.actionchain_withtime_three_candle_data_at_time(driver,text)# Retry fetching the elements
        print("Price reading End".center(60, "="))

        return candle1,candle2,candle3