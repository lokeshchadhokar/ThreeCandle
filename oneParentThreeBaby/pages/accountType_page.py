from selenium.webdriver.common.by import By
from .base_page import BasePage


class accountType(BasePage):
    # account_type = driver.find_element(By.XPATH, "//div[@class='sc-csJRnm kQEjyJ']").click()
    account_type = (By.XPATH,"//div[@class='sc-csJRnm kQEjyJ']")
    # account_switch = driver.find_elements(By.CSS_SELECTOR, ".sc-emDGWR")
    types_of_account = (By.CSS_SELECTOR, ".sc-emDGWR")
    # driver.find_element(By.XPATH, "//span[text()='Trade']").click()
    trade_button = (By.XPATH, "//span[text()='Trade']")

    def click_account_type(self):
        self.wait_for_element(self.account_type).click()

    def list_of_account_types(self):
        self.wait_for_element((self.types_of_account))
        accounts = self.driver.find_elements(By.CSS_SELECTOR, ".sc-emDGWR")
        return accounts

    def click_trade_button(self):
        self.wait_for_element(self.trade_button).click()




    """
def AccountSwitch():
    account_type = driver.find_element(By.XPATH, "//div[@class='sc-csJRnm kQEjyJ']").click()
    sleep(2)
    account_switch = driver.find_elements(By.CSS_SELECTOR, ".sc-emDGWR")
    sleep(2)

    for switch in account_switch:
        # print(switch.text)
        # select_account_type=
        if switch.text == "Demo Account":

            switch.click()

            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Trade']")))

            driver.find_element(By.XPATH, "//span[text()='Trade']").click()
            print('Account Selected')

    sleep(2)
"""