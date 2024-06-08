# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class BasePage:
#     def __init__(self,driver):
#         self.driver = driver
#
#     def wait_for_element(self,locator):
#         return WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator))
#
#     def wait_for_elements(self, locator):
#         return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))

    def wait_for_elements(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(locator))
    def wait_for_1sec(self,locator):
        return WebDriverWait(self.driver, 1).until(EC.presence_of_all_elements_located(locator))