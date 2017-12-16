# coding=utf-8
import unittest

import time
from selenium import webdriver


class Test_taobao_search(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.PhantomJS()
        self.driver.maximize_window()
        self.driver.get('https://www.taobao.com/')
        self.driver.implicitly_wait(8)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_taobao_search(self):
        """淘宝首页-搜索框输入搜索物品"""
        self.driver.find_element_by_id("q").send_keys(u"家用摄像头")
        self.driver.find_element_by_css_selector("button.btn-search.tb-bg").click()
        time.sleep(5)
        title = self.driver.title
        print(title)

        self.assertTrue(u"家用摄像头" in title)