from oneParentThreeBaby.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from oneParentThreeBaby.function.priceReading import Action
from oneParentThreeBaby.pages.DashBoard_page import DashBoard_locators
# Define a function to find and print elements based on their text content

a=Action
class currency_pairs(BasePage):
    def find_currency_pair(self,text):
        # print("Auto Selection currency")
        D= DashBoard_locators(self.driver)
        D.currency_selector()

        # locat = (By.XPATH, f"//div[contains(text(), '{text}')]")
        locat = (By.XPATH, f"//span[contains(text(), '{text}')]")#for saturday and sunday
        try:
            self.wait_for_1sec(locat)
            # self.driver.find_element(By.XPATH, f"//div[contains(text(), '{text}')]").click()
            self.driver.find_element(By.XPATH, f"//span[contains(text(), '{text}')]").click()# for saterday and sunday
            print(f"Found element for {text}:")

            value = a.actionchain(self.driver)
            return value,text
        except Exception as e:
            D.select1H_SmallPeriod()
            print(f"Could not find element for {text}") #{e}")


