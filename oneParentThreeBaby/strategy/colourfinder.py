class candlecolour:
    @staticmethod
    def decide_colour(current_values):
        # print("check the candle colour from strategy".center(60))
        if float(current_values['Open']) > float(current_values['Close']):
            color = 'Red'

        elif float(current_values['Open']) < float(current_values['Close']):
            color = 'green'

        elif float(current_values['Open']) == float(current_values['Close']):
            color = 'doji'

        else:
            color = 'None'
        return color