import base64
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

class FunctionDefinations():
    def __init__(self):
        self.driver=None

        self.stepActual=None
        self.result=None

    def loginToGmail(self,functionmapping):
        pass