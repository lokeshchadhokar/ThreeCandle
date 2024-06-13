from oneParentThreeBaby.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from oneParentThreeBaby.function.priceReading import Action
from oneParentThreeBaby.pages.DashBoard_page import DashBoard_locators
# Define a function to find and print elements based on their text content

a=Action
class currency_pairs(BasePage):
    def find_currency_pair(self,text):
        print("Account select currency from function".center(60, "-"))
        # print("Auto Selection currency")
        D= DashBoard_locators(self.driver)
        D.currency_selector()

        locat = (By.XPATH, f"//div[contains(text(), '{text}')]")
        # locat = (By.XPATH, f"//span[contains(text(), '{text}')]")#for saturday and sunday
        try:
            self.wait_for_1sec(locat)
            self.driver.find_element(By.XPATH, f"//div[contains(text(), '{text}')]").click()
            # self.driver.find_element(By.XPATH, f"//span[contains(text(), '{text}')]").click()# for saterday and sunday
            print(f"Found element for {text}:")

            value = a.actionchain_withtime(self.driver,text)
            print("Account select currency End".center(60, "="))
            return value,text
        except Exception as e:
            D.select10minPeriod()
            print(f"Could not find element for {text}") #{e}")


    def find_currency_pair_Three_values(self, text):
        print("Account select currency from function".center(60, "-"))
        # print("Auto Selection currency")
        D = DashBoard_locators(self.driver)
        D.currency_selector()

        locat = (By.XPATH, f"//div[contains(text(), '{text}')]")
        # locat = (By.XPATH, f"//span[contains(text(), '{text}')]")#for saturday and sunday
        try:
            self.wait_for_1sec(locat)
            self.driver.find_element(By.XPATH, f"//div[contains(text(), '{text}')]").click()
            # self.driver.find_element(By.XPATH, f"//span[contains(text(), '{text}')]").click()# for saterday and sunday
            print(f"Found element for {text}:")

            value = a.actionchain_withtime_three_candle_data_at_time(self.driver, text)
            print("Account select currency End".center(60, "="))
            return value, text
        except Exception as e:
            D.select10minPeriod()
            print(f"Could not find element for {text}")  # {e}")

