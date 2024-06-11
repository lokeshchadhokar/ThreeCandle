from oneParentThreeBaby.pages.DashBoard_page import DashBoard_locators

class chartPeriod_selector:
    @staticmethod
    def SelectPeriod(driver):
        print("Chart Perid from function".center(60, "-"))
        dash = DashBoard_locators(driver)
        dash.select1H_SmallPeriod().click()
        print("small 1 hour timeframe selected")
        print("Chart Perid End".center(60, "="))
        return dash

