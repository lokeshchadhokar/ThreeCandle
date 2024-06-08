import json

def get_config():
    with open('oneParentThreeBaby/data/config.json') as config_file:
        config = json.load(config_file)
        return config
