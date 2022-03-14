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

#We are going to need a BIT of information to even start... So lets start here!

#Lets Start with the login information
clear()
print("|--------------------------------------------------------|")
print("|------------| Kirkland Carson - InstaTheme |------------|")
print("|------------| For Account Sellers by Nerds |------------|")
print("|--------------------------------------------------------|")
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
        print("|--------------------------------------------------------|")
        print("|------------| Kirkland Carson - InstaTheme |------------|")
        print("|------------| For Account Sellers by Nerds |------------|")
        print("|--------------------------------------------------------|")
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
print("|--------------------------------------------------------|")
print("|------------| Kirkland Carson - InstaTheme |------------|")
print("|------------| For Account Sellers by Nerds |------------|")
print("|--------------------------------------------------------|")
print(" ")
print("Future Versions will Change this section to:")
print("If previously used acc: Skip This Section")
print("If new acc: Theme Template Selection")
print(" ")
print("Pre-Set List Example : jokezar, 6nics, shack, memelord, grapejuiceboys")
print(" ")
print("Add as many Pre-Set Accounts as desired.")
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
        print("|--------------------------------------------------------|")
        print("|------------| Kirkland Carson - InstaTheme |------------|")
        print("|------------| For Account Sellers by Nerds |------------|")
        print("|--------------------------------------------------------|")
        print(" ")
        prePages = list(map(str, input("Please Enter your list of Theme Pages to Copy : ").split(", ")))
        print(" ")
        print("Double Check Entered Information")
        for names in prePages:
            if(type(names) == str):
                print(names)
        preCheck = input("Is this information correct?(y/n) : ")
        if preCheck=="y":
            opt_select()
        else:
            print(" ")
            print("Attempts Maxed...")
            print("Please retry again...")
            print(" ")
            exit()
    else:
        print("Please use: 'y' or 'n'...")
        exit()

class opt_select:
    clear()
    print("|--------------------------------------------------------|")
    print("|------------| Kirkland Carson - InstaTheme |------------|")
    print("|------------| For Account Sellers by Nerds |------------|")
    print("|--------------------------------------------------------|")
    print("! WARNING !")
    print("Unfollowing/Following +60 per/hr, or +150 per/day (accounts) may cause:")
    print("Suspension/Ban interactions on account Temporarily to Permanent.")
    print(" ")
    print(" ")
    print("Please Select your Automation type : ")
    print(" ")
    print("1) Fully Automated Account for all bot functions")
    print("----- Used for little to no interaction with account. Full automated processes.")
    print(" ")
    print("2) Semi Automated Mode, call functions manually called for maximum control")
    print("----- Used for Automated processes, but full control and usage of account.")
    print(" ")
    opt_mode = input("Please type 'auto' or 'semi' to select : ")
    if opt_mode == "auto":
        clear()
        print("|--------------------------------------------------------|")
        print("|------------| Kirkland Carson - InstaTheme |------------|")
        print("|------------| For Account Sellers by Nerds |------------|")
        print("|--------------------------------------------------------|")
        print(" ")
        print("Selected:")
        print("Fully Automated Account...")
        print(" ")
        print("Now Loading Browser....")
        print(" ")
    elif opt_mode == "semi":
        clear()
        print("|--------------------------------------------------------|")
        print("|------------| Kirkland Carson - InstaTheme |------------|")
        print("|------------| For Account Sellers by Nerds |------------|")
        print("|--------------------------------------------------------|")
        print(" ")
        print("! WARNING !")
        print("Unfollowing/Following +60 per/hr, or +150 per/day (accounts) may cause:")
        print("Suspension/Ban interactions on account Temporarily to Permanent.")
        print(" ")
        print("Selected:")
        print("Semi-Automated Mode...")
        print(" ")
        print("Now Loading Options...")
        print(" ")
        time.sleep(random.randint(1, 5))
    else:
        print(" ")
        print("I'm sorry, that is not a valid input.")
        exit()

class foll_func:7
    clear()
    a

class unfo_func:
    clear()
    a

clear()
print("|--------------------------------------------------------|")
print("|------------| Kirkland Carson - InstaTheme |------------|")
print("|------------| For Account Sellers by Nerds |------------|")
print("|--------------------------------------------------------|")
print(" ")
print("Starting Browser...")
print(" ")
