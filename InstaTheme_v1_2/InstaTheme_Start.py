#!/usr/bin/python3
import time, sys, os, random, getpass
import selenium
import modules.fouf_v1
from modules.fouf_v1 import FoUf
import modules.functions.scrape
from modules.functions.scrape import scrape
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

###################################################################################
# calls section ###################################################################
###################################################################################
clear = lambda: os.system('clear')
impFoUf = FoUf()
impScrape = scrape()

def call_ascii(fn):
    f = open('ascii_logo.txt','r')
    print(''.join([line for line in f]))

def main():
    clear()
    call_ascii('ascii_logo.txt')
    print(" ")
    print(" ")

    accChk = ["new", "old"]
    modeChk = ["auto", "semi", "ver"]
    preChk = ["custom", "default"]
    descChk = ["yes", "no"]

    ###################################################################################
    # login section ###################################################################
    ###################################################################################

    print("InstaTheme Account Login/Signup")
    print("")
    print("Are you a NEW or RETURNING user?")

    while True:
        acc_opt = input("Please type 'new' or 'old' : ")
        if acc_opt in accChk:
            break
        else:
            print('Please write only valid options : ', ",".join(accChk))

    if acc_opt == ("new"):
        clear()
        call_ascii('ascii_logo.txt')
        print(" ")
        print(" ")
        print("InstaTheme Account Registration")
        print(" ")
        print("Instagram Account info... ")
        print(" ")
        userNew = input("Instagram Username : ")
        passNew = input("Instagram Password : ")
        
        ###################################################################################
        # Bot selection ###################################################################
        ###################################################################################

        clear()
        call_ascii('ascii_logo.txt')
        print(" ")
        print(" ")
        print("InstaTheme Bot Selection:")
        print(" ")
        print("1) Fully Automated : 100% Bot run, no human interaction needed.")
        print("2) Semi Automated : Automated scripts at your disposal, whenever!")
        print(" ")
        while True:
            modeNew = input("'auto' or 'semi' (for version 1.x type 'ver') : ")
            if modeNew in modeChk:
                break
            else:
                print('Please write only valid options : ', ",".join(modeChk))
                
        ###################################################################################
        # Theme selection #################################################################
        ###################################################################################

        while True:
            clear()
            call_ascii('ascii_logo.txt')
            print(" ")
            print(" ")
            print("InstaTheme Theme selection:")
            print(" ")
            print("Would you like a Default or Custom theme?")
            preNew = input("'custom' or 'default' : ")
            if preNew in preChk:
                break
            else:
                print('Please write only valid options : ', ",".join(preChk))
        if preNew == ("custom"):
            clear()
            call_ascii('ascii_logo.txt')
            print(" ")
            print(" ")
            print("List Accounts to add to your watch list!")
            print(" ")
            print("Please use this format: 'name1,name2,name3,name4'")
            print("(improper format will make some functions not work, or crash bot.)")
            print(" ")
            preCust = input("Accounts : ")
        elif preNew == ("default"):
            preCust = ("notadamcarson,holesomememes,iphymeme,xinggan.shoes")
        else:
            print("No List Selected.")
            print(" ")
            print("Some features may not work, and cause crashes.")
            print(" ")
            print("To change this, edit the config file in your config folder.")
            print(" ")
            print(" ")
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            print(" ")
            print(" ")
            
        ###################################################################################
        # Write new Config ################################################################
        ###################################################################################

        fileEdit = open("config/config_"+(userNew), "w+")
        fileEdit.write(userNew + ":" + passNew)
        fileEdit.write("\n")
        fileEdit.write(modeNew)
        fileEdit.write("\n")
        fileEdit.write(preCust)
        fileEdit.close()

        ###################################################################################
        # Auto Start new accounts #########################################################
        ###################################################################################
        #if modeNew == ("auto"):
        #    print("auto")
        #elif modeNew == ("semi"):
        #    print("semi")
        #elif modeNew == ("ver"):
        #    impFoUf.userName = userNew
        #    impFoUf.userPass = passNew
        #    impFoUf.userCust = preCust
        #    impFoUf.main()
        #else:
        #    print("You have not selected a Bot Mode.")
        #    print("Please edit your config file.")
        #    print(" ")
        #    print("Config File Example:")
        #    print("user:pass")
        #    print("auto <- This will be 'auto' or 'semi'")
        #    print("list,of,page,names,here")
        #    print(" ")
        #    print(" ")
        #    exit()
        #
        ###################################################################################
        # Finished Registry ###############################################################
        ###################################################################################

    elif acc_opt == ("old"):
        clear()
        call_ascii('ascii_logo.txt')
        print(" ")
        print(" ")
        print("InstaTheme Account Sign-In")
        print(" ")
        print(" ")
        userScan = input("Username : ")
        
        with open("config/config_"+(userScan), "r") as conf:
            parConf = conf.read().splitlines()
            userParse = list(map(str, parConf[0].split(":")))
            userName = userParse[0]
            userPass = userParse[1]
            userMode = parConf[1]
            userCust = parConf[2]
        
            if userMode == ("auto"):
                print("auto")
            elif userMode == ("semi"):
                print("semi")
            elif userMode == ("ver"):
                impFoUf.userName = userName
                impFoUf.userPass = userPass
                impFoUf.userCust = userCust
                impScrape.userName = userName
                impScrape.userPass = userPass
                impScrape.userCust = userCust
                while True:
                    impFoUf.main()
                    #impScrape.main()
                    time.sleep(2700)
            else:
                print("You have not selected a Bot Mode.")
                print("Please edit your config file.")
                print(" ")
                print("Config File Example:")
                print("user:pass")
                print("auto <- This will be 'auto' or 'semi'")
                print("list,of,page,names,here")
                print(" ")
                print(" ")
                exit()
    else:
        exit()
        
if __name__ == "__main__":
    impFoUf = FoUf()
    impScrape = scrape()
    
    # Set usernames
    impFoUf.userName = ""
    impFoUf.userPass = ""
    impFoUf.userCust = []
    impScrape.userName = ""
    impScrape.userPass = ""
    impScrape.userCust = []

    main()
