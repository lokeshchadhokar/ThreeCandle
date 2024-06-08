from oneParentThreeBaby.pages.DashBoard_page import DashBoard_locators

class chartPeriod_selector:
    @staticmethod
    def SelectPeriod(driver):
        dash = DashBoard_locators(driver)
        dash.select1H_SmallPeriod().click()
        print("small 1 hour timeframe selected")
        return dash
