#!/usr/bin/python3
import time, sys, os, random, getpass
from os import path
import selenium
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class scrape:
    def __init__(self, userCust = []):
        self.userCust = userCust

    def main(self):
        try:
            driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div").click()
        except:
            driver.refresh()

        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(random.choice(self.userCust.split(',')) + Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[1]/div/div/div[2]").click()

        def srcFunc():
            srcImg = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[1]/div/div/div[2]/img").get_attribute("src")
            urllib.urlretrieve(srcImg, ('meme_'+str(len(os.listdir('/tmpUpload')))))
        srcFunc()

    if __name__ == "__main__":
        zCall = scrape
        zCall.main()