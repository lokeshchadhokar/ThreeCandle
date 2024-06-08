class candlecolour:
    @staticmethod
    def decide_colour(current_values):
        if current_values['Open'] > current_values['Close']:
            color = 'Red'
        elif current_values['Open'] == current_values['Close']:
            color = 'doji'
        else:
            color = 'green'
        return color