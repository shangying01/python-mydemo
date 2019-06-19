# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.maximize_window()  # 浏览器窗口最大化
# driver.implicitly_wait(3)  # 隐式等待
# driver.get("https://www.baidu.com")  # 获取URL，打开页面
# search = driver.find_element_by_id("kw")  # 通过id定位搜索框
# search.send_keys("selenium")  # 填入"selenium"
# sleep(5)  # 直接等待
# driver.quit()  # 退出相关浏览器
from Beans import EnumBase
from BaseSelenium import WebServiceBase
from BaseSelenium import FindSeleniumMethods
import time
from selenium.webdriver.support.ui import WebDriverWait
driver=WebServiceBase.getWebServiceBrowes(EnumBase.Browse['CHROME'])
WebServiceBase.getBrowseStyle(driver,True)
WebServiceBase.getConfigWaiteType(driver,EnumBase.Waite_Type['IMPLICITLY_WAIT'],3)
driver.get("https://www.baidu.com")  # 获取URL，打开页面
# search = driver.find_element_by_id("kw")  # 通过id定位搜索框
# search=FindSeleniumMethods.getFindElementType(driver,EnumBase.Element_Type['ID'],'kw')
# driver.find_element_by_link_text()
# driver.find_element_by_partial_link_text()
# driver.find_element_by_class_name()
# driver.find_element_by_css_selector()
name="kw1"
search=driver.find_element_by_xpath(".//*[@id='"+name+"']")
# search=FindSeleniumMethods.getFindElementXpath(driver,EnumBase.Element_Xpath_Type['CONTAIN'],name)
# search=driver.find_element_by_xpath(".//*[contains(@id,'"+name+"')]")
# driver.find_element_by_tag_name()
# driver.find_element()
# search=WebServiceBase.getWebDriverWait(driver,10,name)
# values=FindSeleniumMethods.setKeys(driver,EnumBase.Element_Set_Keys['SETKEY'],search,"",'163')
# FindSeleniumMethods.setKeys(driver,EnumBase.Element_Set_Keys['SELENIUM_SETKEY'],"",name,'163',1)
values=search.send_keys("163")  # 填入"selenium"
# search.submit()
# search.clear()
# search.click()
# search.is_selected()
# search.is_displayed()

print('打印结果---》》',values)
# driver.find_element_by_xpath()
# WebServiceBase.getConfigWaiteType(driver,EnumBase.Waite_Type['SLEEP'],10)
time.sleep(10)
driver.quit()  # 退出相关浏览器





