from public import HTMLTestRunner
import time
import os
import unittest
from public import sendEmail
from base.read_config import get_config
import shutil
suite=unittest.TestSuite()
discover=unittest.defaultTestLoader.discover(get_config('DATABASE', 'testcase_address'), pattern='test*.py', top_level_dir=None)
for test_case in discover:
    for case_name in test_case:
        suite.addTest(case_name)
        print(case_name)
    print(test_case)
if __name__ == "__main__":
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    tdreport = get_config('DATABASE', 'report_address') + day
    reportfile=tdreport+"\\" + now + "_result.html"
    tdresult=get_config('DATABASE', 'result_address')+day
    if os.path.exists(tdreport):
        fp=open(reportfile,"wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="自动化接口测试报告",
                                               description="接口测试用例执行情况")
        runner.run(suite)
        fp.close()
    else:
        os.mkdir(tdreport)
        fp = open(reportfile, "wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               verbosity=2,
                                               title="自动化接口测试报告",
                                               description="接口测试用例执行情况")
        runner.run(suite)
        fp.close()
    if os.path.exists(tdresult):
        shutil.copy(sendEmail.get_NewFile(get_config('DATABASE', 'excel_address')),tdresult)
    else:
        os.mkdir(tdresult)
        shutil.copy(sendEmail.get_NewFile(get_config('DATABASE', 'excel_address')),tdresult)
    time.sleep(5)
    new_report=sendEmail.get_NewFile(tdreport)
    new_result=sendEmail.get_NewFile(tdresult)
    sendEmail.send_email(new_report,new_result)

    