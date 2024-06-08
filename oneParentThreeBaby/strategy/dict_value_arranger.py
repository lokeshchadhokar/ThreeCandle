from .colourfinder import candlecolour
import datetime

class valueDistribute:
    @staticmethod
    def arrangeValues(open_close):
        d = datetime.datetime.now()
        current_data = {
            open_close[0].text: open_close[1].text,
            open_close[2].text: open_close[3].text,
            open_close[4].text: open_close[5].text,
            open_close[6].text: open_close[7].text
        }
        color = candlecolour.decide_colour(current_data)
        current_data = {
            'Date': d.strftime("%d/%m%Y"),
            'Time': d.strftime("%H:%M:%S"),
            'colour': color,
            open_close[0].text: open_close[1].text,
            open_close[2].text: open_close[3].text,
            open_close[4].text: open_close[5].text,
            open_close[6].text: open_close[7].text
        }
        return current_data
