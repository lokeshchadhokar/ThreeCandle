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

currency_pairss = ["AUD USD"]

cur_pair = currency_pairs(driver)
ac = Action

data = []
USD_JPY=[]
EUR_USD=[]
EUR_JPY=[]
GBP_USD=[]
EUR_AUD=[]
CAD_CHF=[]
while True:

    Time = datetime.datetime.now()
    if int(Time.strftime('%S')) == 1:
        sleep(0.15000)
        print("START".center(60, "="))

        #-------------------------------------------------------------
        # Find and print each currency pair
        try:
            for pair in currency_pairss:
                # try:
                    values,text = cur_pair.find_currency_pair(pair)
                    print(values[0].text,text)
                    cureent = valueDistribute.arrangeValues(values)
                    if text == 'USD JPY':
                        USD_JPY.append(cureent)
                        if strategy.check_conditionforUP(USD_JPY):
                            print("Pass for up")
                        elif strategy.check_conditionforDOWN(USD_JPY):
                            print("pass for down")
                        elif strategy.last_two_candle(USD_JPY):
                            index = currency_pairss.index('USD JPY')
                            currency_pairss.insert(0, currency_pairss.pop(index))
                            print("Two Pass",currency_pairss)
                        print(text,strategy.last_two_candle(USD_JPY),USD_JPY)

                    elif text == 'EUR USD':
                        EUR_USD.append(cureent)
                        if strategy.check_conditionforUP(EUR_USD):
                            print("Pass for up")
                        elif strategy.check_conditionforDOWN(EUR_USD):
                            print("pass for down")
                        elif strategy.last_two_candle(EUR_USD):
                            index = currency_pairss.index(text)
                            currency_pairss.insert(0, currency_pairss.pop(index))
                            print("Two Pass",currency_pairss)
                        print(text,strategy.last_two_candle(EUR_USD),EUR_USD[-1])
                    elif text == 'EUR JPY':
                        EUR_JPY.append(cureent)
                        if strategy.check_conditionforUP(EUR_JPY):
                            print("Pass for up")
                        elif strategy.check_conditionforDOWN(EUR_JPY):
                            print("pass for down")
                        elif strategy.last_two_candle(EUR_JPY):
                            index = currency_pairss.index(text)
                            currency_pairss.insert(0, currency_pairss.pop(index))
                            print("Two Pass",currency_pairss)
                        print(text,strategy.last_two_candle(EUR_USD),EUR_JPY)
                    elif text == 'GBP USD':
                        GBP_USD.append(cureent)
                        if strategy.check_conditionforUP(GBP_USD):
                            print("Pass for up")
                        elif strategy.check_conditionforDOWN(GBP_USD):
                            print("pass for down")
                        elif strategy.last_two_candle(GBP_USD):
                            index = currency_pairss.index(text)
                            currency_pairss.insert(0, currency_pairss.pop(index))
                            print("Two Pass", currency_pairss)
                        print(text,strategy.last_two_candle(GBP_USD),GBP_USD[-1])
                    elif text == 'EUR AUD':
                        EUR_AUD.append(cureent)
                        if strategy.check_conditionforUP(EUR_AUD):
                            print("Pass for up")
                        elif strategy.check_conditionforDOWN(EUR_AUD):
                            print("pass for down")
                        elif strategy.last_two_candle(EUR_AUD):
                            index = currency_pairss.index(text)
                            currency_pairss.insert(0, currency_pairss.pop(index))
                            print("Two Pass", currency_pairss)
                        print(text,strategy.last_two_candle(EUR_AUD),EUR_AUD)
                    elif text == 'CAD CHF':
                        CAD_CHF.append(cureent)
                        if strategy.check_conditionforUP(CAD_CHF):
                            print("Pass for up")
                        elif strategy.check_conditionforDOWN(CAD_CHF):
                            print("pass for down")
                        elif strategy.last_two_candle(CAD_CHF):
                            index = currency_pairss.index(text)
                            currency_pairss.insert(0, currency_pairss.pop(index))
                            print("Two Pass", currency_pairss)
                        print(text,strategy.last_two_candle(CAD_CHF),CAD_CHF[-1])
                    else:
                        print(f"Storage not Created {text} ")
                # except Exception as e:
                #     print("Value unpack")
            if len(EUR_USD) > 10:
                del USD_JPY[0],EUR_USD[0],EUR_JPY[0],GBP_USD[0],CAD_CHF[0],EUR_AUD[0]
            print(currency_pairss)
        except Exception as e:
            print(e)

