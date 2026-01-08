from DriverScript.BaseClass import BaseClass
from FunctionLibraries.ApplicationLibrary.functiondefinations import FunctionDefinations



class ApplicationSpecificFunctions():
    @staticmethod
    def exceltofunctionmapping(functionname,testcasename):
        fn=FunctionDefinations()
        functionmapping=None
        stepActual=None
        functionAction=None
        if functionname.find(">>")>0:
            functiondetails=functionname.split(">>")
            functionAction=functiondetails[0]
            functionmapping=functiondetails[1]
        else:
            functionAction=functionname

        if functionAction=='LOGIN_TO_DEMOQA':
            stepActual,result=fn.navigatedemoqa(functionmapping,testcasename)
        return stepActual,result
