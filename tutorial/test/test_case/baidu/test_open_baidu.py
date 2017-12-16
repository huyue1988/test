# coding=utf-8
import unittest
import time

import sys
from selenium import webdriver


class Test_open_baidu(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.PhantomJS()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com/')
        # self.driver.implicitly_wait(8)

    def tearDown(self):
        time.sleep(2)
        t = time.time() - self.startTime
        print "%s: %.3f" %(self.id(), t)
        self.driver.quit()

    def test_open_baidu(self):
        """登录百度首页"""
        # # 获取此方法的名称
        # print sys._getframe().f_code.co_name
        title = self.driver.title
        print(title)
        print(self.id())

        self.assertTrue(u"百度一下就好" in title)

