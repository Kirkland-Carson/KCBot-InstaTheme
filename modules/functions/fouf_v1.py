#!/usr/bin/python3
import time, sys, os, random, getpass
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class FoUf():
    def __init__(self, userName = "", userPass = "", userCust = []):
        self.userCust = userCust
        self.userName = userName
        self.userPass = userPass
        
    def main(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(1)
        
        driver.get("https://instagram.com/")
        
        driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.userName)
        driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.userPass)
        driver.implicitly_wait(15)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        driver.implicitly_wait(15)
        
        driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        driver.implicitly_wait(20)
        
        ###########################################################################
        # Unfollow ################################################################
        ###########################################################################

        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img").click() #click profile
        driver.implicitly_wait(20)
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div").click() #click profile
        driver.implicitly_wait(20)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div").click() #click on followerING button
        driver.implicitly_wait(20)

        htmlUnfollow = "/html/body/div[6]/div/div/div/div[3]/ul/div/li[1]/div/div[3]/button"   
        for i in range(2,12,1):
            htmlUnollow = "/html/body/div[6]/div/div/div/div[3]/ul/div/li["+str(i)+"]/div/div[3]/button"
            if(driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/ul/div/li["+str(i)+"]/div/div[3]/button").text == "Follow"):
                continue               
            driver.find_element_by_xpath(htmlUnfollow).click()
            driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
            driver.implicitly_wait(20)

        ###########################################################################
        # follow ##################################################################
        ###########################################################################

        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div").click()
        driver.implicitly_wait(15)
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(self.userCust[randint(0,len(self.userCust)-1)] + Keys.ENTER)
        driver.implicitly_wait(15)
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()    
        driver.implicitly_wait(15)
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div").click()
        driver.implicitly_wait(15)

        htmlBadBoyToFollow = "/html/body/div[6]/div/div/div/div[3]/ul/div/li[1]/div/div[3]/button"   
        for i in range(2,12,1):
            htmlBadBoyToFollow = "/html/body/div[6]/div/div/div/div[3]/ul/div/li["+str(i)+"]/div/div[3]/button"
            if(driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/ul/div/li["+str(i)+"]/div/div[3]/button").text == "Following"):
                continue        
            driver.find_element_by_xpath(htmlBadBoyToFollow).click()
            driver.implicitly_wait(10)

    if __name__ == "__main__":
        xCall = FoUf(userName, userPass, userCust)
        xCall.main()
