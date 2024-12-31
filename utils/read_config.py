import json
import os

def read_config(config_file="config.json"):
    with open(config_file, 'r') as f:
        config = json.load(f)
        return config
    
def putintoenv():
    config = read_config()
    for key in config:
        os.environ[key] = config[key]
    return None

putintoenv()