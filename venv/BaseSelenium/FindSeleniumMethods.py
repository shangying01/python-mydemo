from selenium import webdriver  # 从selenium中引入webdriver
from Beans import EnumBase
import selenium.common.exceptions

'''
driver webdriver对象
type,根据类型，获取值
type_name,元素的值
search，返回获取的元素参数
'''
def getFindElementType(driver,type,type_name):
    if(type == 1):
        search=driver.find_element_by_id(type_name)
        return search
    elif(type == 2):
        search = driver.find_element_by_name(type_name)
        return search
    elif (type == 3):
        search = driver.find_element_by_xpath(".//*[@id='"+type_name+"']")
        return search
    elif (type == 4):
        search = driver.find_element_by_link_text(type_name)
        return search
    elif (type == 5):
        search = driver.find_element_by_partial_link_text(type_name)
        return search
    elif (type == 6):
        search = driver.find_element_by_class_name(type_name)
        return search
    elif (type == 7):
        search = driver.find_element_by_css_selector(type_name)
        return search
    elif (type == 8):
        search = driver.find_element_by_tag_name(type_name)
        return search
    elif (type == 9):
        search = driver.find_element(By.ID,type_name)
        return search
    else:
        print('没有合适的类型')
        search='没有合适的类型'
        return search


'''
driver webdriver对象
type,根据类型，获取值
type_name,元素的值
search，返回获取的元素参数
'''
def getFindElementTypeValue(driver,type,type_name,value):
    if(type == 1):
        values=driver.find_element_by_id(type_name).send_keys(value)
        return values
    elif(type == 2):
        values = driver.find_element_by_name(type_name).send_keys(value)
        return values
    elif (type == 3):
        values = driver.find_element_by_xpath(".//*[@id='"+type_name+"']").send_keys(value)
        return values
    elif (type == 4):
        values = driver.find_element_by_link_text(type_name).send_keys(value)
        return values
    elif (type == 5):
        values = driver.find_element_by_partial_link_text(type_name).send_keys(value)
        return values
    elif (type == 6):
        values = driver.find_element_by_class_name(type_name).send_keys(value)
        return values
    elif (type == 7):
        values = driver.find_element_by_css_selector(type_name).send_keys(value)
        return values
    elif (type == 8):
        values = driver.find_element_by_tag_name(type_name).send_keys(value)
        return values
    elif (type == 9):
        values = driver.find_element(By.ID,type_name).send_keys(value)
        return values
    else:
        values='没有合适的类型???'
        return values

'''
driver webdriver对象
type,元素赋值方式
search,允许空“”，设置值的元素对象
name,元素名称，允许空“”
value，元素的值
values，返回值
'''

def setKeys(driver,type,search,name,value,type1):
    if(type == 1):
        values=search.send_keys(value)
        return values
    elif (type == 2):
        try:
            values=getFindElementTypeValue(driver, type1, name,value)
            return values
        except selenium.common.exceptions.NoSuchElementException:
            type1+=1
            print("没有找到合适的元素方式类型", "打印type1的值", type1)
            if(type1<=8):
              setKeys(driver,type,search,name,value,type1)
            else:
              print("没有合适的类型--")
              values='没有合适的类型!!!!!!'
              # raise  #这里的raise代表终止后续的继续，不注释则抛出异常，注释后则不抛出异常
              print('看不到')
              driver.quit()
              return values
    else:
        print("类型不存在！！！")
        values='类型不存在！！！'
        return values
'''
driver webdriver对象
type,根据类型，获取值
type_name,元素的值
search，返回获取的元素参数
通过path获取页面元素

'''
def getFindElementXpath(driver,type,type_name):
    if(type == 1):
        search=driver.find_element_by_xpath(".//*[start-with(@id,'"+type_name+"')]")
        return search
    elif (type == 2):
        search= driver.find_element_by_xpath(".//*[ends-with(@id,'"+type_name+"')]")
        return search
    elif (type == 3):
        search= driver.find_element_by_xpath(".//*[contains(@id,'"+type_name+"')]")
        return search
    elif (type == 4):
        search= driver.find_element_by_xpath(".//*[@id='"+type_name+"']")
        return search
    elif (type == 5):
        search= driver.find_element_by_xpath(".//*[@name='"+type_name+"']")
        return search
    elif (type == 6):
        search= driver.find_element_by_xpath(".//*[@type='"+type_name+"']")
        return search
    elif (type == 6):
        search= driver.find_element_by_xpath(".//*[@class='"+type_name+"']")
        return search
    else:
        print("类型不存在！！！")
        search='类型不存在！！！'
        return search


'''
type,根据类型，获取值
search，返回获取的元素参数
name, 设置内容值
提交按钮事件
'''
def getElementOperateEvent(type,search,name):
    if(type == 1):
        search.clear()
    elif (type == 2):
        search.send_keys(name)
    elif (type == 3):
        search.click()
    elif (type == 4):
        search.submit()
    elif (type == 5):
        search.submit()
    elif (type == 6):
        search.submit()
    elif (type == 7):
        search.submit()
    elif (type == 8):
        search.submit()
    else:
        print("类型不存在！！！")

'''
driver webdriver对象
type 事件类型
driver的操作事件

'''
def getDriverOperateEvent(dirver,type):
    if(type == 1):
        values=driver.quit()
        return values
    elif (type == 2):
        values= driver.find_element_by_id("kw").send_keys()
        return values
    else:
        values='类型不存在'
        print(values)
        return values

'''
driver webdriver对象
type,根据类型，获取值
type_name,元素的值
search，返回获取的元素参数
'''
def getFindElementsType(driver,type,type_name):
    if(type == 1):
        search=driver.find_element_by_id(type_name)
        return search
    elif(type == 2):
        search = driver.find_element_by_name(type_name)
        return search
    elif (type == 3):
        search = driver.find_element_by_xpath(".//*[@id='"+type_name+"']")
        return search
    elif (type == 4):
        search = driver.find_element_by_link_text(type_name)
        return search
    elif (type == 5):
        search = driver.find_element_by_partial_link_text(type_name)
        return search
    elif (type == 6):
        search = driver.find_element_by_class_name(type_name)
        return search
    elif (type == 7):
        search = driver.find_element_by_css_selector(type_name)
        return search
    elif (type == 8):
        search = driver.find_element_by_tag_name(type_name)
        return search
    elif (type == 9):
        search = driver.find_element(By.ID,type_name)
        return search
    else:
        print('没有合适的类型')
        search='没有合适的类型'
        return search

'''
获取截图
'''
def getScreenShot(driver,type,type_name):
    print('')

'''
选择事件
'''
def getSelectEvent(driver,type,type_name):
    print('')

'''
文件事件
'''
def getFileEvent(driver,type,type_name):
    print('')