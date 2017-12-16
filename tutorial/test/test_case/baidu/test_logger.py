# coding:utf-8
import unittest
import time

import sys
from selenium import webdriver

from common.logger import Log

log = Log()


class Test_logger(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(30)

    def test_logger(self):
        log.info("-------测试用例开始---------")
        # 从方法内部获取方法名称
        print sys._getframe().f_code.co_name

        self.driver.find_element_by_id("kw").send_keys("yoyo")
        log.info("输入内容：yoyo")
        self.driver.find_element_by_id("su").click()
        log.info("点击按钮：id = su")
        time.sleep(2)
        t = self.driver.title
        log.info(u"获取title内容：%s" % t)
        self.assertIn(u"百度搜索", t)

    def tearDown(self):
        self.driver.quit()
        log.info("-------测试用例结束----------")

