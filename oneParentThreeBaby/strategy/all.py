from oneParentThreeBaby.function.login import login_procce
from oneParentThreeBaby.function.Account_Type import select_accunt_type
from oneParentThreeBaby.function.japanis_candlestick import select_japanis_candle
from oneParentThreeBaby.function.priceReading import Action
from oneParentThreeBaby.function.Auto_select_currency import currency_pairs
from oneParentThreeBaby.function.Intervel import selectTimeIntervel
from oneParentThreeBaby.strategy.colourfinder import candlecolour
import datetime
from time import sleep

driver = login_procce.startLogin()
driver = select_accunt_type.select_account(driver)
driver = select_japanis_candle.select_candle_pattern(driver)
driver = selectTimeIntervel.selectTime(driver)

currency_pairss = ["EUR GBP", "EUR AUD", "CHF JPY", "AUD USD", "AUD JPY", "AUD CAD"]
cur_pair = currency_pairs
ac = Action
data = []
while True:
    Time = datetime.datetime.now()
    if int(Time.strftime('%S')) == 1:
        sleep(0.15000)
        if len(data) > 10:
            del data[0]
        open_close = ac.actionchain(driver)
        current_data = {
            open_close[0].text: open_close[1].text,
            open_close[2].text: open_close[3].text,
            open_close[4].text: open_close[5].text,
            open_close[6].text: open_close[7].text
        }
        color = candlecolour.decide_colour(current_data)
        current_data = {'colour':color,
            open_close[0].text: open_close[1].text,
            open_close[2].text: open_close[3].text,
            open_close[4].text: open_close[5].text,
            open_close[6].text: open_close[7].text
        }
        data.append(current_data)
        print(data)
        if len(data)>3:
            if data[-3]['High'] >= data[-2]['Close'] and \
                    data[-3]['High'] >= data[-1]['Close']:
                print('Pass')
        sleep(1)
