import json
from pathlib import Path

# configPath = str(Path().absolute())+"/configuration.json"
configPath = "/home/alarm/HAB-Experiment/config/configuration.json"

def load_config():
    with open(configPath) as json_file:
        config = json.load(json_file)

    return config
