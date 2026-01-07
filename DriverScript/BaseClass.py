import sys
import cx_Oracle
import pandas as pd
from datetime import datetime
import logging
import os
import openpyxl
from pathlib import Path


class BaseClass:
    def __init__(self):
        self.conn=None
        self.initialize_variable()
        os.environ['project_path'] = self.project_path
        self.testCaseList=self.get_testcase_list()

    def initialize_variable(self):
        try:
            execution_path =os.environ['project_path']+'//Configutrations//TestExecution.xlsx'   
            wb = openpyxl.load_workbook(execution_path)
            ws = wb['GlobalConfig']
            os.environ['BrowserType'] = ws['A2'].value
            os.environ['Headlessmode'] = ws['B2'].value
            wb.close()
            configpath = os.environ['project_path'] + '//Configutrations//GlobalConfiguration.ini'
            config=configparser.ConfigParser()
            config.read(configpath)
            for key in config['PATHS']:
                os.environ[key]=config['PATHS'][key]
            cx_Oracle.init_oracle_client(    