
from .base_page import BasePage
from selenium.webdriver.common.by import By

class DashBoard_locators(BasePage):
    onehourLargePeriod_xpath = (By.XPATH, "//button[text()='1h']")
    onehourSmallPeriod_xpath = (By.XPATH, "//button[text()='1h'][2]")
    fiftyMinPeriod_xpath = (By.XPATH, "//button[text()='50min']")
    TenMinPeriod =(By.XPATH, "//button[text()='10m']")

    buttontimeInterval_xpath = (By.XPATH, "//div[@class='sc-kRXbY hzjne']")
    Listalltime_xpath = (By.XPATH, "//button[@class='sc-kDkoGq hBvjqL']")
    selectcurrency_css = (By.CSS_SELECTOR, "button[class='sc-gnEqpY kBLzPd']")
    list_of_asset_XPATH = (By.XPATH,'//*[@id="root"]/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div/div[3]/div/div[1]/div[1]/div[1]')
    n = (By.XPATH,'//div[contains(text(), "GBP USD")]')

    def currency_selector(self):
        return self.wait_for_element(self.selectcurrency_css).click()

    def selectAsset(self):
        a = self.wait_for_element(self.list_of_asset_XPATH).click()
        # self.wait_for_element(self.n).click()

    def select1H_LargePeriod(self):
        # print("Selecting 1-hour large period...")
        return self.wait_for_element(self.onehourLargePeriod_xpath).click()

    def select1H_SmallPeriod(self):
        # print("Selecting 1-hour small period...")
        return self.wait_for_element(self.onehourSmallPeriod_xpath).click()
    def select10minPeriod(self):
        return self.wait_for_element(self.TenMinPeriod)
    def clickTimeIntervalButton(self):
        # print("Clicking on time interval button...")
        return self.wait_for_element(self.buttontimeInterval_xpath).click()

    def selectOneMinTime(self):
        self.wait_for_element(self.Listalltime_xpath)
        # print("Selecting 1 minute time interval...")
        # all_buttons = self.driver.wait(By.XPATH, "//button[@class='sc-kDkoGq hBvjqL']")
        all_buttons =self.wait_for_elements(self.Listalltime_xpath)
        for button in all_buttons:
            # print(f"Found button with text: {button.text}")
            if button.text == '1 min':
                print("Clicking on 1 min button...")
                button.click()
                break
