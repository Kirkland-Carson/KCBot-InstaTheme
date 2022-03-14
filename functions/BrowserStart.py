#!/usr/bin/python3
import time, sys, os, random
import getpass
import unfo_v1_1 as unfoFunc
import foll_v1_1 as follFunc
import BrowserStart as BrowSt
import InstaTheme_Start as InstaMain
from random import seed
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

clear = lambda: os.system('clear')

class BrowSt:
    #Lets define "things" to actually do "things"
    def __init__(self, typeUser, typePass, prePages):
        prePages = []
    
    def document_initialised(driver):
        return driver.execute_script("return initialised")
    
    #The code above inits driver, and the one below starts it up.
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    
    #Now lets start logging into Instagram with the bot!
    driver.get("https://instagram.com")
    driver.implicitly_wait(10)

    driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(typeUser)
    driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(typePass)
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    driver.implicitly_wait(5)
    
BrowSt(typeUser, typePass, prePages)
