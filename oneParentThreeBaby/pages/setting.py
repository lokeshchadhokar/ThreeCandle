from .base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class Setting_page(BasePage):
    # setting = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[1]/div[2]/div/div[2]/div/div/div')
    setting_xpath = (By.XPATH,'//*[@id="root"]/div[2]/div[1]/div[2]/div/div[2]/div/div/div')
    # driver.find_element(By.XPATH, "//span[text()='Candlestick Chart']").click()
    candleStick_xpath =(By.XPATH, "//span[text()='Candlestick Chart']")
    interval_xpath = (By.XPATH, "//span[text()='Intervals']")
    OneMin_xpath =(By.XPATH,"//div[@class='sc-eYDgzN AhOwJ']/div")

    test = (By.XPATH,"//div[@class='sc-eYDgzN iHgBB']")

    def setting_click(self):
        self.wait_for_element(self.setting_xpath).click()

    def SelectCandlestick(self):
        self.wait_for_element(self.candleStick_xpath).click()

    def selectInterval(self):
        self.wait_for_element(self.interval_xpath).click()
        print("interval selected")

    def select1min(self):
        self.wait_for_element(self.OneMin_xpath).click()
        print("1 MIN interval selected")

    def testda(self):
        a = self.driver.find_elements(By.XPATH,"//div[@class='sc-eYDgzN iHgBB']")
        print(len(a))
    # @staticmethod
    # def setting_option(driver):
    #     # wait.until(
    #     #     EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[2]/div/div[2]/div/div/div')))
    #     setting = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[2]/div/div[2]/div/div/div').click()
    #     sleep(10)




