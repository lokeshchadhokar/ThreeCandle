import json

def get_test_data():
    with open(r'D:\selenium_vertual_envorment\ThreeCandle\oneParentThreeBaby\data\test_data.json') as data_file:
        test_data = json.load(data_file)
    return test_data
