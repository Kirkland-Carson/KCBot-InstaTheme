#!/usr/bin/python3
import time, sys, os, random, getpass
from os import path
import urllib
from urllib.request import urlretrieve
import selenium
from random import randint
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class scrape:
    def __init__(self, userName = "", userPass = "", userCust = []):
        self.userName = userName
        self.userPass = userPass
        self.userCust = userCust

    def main(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.download.dir', '/tmpUpload')
        profile.set_preference('browser.download.manager', False)
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)

        driver.implicitly_wait(10)
        
        driver.get("https://instagram.com/")
        
        def login():
            driver.find_element_by_xpath("//input[@name=\"username\"]").clear()
            driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.userName)
            driver.find_element_by_xpath("//input[@name=\"password\"]").clear()
            driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.userPass)
            time.sleep(2)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(8)
        
            try:
                driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
                time.sleep(5)
                if driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]"):
                    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            except:
                try:
                    if driver.find_element_by_xpath("//*[@id='slfErrorAlert']"):
                        driver.refresh()
                        time.sleep(5)
                        login()
                except:
                    time.sleep(5)
        login()
        time.sleep(10)

        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(random.choice(self.userCust.split(',')) + Keys.ENTER)
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()
        time.sleep(8)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]").click()
        tile.sleep(5)

        def srcFunc():
            try:
                srcCheckImg = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[1]/div/div/div[1]/img")
                srcCheckVid = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[1]/div/div/div/div/div/video")
            except:
                pass
            srcImg = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div/img").get_attribute("src")
            urllib.request.urlretrieve(srcImg, ('meme_'+str(len(os.listdir('/home/acarson/Desktop/Bots/Instagram/InstaTheme_v1_2/tmpUpload')))))
        srcFunc()

    if __name__ == "__main__":
        zCall = scrape()
        zCall.main()