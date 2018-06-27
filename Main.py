#coding=utf-8
import json
from selenium import webdriver
import datetime

def load_config():
    config_path = "config.json"
    f = open(config_path)
    settings = json.load(f)
    return settings

def CheckIn():
    settings = load_config()
    dr = webdriver.Firefox()
    dr.get(settings['url']['login'])
    dr.find_element_by_id('username').send_keys(settings['personal-info']['erp-account'])
    dr.find_element_by_id('password').send_keys(settings['personal-info']['erp-password'])
    dr.find_element_by_class_name('formsubmit_btn').click()
    dr.find_element_by_id('clockLink').click()
    dr.quit()


if __name__ == "__main__":
    CheckIn()