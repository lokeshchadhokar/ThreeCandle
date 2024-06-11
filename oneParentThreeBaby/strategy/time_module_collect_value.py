from oneParentThreeBaby.function.login import login_procce
from oneParentThreeBaby.function.Account_Type import select_accunt_type
from oneParentThreeBaby.function.japanis_candlestick import select_japanis_candle
from oneParentThreeBaby.function.priceReading import Action
from oneParentThreeBaby.function.Auto_select_currency import currency_pairs
from oneParentThreeBaby.function.Intervel import selectTimeIntervel
from oneParentThreeBaby.strategy.colourfinder import candlecolour
import datetime
from oneParentThreeBaby.strategy.dict_value_arranger import valueDistribute
from time import sleep
from oneParentThreeBaby.strategy.StrategyTwoChildrenOneParent import twoChildparent

strategy = twoChildparent
driver = login_procce.startLogin()
driver = select_accunt_type.select_account(driver)
driver = select_japanis_candle.select_candle_pattern(driver)
driver = selectTimeIntervel.selectTime(driver)

currency_pairss = ["EUR USD", "GBP USD","CAD CHF"]

cur_pair = currency_pairs(driver)
ac = Action

while True:

    Time = datetime.datetime.now()
    if int(Time.strftime('%S')) == 1:
        sleep(0.15000)
        print("START".center(60, "="))
        pricevalue = ac.actionchain_withtime(driver)
        print(pricevalue[0].text,pricevalue[1].text)