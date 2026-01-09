import logging
import os
import socket
import getpass
import platform
from datetime import datetime


def normalize(value):
    """
    Converts any value into a safe string for HTML reports.
    Prevents datetime / None / int concatenation issues permanently.
    """
    if value is None:
        return ""
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return str(value)


class ReportGeneration:

    def create_html_content(self, testreportlistdetails, globalreportdetails):

        host_Name = socket.gethostname()
        Executed_By = getpass.getuser()
        operatingSystem = platform.system() + " " + platform.release()

        totaltestCasescnt = normalize(globalreportdetails[0])
        totalPassedcnt = normalize(globalreportdetails[1])
        totalFailedcnt = normalize(globalreportdetails[2])
        testStartTime = normalize(globalreportdetails[3])
        testEndTime = normalize(globalreportdetails[4])
        totalDuration = normalize(globalreportdetails[5])
        environment = normalize(globalreportdetails[6])

        with open(
            os.getenv("project_path")
            + "\\Configurations\\ReportUtility\\HTMLInitialization.txt",
            "r"
        ) as reader:
            html_content2 = "".join(reader.readlines())

        # 🔹 ADD TOGGLE JAVASCRIPT (MANDATORY)
        html_content2 += f"""
<!DOCTYPE html>

<script type="text/javascript">
function toggle(id, el) {{
    var row = document.getElementById(id);
    if (!row) return;

    if (row.style.display === "none" || row.style.display === "") {{
        row.style.display = "table-row";
        el.innerHTML = "-";
    }} else {{
        row.style.display = "none";
        el.innerHTML = "+";
    }}
}}
</script>

<table style="width:100%; font-family:Calibri; font-size:medium;">
<tr>
    <td class="style1">Host</td><td>{host_Name}</td>
    <td class="style1">Total Test Cases</td><td>{totaltestCasescnt}</td>
</tr>
<tr>
    <td class="style1">Executed By</td><td>{Executed_By}</td>
    <td class="style1">Test Cases Passed</td><td>{totalPassedcnt}</td>
</tr>
<tr>
    <td class="style1">Operating System</td><td>{operatingSystem}</td>
    <td class="style1">Test Cases Failed</td><td>{totalFailedcnt}</td>
</tr>
<tr>
    <td class="style1">Start Time</td><td>{testStartTime}</td>
    <td class="style1">End Time</td><td>{testEndTime}</td>
</tr>
<tr>
    <td class="style1">Total Duration (Seconds)</td><td>{totalDuration}</td>
    <td class="style1">Environment</td><td>{environment}</td>
</tr>
</table>

<p style="font-size:x-large; font-weight:bold; text-decoration:underline;">
Overview - Test Cases
</p>

<table style="width:100%; border-spacing:0;">
<tr style="background:#007CAC; color:#FFF;">
    <th></th>
    <th>S.No</th>
    <th>Test Case Name</th>
    <th>Result</th>
    <th>Duration (Seconds)</th>
</tr>
"""

        # 🔒 NORMALIZE TEST DATA (PERMANENT FIX)
        normalized_tests = []
       # print(type(testreportlistdetails))
        #print("testReportList", testreportlistdetails)
        #print("length", len(testreportlistdetails))
        for t in testreportlistdetails:

            #print(type(testreportlistdetails))
           # print("testReportList", testreportlistdetails)
            #print("length", len(testreportlistdetails))
            #normalized_tests.append([
             #   normalize(t[i]) if i < len(t) else "" for i in range(9)
            #])
            normalized_tests.append([normalize(x) for x in t])
            #print("normalized_tests", normalized_tests)
        html_test_content = ""
        testcnt = 0

        for test in normalized_tests:
            print("test", test)
            testcnt += 1
            bgc = "#D6EBFC" if testcnt % 2 == 0 else "#FFFFFF"
            status_color = "#008000" if test[2] == "Passed" else "#FF0000"

            html_test_content += f"""
<tr>
    <td style="text-align:center; background:{bgc};">
        <a href="javascript:void(0)"
           onclick="toggle('subitem-{testcnt}', this)">+</a>
    </td>

    <td style="background:{bgc}; text-align:center;">{test[0]}</td>
    <td style="background:{bgc}; text-align:center;">{test[1]}</td>
    <td style="background:{bgc}; text-align:center; color:{status_color};">
        {test[2]}
    </td>
    <td style="background:{bgc}; text-align:center;">{test[5]}</td>
</tr>

<tr id="subitem-{testcnt}" style="display:none;">
<td colspan="5" style="background:{bgc};">
<table width="95%" border="1" align="center">
<tr style="background:#0085F0; color:#FFF;">
    <th>Step</th>
    <th>Description</th>
    <th>Expected</th>
    <th>Status</th>
    <th>Actual</th>
</tr>
<tr>
    <td>{test[6]}</td>
    <td>{test[7]}</td>
    <td>{test[8]}</td>
    <td style="color:{status_color};">{test[2]}</td>
    <td>{test[9]}</td>
</tr>
</table>
</td>
</tr>
"""

        html_content2 += html_test_content + """
</table>
<p align="center">Limited Access</p>
</body>
</html>
"""

        self.create_html_file(html_content2)

    def create_html_file(self, html_content):
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        folderpath = os.getenv("report_path")

        filename = os.path.join(
            folderpath,
            f"Execution_Result_{current_time}.html"
        )

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(html_content)
            logging.info(f"HTML report created successfully: {filename}")
        except Exception:
            logging.exception("Error creating HTML report")
