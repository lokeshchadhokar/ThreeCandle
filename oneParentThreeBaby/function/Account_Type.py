from oneParentThreeBaby.function.login import login_procce
from oneParentThreeBaby.pages.accountType_page import accountType
from time import sleep

class select_accunt_type:
    @staticmethod
    def select_account(driver):
        print("Account Type from function".center(60,"-"))
        # driver = login_procce.startLogin()
        account_page  = accountType(driver)
        sleep(2)
        account_page .click_account_type()
        sleep(2)
        account_switch = account_page.list_of_account_types()
        for i in account_switch:
            print('Enter',account_switch.index(i),"for",i.text)
        select = 2 # int(input("SELECT a no :"))


        for switch in account_switch:
            if switch == account_switch[select]:
                switch.click()
                account_page .click_trade_button()
                print(f"{switch.text} Account selected")
                sleep(5)
                return driver
        print("Account Type End".center(60, "="))
# a= select_accunt_type()
# # # lg = login_procce.startLogin(a)
# a.select_account()
