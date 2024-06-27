import yaml

def get_config():
    config_file = "config.yml"
    with open(config_file, 'r') as ymlfile:
        config = yaml.load(ymlfile, Loader=yaml.FullLoader)
    return config
