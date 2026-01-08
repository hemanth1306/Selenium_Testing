import os
import logging
from DriverScript.BaseClass import BaseClass
from datetime import datetime
from FunctionLibraries.ApplicationLibrary.ApplicationSpecificFunctions import ApplicationSpecificFunctions
from FunctionLibraries.FrameworkLibrary.ReportGeneration import ReportGeneration


class Driver(BaseClass):
    def main(self):
        testexecutionstarttime=datetime.now()
        logging.info("Starting Test")
        testreportlist=[]
        testcnt=0
        failedcnt=0
        passedcnt=0
        result=None
        for elements in self.testCaseList:
            testcnt=testcnt+1
            testcasename=elements['testCaseName']
            testfunctionname=elements['Function']
            testdescription=elements['Description']
            testexpectedresult=elements['ExpectedResult']
            step=elements['TestCaseID']
            testcasestarttime=datetime.now()
            stepActual,resultbool=ApplicationSpecificFunctions.exceltofunctionmapping(testfunctionname,testcasename)
            if resultbool==True:
                result='Passed'
                print(f"{testcasename} : {result}")
                passedcnt=passedcnt+1
            elif resultbool==False:
                result='Failed'
                print(f"{testcasename} : {result}")
                failedcnt=failedcnt+1
            testcaseendtime=datetime.now()
            logging.info(f"{testcasename} : {testcaseendtime-testcasestarttime}")
            testcaseexecutiontime=testcaseendtime-testcasestarttime
            testreportlistdetails=[testcnt,testcasename,result,testcasestarttime,testcaseendtime,int(testcaseexecutiontime.total_seconds()),step,testdescription,testexpectedresult,result,stepActual]
            testreportlist.append(testreportlistdetails)
        testcaseexecutionendtime=datetime.now()
        logging.info('test execution completed')
        testtotalexecutiontime=testcaseexecutionendtime-testcaseexecutionendtime
        globalreportdetails=[testcnt,passedcnt,failedcnt,testexecutionstarttime,testcaseexecutionendtime,int(testtotalexecutiontime.total_seconds()),'PATHS']
        rpt=ReportGeneration()
        rpt.create_html_content(testreportlist, globalreportdetails)



if __name__ =="__main__":
    test=Driver()
    test.main()
