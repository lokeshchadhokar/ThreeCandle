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
from oneParentThreeBaby.pages.DashBoard_page import DashBoard_locators
# Login and setup
driver = login_procce.startLogin() # function/login.py
driver = select_accunt_type.select_account(driver) # function/Account_Type.py
driver = select_japanis_candle.select_candle_pattern(driver) # function/japanis_candlestick.py
driver = selectTimeIntervel.selectTime(driver)
d= DashBoard_locators(driver)

strategy = twoChildparent

# List of currency pairs to monitor
currency_pairss = ["EUR JPY","USD JPY","CHF JPY","EUR USD","GBP USD","AUD USD","AUD JPY","USD CHF"]

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
    "AUD USD": [],
    "CHF JPY": []
}

cur_pair = currency_pairs(driver)
ac = Action

while True:
    Time = datetime.datetime.now()
    if int(Time.strftime('%S')) == 1:
        sleep(0.20000)
        print("START".center(100, "-"))
        try:
            for pair in currency_pairss:
                try :
                    print(f"{pair}".center(100))
                    values, text = cur_pair.find_currency_pair_Three_values(pair)
                    candle1 = values[0]#valueDistribute.arrangeValues_Three_time(values[0],values[3])
                    candle2 = values[1]#valueDistribute.arrangeValues_Three_time(values[1],values[4])
                    candle3 = values[2]#valueDistribute.arrangeValues_Three_time(values[2],values[5])
                    # print(f"candle1 :{candle1}")
                    # print(f"candle2 :{candle2}")
                    # print(f"candle3 :{candle3}")
                    if text in currency_data:
                        # currency_data[text].append(candle1)
                        currency_data[text]=[candle1,candle2,candle3]
                        if strategy.check_conditionforUP(currency_data[text]):
                            print(f"{text}: Pass for up")
                            d.click_upper_button()
                        elif strategy.check_conditionforDOWN(currency_data[text]):
                            print(f"{text}: Pass for down")
                            d.click_lower_button()
                        elif strategy.last_two_candle(currency_data[text]):
                            index = currency_pairss.index(text)
                            currency_pairss.insert(0, currency_pairss.pop(index))

                        print(text)
                except Exception as e:
                    index = currency_pairss.index(pair)# agr kisi bhi currency pair main koi failhonga to us pair ko bahar nikalemga
                    currency_pairss.insert(-1, currency_pairss.pop(index))# fail pair ko last indexing main insert karvaynga
                    print(f"inside for loop{pair}:{e}")
            # Keep only the last 10 records for each currency pair
            for key in currency_data:
                if len(currency_data[key]) > 10:
                    currency_data[key] = currency_data[key][-10:]

            print(currency_pairss)
            for i in currency_pairss:
                # print(i, currency_data[i][-1] if currency_data[i] else "No Data")
                print(i, f' Time  :{currency_data[i][-1]["Time"]},'
                         f' Open  :{currency_data[i][-1]["Open"]},'
                         f' High  :{currency_data[i][-1]["High"]},'
                         f' Low   :{currency_data[i][-1]["Low"]} ,'
                         f' Close :{currency_data[i][-1]["Close"]}'  if currency_data[i] else "No Data")
            # # print("GBP USD", currency_data["GBP USD"][-1] if currency_data["GBP USD"] else "No Data")
            # print("EUR JPY", currency_data["EUR JPY"][-1] if currency_data["EUR JPY"] else "No Data")

        except Exception as e:

            print("all",e)
            continue
