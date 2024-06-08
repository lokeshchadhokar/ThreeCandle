from oneParentThreeBaby.pages.DashBoard_page import DashBoard_locators
from time import sleep

class selectTimeIntervel:
    @staticmethod
    def selectTime(driver):
        d = DashBoard_locators(driver)
        d.clickTimeIntervalButton()
        d.selectOneMinTime()
        print("1-minute time selected")
        # d.select1H_LargePeriod()
        d.select1H_SmallPeriod()
        d.clickTimeIntervalButton()
        sleep(3)
        d.currency_selector()
        d.selectAsset()
        return driver