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
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)

        driver.implicitly_wait(10)
        
        driver.get("https://instagram.com/")
        
        driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.userName)
        driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.userPass)
        time.sleep(2)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(5)
        
        driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        time.sleep(2)
        
        ##############################################################################################################################################
        # Unfollow ###################################################################################################################################
        ##############################################################################################################################################

        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img").click() #click profile
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div").click() #click profile
        time.sleep(3)
        if driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div/span").text == "0":
            print("You are no longer following anyone!")
        else:
            def UnfRef():
                refCount = 0
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div").click() #click on followerING button
                    time.sleep(2)
                    htmlUnfollow = "/html/body/div[6]/div/div/div/div[3]/ul/div/li[1]/div/div[3]/button"   
                    for i in range(1,45,1):         
                        htmlUnfollow = "/html/body/div[6]/div/div/div/div[3]/ul/div/li["+str(i)+"]/div/div[3]/button"
                        if (driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/ul/div/li["+str(i)+"]/div/div[3]/button").text == "Follow"):
                            continue    
                        driver.find_element_by_xpath(htmlUnfollow).click()
                        driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
                        time.sleep(2)
                        refCount = refCount + 1
                except:
                    driver.refresh()
                    if refCount <= 45:
                        UnfRef()
                    else:
                        print(" ")
                        print(" ")
                        print(" ")
                        print("You have maxed out your Unfollows for 2 hours!")
                        print("If your account is on Fully Automaed, this will auto repeat by itself again in 2 hours.")
                        print("If your account is on Semi Automaed, Please refrain from running script to avoid Ghost Ban.")
                        print(" ")
                        print("(if you must run it again, do it in 1 hour. Instagram has 150acc soft cap per 'day')")
                        print("(This means every 8 hours, you can run 150 accounts, in 24 hours thats 450.)")
                        print("(To avoid soft cap, run 40, every 2 hours to avoid account resets)")
                        print(" ")
                        print(" ")
                        print(" ")
                        pass
            UnfRef()
        ############################################################################################################################################
        # follow ###################################################################################################################################
        ############################################################################################################################################

        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(random.choice(self.userCust.split(',')) + Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()    
        time.sleep(3)
        def FolRef():
            refCount = 0
            try:
                driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div").click()
                htmlBadBoyToFollow = "/html/body/div[6]/div/div/div/div[2]/ul/div/li[1]/div/div[3]/button"   
                for i in range(1,49,1):
                    htmlBadBoyToFollow = "/html/body/div[6]/div/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[3]/button"
                    if (driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[3]/button").text == "Following"):
                        continue        
                    driver.find_element_by_xpath(htmlBadBoyToFollow).click()
                    time.sleep(3)
                    refCount = refCount + 1
            except:
                driver.refresh()
                print(refCount)
                if refCount <= 49:
                    FolRef()
                else:
                    pass

    if __name__ == "__main__":
        xCall = FoUf(userName, userPass, userCust)
        xCall.main()