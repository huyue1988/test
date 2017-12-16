# coding=utf-8
import HTMLTestRunner
import os
import unittest
import time
import sys

# 避免执行此脚本时报错:No handlers could be found for logger "selenium.webdriver.remote.remote_connection"
reload(sys)
sys.setdefaultencoding('utf8')

# 设置测试用例路径
case_path = os.path.join(os.getcwd(), "test_case")
# 设置测试报告路径
report_path = os.path.join(os.getcwd(), "test_report\\")
# 获取系统当前时间
now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
# html报告文件路径
result_file = report_path + now + '_Result.html'


def all_case():
    # 构建suite
    suite = unittest.defaultTestLoader.discover(case_path)
    print(suite)
    return suite


if __name__ == "__main__":
    fp = open(result_file, "wb")
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u"用例执行情况：", verbosity=2)
    # 开始执行测试套件,run所有用例
    runner.run(all_case())
    fp.close()
