from oneParentThreeBaby.pages.DashBoard_page import DashBoard_locators
from time import sleep

class selectTimeIntervel:
    @staticmethod
    def selectTime(driver):
        print("interval from function".center(60,"-"))
        d = DashBoard_locators(driver)
        d.clickTimeIntervalButton()
        d.selectOneMinTime()
        print("1-minute candlestick ")
        # d.select1H_LargePeriod()
        d.select10minPeriod()
        d.clickTimeIntervalButton()
        sleep(3)
        d.currency_selector()
        d.selectAsset()
        print("interval End".center(60, "="))
        return driver