# coding=utf-8
import unittest

import time
from selenium import webdriver


class Test_taobao_login(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.PhantomJS()
        self.driver.maximize_window()
        self.driver.get('https://www.taobao.com/')
        self.driver.implicitly_wait(5)

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    def test_taobao_login_1(self):
        """淘宝登录界面-输入错误的密码"""
        self.driver.find_element_by_link_text(u'亲，请登录').click()
        self.driver.find_element_by_link_text(u'密码登录').click()
        time.sleep(5)
        self.driver.find_element_by_id("TPL_username_1").send_keys("15994213148")
        self.driver.find_element_by_id('TPL_password_1').send_keys('85602146hy')
        self.driver.find_element_by_id('J_SubmitStatic').click()
        time.sleep(3)

        assert self.driver.find_element_by_id('J_SubmitStatic').is_displayed()

    def test_taobao_login_2(self):
        """淘宝登录界面-输入空账号和空密码"""
        self.driver.find_element_by_link_text(u'亲，请登录').click()
        self.driver.find_element_by_link_text(u'密码登录').click()
        time.sleep(5)
        self.driver.find_element_by_id("TPL_username_1").clear()
        self.driver.find_element_by_id('TPL_password_1').clear()
        self.driver.find_element_by_id('J_SubmitStatic').click()
        time.sleep(3)

        assert self.driver.find_element_by_xpath("//div[@id='J_Message']//p[.='请输入账户名和密码']").is_displayed()



