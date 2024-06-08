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

currency_pairss = ["USD JPY", "EUR USD", "EUR JPY", "GBP USD"]
cur_pair = currency_pairs(driver)
ac = Action

data = []
USD_JPY=[]
EUR_USD=[]
EUR_JPY=[]
GBP_USD=[]
while True:
    Time = datetime.datetime.now()
    if int(Time.strftime('%S')) == 1:
        sleep(0.15000)

        #-------------------------------------------------------------
        # Find and print each currency pair
        for pair in currency_pairss:
            values,text = cur_pair.find_currency_pair(pair)
            print(values[0].text,text)
            cureent = valueDistribute.arrangeValues(values)
            if text == 'USD JPY':
                USD_JPY.append(cureent)
                if strategy.check_conditionforUP(USD_JPY):
                    print("Pass for up")
                elif strategy.check_conditionforDOWN(USD_JPY):
                    print("pass for down")
                print("UsdJpy",USD_JPY)
            elif text == 'EUR USD':
                EUR_USD.append(cureent)
                if strategy.check_conditionforUP(USD_JPY):
                    print("Pass for up")
                elif strategy.check_conditionforDOWN(USD_JPY):
                    print("pass for down")
                print("EurUsd",EUR_USD)
            elif text == 'EUR JPY':
                EUR_JPY.append(cureent)
                if strategy.check_conditionforUP(USD_JPY):
                    print("Pass for up")
                elif strategy.check_conditionforDOWN(USD_JPY):
                    print("pass for down")
                print("EurJpy",EUR_JPY)
            elif text == 'GBP USD':
                GBP_USD.append(cureent)
                if strategy.check_conditionforUP(USD_JPY):
                    print("Pass for up")
                elif strategy.check_conditionforDOWN(USD_JPY):
                    print("pass for down")
                print("GBPUSD",GBP_USD)
            else:
                print(f"Storage not Created {text} ")

        if len(EUR_USD) > 10:
            del USD_JPY[0],EUR_USD[0],EUR_JPY[0],GBP_USD[0]



