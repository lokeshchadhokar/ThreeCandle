from oneParentThreeBaby.function.login import login_procce
from oneParentThreeBaby.function.Account_Type import select_accunt_type
from oneParentThreeBaby.function.japanis_candlestick import select_japanis_candle
from oneParentThreeBaby.function.priceReading import Action
from oneParentThreeBaby.function.Auto_select_currency import currency_pairs
from oneParentThreeBaby.function.Intervel import selectTimeIntervel
import datetime
from oneParentThreeBaby.strategy.dict_value_arranger import valueDistribute
from time import sleep
from oneParentThreeBaby.strategy.StrategyTwoChildrenOneParent import twoChildparent

# Login and setup
driver = login_procce.startLogin() # function/login.py
driver = select_accunt_type.select_account(driver) # function/Account_Type.py
driver = select_japanis_candle.select_candle_pattern(driver) # function/japanis_candlestick.py
driver = selectTimeIntervel.selectTime(driver)
strategy = twoChildparent

# List of currency pairs to monitor
currency_pairss = ["EUR JPY", "EUR USD"]

# Initialize currency pair data storage
currency_data = {
    "USD JPY": [],
    "EUR USD": [],
    "EUR JPY": [],
    "GBP USD": [],
    "CAD CHF": [],
    "USD CHF": [],
    "EUR AUD": [],
    "AUD JPY": [],
    "AUD USD": []
}

cur_pair = currency_pairs(driver)
ac = Action

while True:
    Time = datetime.datetime.now()
    if int(Time.strftime('%S')) == 1:
        sleep(0.20000)
        print("START".center(60, "-"))

        try:
            for pair in currency_pairss:
                values, text = cur_pair.find_currency_pair(pair)
                print(values[0].text, text)
                cureent = valueDistribute.arrangeValues(values)

                if text in currency_data:
                    currency_data[text].append(cureent)

                    if strategy.check_conditionforUP(currency_data[text]):
                        print(f"{text}: Pass for up")
                    elif strategy.check_conditionforDOWN(currency_data[text]):
                        print(f"{text}: Pass for down")
                    elif strategy.last_two_candle(currency_data[text]):
                        index = currency_pairss.index(text)
                        currency_pairss.insert(0, currency_pairss.pop(index))

                    print(text, strategy.last_two_candle(currency_data[text]), currency_data[text][-1])

            # Keep only the last 10 records for each currency pair
            for key in currency_data:
                if len(currency_data[key]) > 10:
                    currency_data[key] = currency_data[key][-10:]

            print(currency_pairss)
            print("EUR USD", currency_data["EUR USD"][-1] if currency_data["EUR USD"] else "No Data")
            print("GBP USD", currency_data["GBP USD"][-1] if currency_data["GBP USD"] else "No Data")
            print("EUR JPY", currency_data["EUR JPY"][-1] if currency_data["EUR JPY"] else "No Data")

        except Exception as e:
            print(e)
