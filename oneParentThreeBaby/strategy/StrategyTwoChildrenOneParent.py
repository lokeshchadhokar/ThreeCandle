
class twoChildparent:
    @staticmethod
    def check_conditionforDOWN(candle_data):
        print("Three candle check GREEN for DOWN conditon from strategy".center(60))
        # Ensure there are enough candles to check the condition
        if len(candle_data) < 3:
            # print("Not enough candle data to check the condition.")
            return False

        # for i in range(len(candle_data) - 2):
            # Extract the relevant candles
        candle_1 = candle_data[-3]
        candle_2 = candle_data[-2]
        candle_3 = candle_data[-1]

            # Get the high of the first candle
        high_1 = float(candle_1['High'])

            # Check the conditions for the second and third candles
        if all([
                candle_1['colour']== 'green',
                candle_2['colour'] == 'green',
                candle_3['colour'] == 'green',
                float(candle_2['Close']) <= high_1,
                float(candle_3['Close']) <= high_1
            ]):
            print("Three conditon GREEN Down".center(60, "#"))
            print(f"candle_1 {candle_1}\ncandle_2 {candle_2}\ncandle 3{candle_3}")
            return True
        else :
            return False

    @staticmethod
    def check_conditionforUP(candle_data):
        print("Three candle check RED for UP conditon from strategy".center(60))
        # Ensure there are enough candles to check the condition
        if len(candle_data) < 3:
            # print("Not enough candle data to check the condition.")
            return False

            # Extract the relevant candles
        candle_1 = candle_data[-3]
        candle_2 = candle_data[-2]
        candle_3 = candle_data[-1]

            # Get the high of the first candle
        Low_1 = float(candle_1['Low'])

            # Check the conditions for the second and third candles
        if all([
                candle_1['colour'] == 'Red',
                candle_2['colour'] == 'Red',
                candle_3['colour'] == 'Red',
                float(candle_2['Close']) >= Low_1,
                float(candle_3['Close']) >= Low_1
            ]):
            print("Three conditon RED  UP".center(60, "^"))
            print(f"candle_1 {candle_1}\ncandle_2 {candle_2}\ncandle 3{candle_3}")
            return True
        else:
            return False
    @staticmethod
    def last_two_candle(candle_data):
        print("TWO candle for rearrange the secuence conditon from strategy".center(60))
        if len(candle_data)<2:
            return False
        candle_1 = candle_data[-2]
        candle_2 = candle_data[-1]
        high = float(candle_1["High"])
        low = float(candle_1["Low"])

        if all([candle_1['colour']=='green',
                candle_2['colour']=='green',
                float(candle_2['Close'])<= high]) or \
                all([candle_1['colour'] == 'Red',
                candle_2['colour'] == 'Red',
                float(candle_2['Close']) >= low
        ]):
            print("Two candle Pass".center(60, "@"))
            print(f"candle_1 {candle_1}\ncandle_2 {candle_2}")
            return True
        else:
            return False
