import json


def load_config():
    with open("/home/rutek/Strato/Exp/config/configuration.json") as json_file:
        config = json.load(json_file)

    return config
