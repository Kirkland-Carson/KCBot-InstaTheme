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
