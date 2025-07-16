import os
import json

def load_config_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing config: {path}")
    with open(path, 'r') as f:
        return json.load(f)

def load_lambda_config(lambda_name):
    env = os.getenv("ENV", "dev")  #************ ENV will be passed via SAM  ************#
    base_path = os.path.join("env", env)

    global_config = load_config_file(os.path.join(base_path, "global.json"))
    lambda_config = load_config_file(os.path.join(base_path, f"{lambda_name}.json"))

    return lambda_config, global_config
