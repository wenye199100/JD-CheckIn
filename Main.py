#coding=utf-8
import json
from selenium import webdriver

def load_config():
    config_path = "config.json"
    f = open(config_path)
    settings = json.load(f)
    return settings


if __name__ == "__main__":
    dr = webdriver.Chrome('C:\\Users\\qzlab\\Documents\\GitHub\\chromedriver.exe')
    settings = load_config()
