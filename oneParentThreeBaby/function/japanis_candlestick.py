from oneParentThreeBaby.pages.setting import Setting_page
# from oneParentThreeBaby.function.Account_Type import select_accunt_type
from time import sleep
class select_japanis_candle:
    @staticmethod
    def select_candle_pattern(driver):
        print("japanis candlestick from function".center(60, "-"))
        setting_page = Setting_page(driver)
        setting_page.setting_click()
        setting_page.SelectCandlestick()
        driver.back()
        sleep(2)
        print("japanis candlestick End".center(60, "="))
        return driver

