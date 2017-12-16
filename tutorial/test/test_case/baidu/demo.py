# coding=utf-8
from selenium import webdriver

# 火狐配置文件地址
profile_directory = r"C:\Users\Huyue\AppData\Roaming\Mozilla\Firefox\Profiles\yn80ouvt.default"
# 火狐加载配置文件
profile = webdriver.FirefoxProfile(profile_directory)
# 火狐启动浏览器配置
dr = webdriver.Firefox(profile)


# option = webdriver.ChromeOptions()
# 伪装成iPhone登录浏览器触屏版
# option.add_argument("--user-agent = iphone")
# 伪装成Android登录
# option.add_argument("--user-agent = android")

# 加入谷歌浏览器配置地址
# option.add_argument("--user-data-dir = C:\Users\Huyue\AppData\Local\Google\Chrome\User Data")
# dr = webdriver.Chrome(chrome_options=option)
dr.maximize_window()
dr.implicitly_wait(5)

# 打开指定网址
dr.get("http://www.taobao.com/")
print(dr.title)


assert u"淘宝" in dr.title

# dr.quit()


