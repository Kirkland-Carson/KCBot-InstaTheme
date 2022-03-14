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

#Now lets start following!
driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(prePages[randint(0,len(prePages)-1)] + Keys.ENTER)
driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()    
driver.implicitly_wait(5)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div").click()
driver.implicitly_wait(5)

htmlBadBoyToFollow = "/html/body/div[6]/div/div/div/div[3]/ul/div/li[1]/div/div[3]/button"   
for i in range(2,12,1):
    htmlBadBoyToFollow = "/html/body/div[6]/div/div/div/div[3]/ul/div/li["+str(i)+"]/div/div[3]/button"
    if(driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/ul/div/li["+str(i)+"]/div/div[3]/button").text == "Following"):
        # This is so we dont follow people we already follow- trust me this would cause issues otherwise
        continue               
    driver.find_element_by_xpath(htmlBadBoyToFollow).click()
    driver.implicitly_wait(5)
