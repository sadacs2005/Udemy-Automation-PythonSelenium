import configparser


def readConfigFile(section, key):
    cfg = configparser.ConfigParser()
    cfg.read("../ConfigurationFiles/config.cfg")
    return cfg.get(section, key)
