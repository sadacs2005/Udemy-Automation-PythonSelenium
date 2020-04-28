import configparser
import os

# Get the project path
from configparser import NoSectionError

fileDir = os.path.dirname(__file__)
rootDir = os.path.dirname(fileDir)
# Create object of ConfigParser
configObj = configparser.ConfigParser()
try:
    # To read data from config file
    # configObj.read(rootDir+"\\config.cfg")
    configObj.read(".././config.cfg")
    print("The URL is: "+configObj.get("Application1", "url"))
    print("The username is:"+configObj.get("Application1", "username"))
    print("The password is:" + configObj.get("Application1", "password"))
except FileNotFoundError as e:
    print(e)
except NoSectionError as e:
    print(e)
