#!/usr/bin/python3
import time, sys, os, random, getpass
import selenium
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class FoUf:
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
                    driver.find_element_by_xpath("//*[@id='slfErrorAlert']")
                    time.sleep(60) #let your internet figure out wtf is going on, maybe its your browser, elt it vibe for a bit.
                    login()
                except:
                    time.sleep(5)
        login()
        time.sleep(10)

        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img").click() #click profile
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div").click() #click profile
        time.sleep(3)
        if driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div/span").text == "0":
            print("You are no longer following anyone!")
        else:
            def UnfRef(num_ref = 3):
                for numRef in range(num_ref):
                    if driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div/span").text == "0":
                        pass
                    else:
                        try:
                            driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div").click() #click on followerING button
                            time.sleep(2)
                            htmlUnfollow = "/html/body/div[6]/div/div/div/div[3]/ul/div/li[1]/div/div[3]/button"   
                            for i in range(1,13,1):         
                                htmlUnfollow = "/html/body/div[6]/div/div/div/div[3]/ul/div/li["+str(i)+"]/div/div[3]/button"
                                if (driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/ul/div/li["+str(i)+"]/div/div[3]/button").text == "Follow"):
                                    continue    
                                driver.find_element_by_xpath(htmlUnfollow).click()
                                driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
                                time.sleep(2)
                        except:
                            driver.refresh()
            UnfRef()

        def FolReset():
            try:
                driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div").click()
            except:
                driver.refresh()
            time.sleep(4)
            driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(random.choice(self.userCust.split(',')) + Keys.ENTER)
            time.sleep(3)
            driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()    
            time.sleep(3)
            def FolRef(num_ref = 3):
                for numRef in range(num_ref):
                    try:
                        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div").click()
                        if (driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[1]/div/div[3]/button").text == "Following"):
                            FolReset()
                        else:
                            htmlBadBoyToFollow = "/html/body/div[6]/div/div/div/div[2]/ul/div/li[1]/div/div[3]/button"   
                            for i in range(1,13,1):
                                htmlBadBoyToFollow = "/html/body/div[6]/div/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[3]/button"
                                if (driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[3]/button").text == "Following"):
                                    continue        
                                driver.find_element_by_xpath(htmlBadBoyToFollow).click()
                                time.sleep(3)
                    except:
                        driver.refresh()
            FolRef()
        FolReset()
        driver.close()

    if __name__ == "__main__":
        xCall = FoUf(userName, userPass, userCust)
        xCall.main()