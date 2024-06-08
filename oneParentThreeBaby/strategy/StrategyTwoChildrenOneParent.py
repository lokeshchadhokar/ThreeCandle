
class twoChildparent:
    @staticmethod
    def check_conditionforDOWN(candle_data):
        # Ensure there are enough candles to check the condition
        if len(candle_data) < 3:
            print("Not enough candle data to check the condition.")
            return False

        for i in range(len(candle_data) - 2):
            # Extract the relevant candles
            candle_1 = candle_data[i]
            candle_2 = candle_data[i + 1]
            candle_3 = candle_data[i + 2]

            # Get the high of the first candle
            high_1 = float(candle_1['High'])

            # Check the conditions for the second and third candles
            if all([
                candle_2['colour'] == 'green',
                float(candle_2['Close']) < high_1,
                candle_3['colour'] == 'green',
                float(candle_3['Close']) < high_1
            ]):
                return True

        return False

    @staticmethod
    def check_conditionforUP(candle_data):
        # Ensure there are enough candles to check the condition
        if len(candle_data) < 3:
            print("Not enough candle data to check the condition.")
            return False

        for i in range(len(candle_data) - 2):
            # Extract the relevant candles
            candle_1 = candle_data[i]
            candle_2 = candle_data[i + 1]
            candle_3 = candle_data[i + 2]

            # Get the high of the first candle
            high_1 = float(candle_1['High'])

            # Check the conditions for the second and third candles
            if all([
                candle_2['colour'] == 'green',
                float(candle_2['Close']) < high_1,
                candle_3['colour'] == 'green',
                float(candle_3['Close']) < high_1
            ]):
                return True

        return False
