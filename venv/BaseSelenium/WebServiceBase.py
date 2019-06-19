from time import sleep  # 从time中引入sleep
from selenium import webdriver  # 从selenium中引入webdriver
import operator       #首先要导入运算符模块
from Beans import EnumBase
import time
from selenium.webdriver.support.ui import WebDriverWait

#获取浏览器的函数
driver=None
def  getWebServiceBrowes(browseenum):
    # 选择打开的浏览器
    if (browseenum == 1):
        print("是否进入方法")
        driver = webdriver.Chrome()
        return driver
    elif (browseenum == 2):
        driver = webdriver.Firefox()
        return driver
    elif (browseenum == 3):
        driver = webdriver.Safari
        return driver
    elif (browseenum == 4):
        driver = webdriver.Safari
        return driver
    else:
        driver = webdriver.Chrome()
        return driver
        print("没有匹配的浏览器类型，默认是chrome")

# 浏览器窗口是否最大化
def getBrowseStyle(driver,maximize):
    # 是否最大化
    if (maximize == True):
        driver.maximize_window()
    else:
        print('使用默认')


# # 等待方式
def getConfigWaiteType(driver,waite_Type_enum,timeint):
    if (waite_Type_enum == 1):
        time.sleep(timeint)  #强制等待
    elif(waite_Type_enum == 2):
        driver.implicitly_wait(timeint)  # 隐性等待，最长等3秒
    else:
        print("默认设置20秒")
        driver.implicitly_wait(3)  # 隐性等待，最长等3秒

#  显示等待
def getWebDriverWait(driver,timeint,seleniumid):
    search=WebDriverWait(driver, timeint).until(lambda driver: driver.find_element_by_id("kw"))  # 显性等待，最长等3秒
    return search