#!/usr/bin/python3

#!/usr/bin/python3
#Import everything i need, cant make a sword without the ore.
import time, sys, os, random
import getpass
from random import seed
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

clear = lambda: os.system('clear')

#We are going to need a BIT of information to even start... So lets start here!

#Lets Start with the login information
clear()
print("----------------------------------")
print("-- Kirkland Carson - InstaTheme --")
print("----------------------------------")
print(" ")
print("Welcome to InstaTheme...")
print(" ")
typeUser = input("Instagram Username : ")
typePass = getpass.getpass("Instagram Password : ")
print(" ")
print("Double Check Entered Information")
print("Username : ", typeUser)
#print("Password : ", typePass)
loginCheck = input("Is this information correct?(y/n) : ")
clear()
class loginLoop:
    if loginCheck=="y":
        clear()
    elif loginCheck=="n":
        print("----------------------------------")
        print("-- Kirkland Carson - InstaTheme --")
        print("----------------------------------")
        print(" ")
        typeUser = input("Instagram Username : ")
        typePass = input("Instagram Password : ")
        print(" ")
        print("Double Check Entered Information")
        print("Username : ", typeUser)
        print("Password : ", typePass)
        loginCheck = input("Is this information correct?(y/n) : ")
        if loginCheck=="y":
            clear()
        else:
            print(" ")
            print("Attempts Maxed...")
            print("Please retry again...")
            print(" ")
            exit()
    else:
        print("Please use: 'y' or 'n'...")
        exit()
print("----------------------------------")
print("-- Kirkland Carson - InstaTheme --")
print("----------------------------------")
print(" ")
print("Pre-Set List Example : jokezar, 6nics, shack")
print("Add as many Pre-Set Accounts as wanted.")
print(" ")
prePages = list(map(str, input("Please Enter your list of Theme Pages to Copy : ").split(", ")))
print(" ")
print("Double Check Entered Information")
for names in prePages:
    if(type(names) == str):
        print(names)
preCheck = input("Is this information correct?(y/n) : ")
clear()
class preLoop:
    if preCheck=="y":
        clear()
    elif preCheck=="n":
        print("----------------------------------")
        print("-- Kirkland Carson - InstaTheme --")
        print("----------------------------------")
        print(" ")
        prePages = list(map(str, input("Please Enter your list of Theme Pages to Copy : ").split(", ")))
        print(" ")
        print("Double Check Entered Information")
        for names in prePages:
            if(type(names) == str):
                print(names)
        preCheck = input("Is this information correct?(y/n) : ")
        if preCheck=="y":
            clear()
        else:
            print(" ")
            print("Attempts Maxed...")
            print("Please retry again...")
            print(" ")
            exit()
    else:
        print("Please use: 'y' or 'n'...")
        exit()
print("----------------------------------")
print("-- Kirkland Carson - InstaTheme --")
print("----------------------------------")
print(" ")
print("Starting Bot...")
print(" ")

class FoUf:
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
    
    #Now lets start following!
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(prePages[randint(0,len(prePages)-1)] + Keys.ENTER)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()    
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div").click()
    driver.implicitly_wait(5)

    htmlBadBoyToFollow = "/html/body/div[6]/div/div/div/div[2]/ul/div/li[1]/div/div[3]/button"   
    for i in range(2,12,1):
        htmlBadBoyToFollow = "/html/body/div[6]/div/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[3]/button"
        if(driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[3]/button").text == "Following"):
            # This is so we dont follow people we already follow- trust me this would cause issues otherwise
            continue               
        driver.find_element_by_xpath(htmlBadBoyToFollow).click()
        driver.implicitly_wait(5)
    
FoUf(typeUser, typePass, prePages)
