import  logging
import os
import socket
import getpass
import platform
from datetime import datetime


class ReportGeneration:

            def create_html_content(self, testReportList, globalreportdetails):
                host_Name = socket.gethostname()
                Executed_By = getpass.getuser()
                operatingSystem = platform.system() + " " + platform.release()

                totaltestCasescnt = globalreportdetails[0]
                totalPassedcnt = globalreportdetails[1]
                totalFailedcnt = globalreportdetails[2]

                testStartTime = globalreportdetails[3].strftime("%Y-%m-%d %H:%M:%S")
                testEndTime = globalreportdetails[4].strftime("%Y-%m-%d %H:%M:%S")
                totalDuration = globalreportdetails[5]
                environment = globalreportdetails[6]

                # print(environment)

                with open(
                        os.getenv("project_path")
                        + "\\Configurations\\ReportUtility\\HTMLInitialization.txt",
                        "r"
                ) as reader:
                    html_content1 = reader.readlines()

                html_content2 = "".join(html_content1)
                html_content2 = html_content2 + """<!DOCTYPE html>
                <table style="width: 100%; font-family: Calibri; font-size: medium;">
                    <tr>
                        <td class="style1" style="background-color: #D6EBFC">Host</td>
                        <td class="style2">""" + host_Name + """</td>
                        <td class="style3" style="background-color: #D6EBFC">Total Test Cases</td>
                        <td id="TotalManualCaseCount">""" + str(totaltestCasescnt) + """</td>
                    </tr>
                    <tr>
                        <td class="style1" style="background-color: #D6EBFC">Executed By</td>
                        <td class="style2">""" + Executed_By + """</td>
                        <td class="style3" style="background-color: #D6EBFC">Test Cases Passed</td>
                        <td id="PassedManualCaseCount">""" + str(totalPassedcnt) + """</td>
                    </tr>
                    <tr>
                        <td class="style1" style="background-color: #D6EBFC">Operating System</td>
                        <td class="style2">""" + operatingSystem + """</td>
                        <td class="style3" style="background-color: #D6EBFC">Test Cases Failed</td>
                        <td id="FailedManualCaseCount">""" + str(totalFailedcnt) + """</td>
                    </tr>
                    <tr>
                        <td class="style1" style="background-color: #D6EBFC">Start Time</td>
                        <td class="style2">""" + testStartTime + """</td>
                        <td class="style1" style="background-color: #D6EBFC">End Time</td>
                        <td class="style2">""" + testEndTime + """</td>
                    </tr>
                    <tr>
                        <td class="style1" style="background-color: #D6EBFC">Total Duration (Seconds)</td>
                        <td class="style2">""" + str(totalDuration) + """</td>
                        <td class="style1" style="background-color: #D6EBFC">Environment</td>
                        <td class="style2">""" + environment + """</td>
                    </tr>
                </table>
                <td class="style1" style="background-color: #D6EBFC">Operating System</td>
<td class="style2">""" + operatingSystem + """</td>
<td class="style3" style="background-color: #D6EBFC">Test Cases Failed</td>
<td id="FailedManualCaseCount">""" + str(totalFailedcnt) + """</td>
</tr>

<tr>
    <td class="style1" style="background-color: #D6EBFC">Start Time</td>
    <td class="style2">""" + testStartTime + """</td>
    <td class="style1" style="background-color: #D6EBFC">End Time</td>
    <td class="style2">""" + testEndTime + """</td>
</tr>

<tr>
    <td class="style1" style="background-color: #D6EBFC">Total Duration (Seconds)</td>
    <td class="style2">""" + str(totalDuration) + """</td>
    <td class="style1" style="background-color: #D6EBFC">Environment</td>
    <td class="style2">""" + environment + """</td>
</tr>
</table>

<p style="font-family: Microsoft Sans Serif; font-size: x-large;
font-weight: bolder; text-decoration: underline;">
    Overview - Test Cases
</p>

<table style="padding: 0px; width: 100%; border-spacing: 0px;">
<tr>
    <th style="vertical-align: middle; text-align: center; font-family: Calibri;
        padding: 0px; margin: 0px; background-color: #007CAC; color: #FFFFFF;
        font-weight: bold; font-size: large;" class="style6">
        &nbsp;
    </th>

    <th style="vertical-align: middle; text-align: center; font-family: Calibri;
        padding: 0px; margin: 0px; background-color: #007CAC; color: #FFFFFF;
        font-weight: bold; font-size: large;" class="style5">
        S.No
    </th>

    <th style="vertical-align: middle; text-align: center; font-family: Calibri;
        padding: 0px; margin: 0px; background-color: #007CAC; color: #FFFFFF;
        font-weight: bold; font-size: large;" class="style7">
        Test Case Name
    </th>

    <th style="vertical-align: middle; text-align: center; font-family: Calibri;
        padding: 0px; margin: 0px; background-color: #007CAC; color: #FFFFFF;
        font-weight: bold; font-size: large;" class="style4">
        Result
    </th>

    <th style="vertical-align: middle; text-align: center; font-family: Calibri;
        padding: 0px; margin: 0px; background-color: #007CAC; color: #FFFFFF;
        font-weight: bold; font-size: large;">
        Duration (Seconds)
    </th>
</tr>
"""
                html_test_content = ""
                testcnt = 0

                for test in testReportList:
                    testcnt = testcnt + 1

                    if testcnt % 2 == 0:
                        bgc = "#D6EBFC"
                    else:
                        bgc = "#FFFFFF"

                    if test[2] == "Passed":
                        html_test_content = html_test_content + """
                        <tr>
                            <td id="main-""" + str(testcnt) + """"
                                style="vertical-align: middle; text-align: center; font-family: Calibri;
                                padding: 0px; margin: 0px; background-color: """ + bgc + """;">
                                &nbsp;
                                <a href="javascript:void(0)"
                                   onclick="toggle('subitem-""" + str(testcnt) + """,open')" class="style7>+</a>&nbsp;
                            </td>

                            <td style="vertical-align: middle; text-align: center; font-family: Calibri;
                                padding: 0px; margin: 0px; background-color: """ + bgc + """;">
                                """ + str(test[0]) + """
                            </td>

                            <td style="vertical-align: middle; text-align: center; font-family: Calibri;
                                padding: 0px; margin: 0px; background-color: """ + bgc + """;">
                                """ + test[1] + """
                            </td>

                            <td style="vertical-align: middle; text-align: center; font-family: Calibri;
                                padding: 0px; margin: 0px; background-color: """ + bgc + """; color:#008000;">
                                """ + test[2] + """
                            </td>

                            <td style="vertical-align: middle; text-align: center; font-family: Calibri;
                                padding: 0px; margin: 0px; background-color: """ + bgc + """;">
                                """ + str(test[3]) + """
                            </td>
                        </tr>

                        <tr id="subitem-""" + str(testcnt) + """" style="display:none;">
                            <td colspan="5"
                                style="vertical-align: middle; text-align: center; font-family: Calibri;
                                margin: 0px; background-color: """ + bgc + """;">

                            <p style="font-family: 'Trebuchet MS'; font-size: small; font-weight: bold;
                                text-decoration: underline; text-align: left;">
                                Iteration 1
                            </p>

                            <table align="center"
                                   style="border-style: ridge; border-width: 2px;
                                   width:95%; cellpadding:0; cellspacing:0;">

                                <tr>
                                    <th width="5%" style="border-style: solid; border-width: 1px;
                                        background-color: #0085F0;">Step No</th>

                                    <th width="10%" style="border-style: solid; border-width: 1px;
                                        background-color: #0085F0;">Step Name</th>

                                    <th width="20%" style="border-style: solid; border-width: 1px;
                                        background-color: #0085F0;">Step Description</th>

                                    <th width="35%" style="border-style: solid; border-width: 1px;
                                        background-color: #0085F0;">Expected Results</th>

                                    <th width="10%" style="border-style: solid; border-width: 1px;
                                        background-color: #0085F0;">Status</th>

                                    <th style="border-style: solid; border-width: 1px;
                                        background-color: #0085F0;">Actual Results</th>
                                </tr>

                                <tr>
                                    <td style="border-style: solid; border-width: 1px;">1</td>
                                    <td style="border-style: solid; border-width: 1px;">""" + test[4] + """</td>
                                    <td style="border-style: solid; text-align: left; border-width: 1px;">
                                        """ + test[5] + """
                                    </td>
                                    <td style="border-style: solid; text-align: left; border-width: 1px;">
                                        """ + test[6] + """
                                    </td>
                                    <td style="border-style: solid; border-width: 1px;">Passed</td>
                                    <td style="border-style: solid; text-align: left; border-width: 1px;
                                        color:#008000;">
                                        """ + test[8] + """
                                    </td>
                                </tr>
                            </table>
                            </td>
                        </tr>
                        """
                    elif test[2] == "Failed":

                        html_test_content = html_test_content + """
                            <tr>
                                <td id="main-""" + str(testcnt) + """"
                                    style="vertical-align: middle; text-align: center; font-family: Calibri;
                                    padding: 0px; margin: 0px; background-color: """ + bgc + """;">
                                    &nbsp;
                                    <a href="javascript:void(0)"
                                       onclick="toggle('subitem-""" + str(testcnt) + """,open')" class="style7>+</a>&nbsp;
                                </td>

                                <td style="vertical-align: middle; text-align: center; font-family: Calibri;
                                    padding: 0px; margin: 0px; background-color: """ + bgc + """;">
                                    """ + str(test[0]) + """
                                </td>

                                <td style="vertical-align: middle; text-align: center; font-family: Calibri;
                                    padding: 0px; margin: 0px; background-color: """ + bgc + """;">
                                    """ + test[1] + """
                                </td>

                                <td style="vertical-align: middle; text-align: center; font-family: Calibri;
                                    padding: 0px; margin: 0px; background-color: """ + bgc + """; color:#FF0000;">
                                    """ + test[2] + """
                                </td>

                                <td style="vertical-align: middle; text-align: center; font-family: Calibri;
                                    padding: 0px; margin: 0px; background-color: """ + bgc + """;">
                                    """ + str(test[3]) + """
                                </td>
                            </tr>

                            <tr id="subitem-""" + str(testcnt) + """" style="display:none;">
                                <td colspan="5"
                                    style="vertical-align: middle; text-align: center; font-family: Calibri;
                                    margin: 0px; background-color: """ + bgc + """;">

                                <p style="font-family: 'Trebuchet MS'; font-size: small; font-weight: bold;
                                    text-decoration: underline; text-align: left;">
                                    Iteration 1
                                </p>

                                <table align="center"
                                       style="border-style: ridge; border-width: 2px;
                                       width:95%; cellpadding:0; cellspacing:0;">

                                    <tr>
                                        <th width="5%" style="border-style: solid; border-width: 1px;
                                            background-color: #0085F0;">Step No</th>

                                        <th width="10%" style="border-style: solid; border-width: 1px;
                                            background-color: #0085F0;">Step Name</th>

                                        <th width="20%" style="border-style: solid; border-width: 1px;
                                            background-color: #0085F0;">Step Description</th>

                                        <th width="35%" style="border-style: solid; border-width: 1px;
                                            background-color: #0085F0;">Expected Results</th>

                                        <th width="10%" style="border-style: solid; border-width: 1px;
                                            background-color: #0085F0;">Status</th>

                                        <th style="border-style: solid; border-width: 1px;
                                            background-color: #0085F0;">Actual Results</th>
                                    </tr>

                                    <tr>
                                        <td style="border-style: solid; border-width: 1px;">1</td>
                                        <td style="border-style: solid; border-width: 1px;">""" + test[4] + """</td>
                                        <td style="border-style: solid; text-align: left; border-width: 1px;">
                                            """ + test[5] + """
                                        </td>
                                        <td style="border-style: solid; text-align: left; border-width: 1px;">
                                            """ + test[6] + """
                                        </td>
                                        <td style="border-style: solid; border-width: 1px; color:#FF0000;">
                                            Failed
                                        </td>
                                        <td style="border-style: solid; text-align: left; border-width: 1px;
                                            color:#FF0000;">
                                            """ + test[8] + """
                                        </td>
                                    </tr>
                                </table>
                                </td>
                            </tr>
                            """
                html_test_content = html_test_content + """
                </table>
                <p align='center'>Limited Access</p>
                </body>
                </html>
                """
                html_content2 = html_content2 + html_test_content

                # print(html_content2)
                self.create_html_file(html_content2)

            def create_html_file(self, html_content):
                current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
                print(os.getenv('report_path'))
                folderpath = os.getenv("report_path")
                filename = os.path.join(
                    folderpath,
                    "Execution_Result_" + current_time + ".html"
                )

                try:
                    with open(filename, "w") as file:
                        file.write(html_content)

                    # print(f"HTML file '{filename}' created successfully.")
                    logging.info(
                        f"HTML file '{filename}' created successfully."
                    )

                except Exception as e:
                    print(f"An error occurred: {e}")
                    logging.exception("An unexpected Error Occur")



