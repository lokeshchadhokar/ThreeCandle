from oneParentThreeBaby.utils.browser_setup import get_driver
from oneParentThreeBaby.utils.data_reader import get_test_data
from oneParentThreeBaby.pages.login_page import LoginPage
from time import sleep

class login_procce:
    @staticmethod
    def startLogin():
        print("login from functon".center(60,"-"))
        driver = get_driver()
        driver.get('https://irontrade.com/')
        user = get_test_data()["username"]
        passw= get_test_data()["password"]
        login_page = LoginPage(driver)
        login_page.enter_username(user)
        login_page.enter_password(passw)
        sleep(40)
        login_page.click_login()
        print("login End".center(60, "="))
        return driver

# a=login_procce
# a.startLogin(a)