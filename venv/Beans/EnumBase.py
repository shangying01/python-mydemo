from enum import Enum
'''
    'CHROME':1,谷歌浏览器
    'FIREFOX':2,火狐浏览器
    'SAFARI':3,safra浏览器
    'IE':4，IE浏览器
'''
Browse={
    'CHROME':1,
    'FIREFOX':2,
    'SAFARI':3,
    'IE':4
}

'''
       'SLEEP':1,进程挂起的时间,强制等待
    'IMPLICITLY_WAIT':2,隐式等待
    'WEBDRIVERWAIT',显示等待
'''
Waite_Type={
    'SLEEP':1,
    'IMPLICITLY_WAIT':2,
    'WEBDRIVERWAIT':3
}


'''
    'ID':1,根据id查询
    'NAME':2,根据name查询
    'PATH':3,根据path查询
    'LINK_TEXT':4,根据link_text查询
    'PART_LINK_TEXT':5,根据part_link_text查询
    'CLASS_NAME':6,根据class_name查询
    'CSS_SELECTOR':7,根据css_selector查询
    'TAG_NAME':8,根据tag_text查询
    'ELEMENT_NAME':9,根据element_name查询
'''
Element_Type={
    'ID':1,
    'NAME':2,
    'PATH':3,
    'LINK_TEXT':4,
    'PART_LINK_TEXT':5,
    'CLASS_NAME':6,
    'CSS_SELECTOR':7,
    'TAG_NAME':8,
    'ELEMENT_NAME':9

}


'''
     'ID':1,根据id查询
    'NAME':2,根据name查询
    'PATH':3,根据path查询
    'LINK_TEXT':4,根据link_text查询
    'PART_LINK_TEXT':5,根据part_link_text查询
    'CLASS_NAME':6,根据class_name查询
    'CSS_SELECTOR':7,根据css_selector查询
    'TAG_NAME':8,根据tag_text查询
    'ELEMENT_NAME':9,根据element_name查询
'''
Elements_Type={
    'ID':1,
    'NAME':2,
    'PATH':3,
    'LINK_TEXT':4,
    'PART_LINK_TEXT':5,
    'CLASS_NAME':6,
    'CSS_SELECTOR':7,
    'TAG_NAME':8,
    'ELEMENT_NAME':9

}


'''
    'STRAT':1, 以某作为开始查询条件
    'END':2,以某作为结束查询条件
    'CONTAIN':3,查询条件中包含某值
    'ID':4,以id进行查询
    'NAME':5,以name进行查询
    'CSS':6,以css进行查询
    'LINK':7以link进行查询
'''
Element_Xpath_Type={
    'STRAT':1,
    'END':2,
    'CONTAIN':3,
    'ID':4,
    'NAME':5,
    'CSS':6,
    'LINK':7

}


'''
    'SETKEY': 1,直接设置
    'SELENIUM_SETKEY': 2,通过元素设置
    'KEYS_SPACE': 3，输入空格
    'KEYS_CONTROL': 4,复制
    'KEYS_ENTER':5,回车代替点击
    'KEYS_TAB':6,制表键
    'KEYS_ESCAPE':7,回退键
    
'''
Element_Set_Keys={
    'SETKEY': 1,
    'SELENIUM_SETKEY': 2,
    'KEYS_SPACE':3,
    'KEYS_CONTROL':4,
    'KEYS_ENTER':5,
    'KEYS_TAB':6,
    'KEYS_ESCAPE':7
}

'''
    'CLEAR':1,清除事件
    'SEND_KEYS':2,设值事件
    'CLICK':3,点击事件
    'SUBMIT':4，提交事件
    'IS_SELECTED':5,是非被选中事件
    'IS_ENABLED':6,判断元素是否被使用
    'IS_DISPLAYED':7判断元素是否显示
    'TEXT':8获取元素的文本值
'''
Element_Operate_Event={
    'CLEAR':1,
    'SEND_KEYS':2,
    'CLICK':3,
    'SUBMIT':4,
    'IS_SELECTED':5,
    'IS_ENABLED':6,
    'IS_DISPLAYED':7,
    'TEXT':8
}

'''
   'CURRENT_URL':1,获取当前页面的Url
   'CLOSE':2,关闭浏览器
   'QUITE':3,关闭浏览器并且退出驱动程序
   'BACK':4,返回上一页
   'CLEAR':5,清空输入框
   'MAXIMIZE_WINDOW':6,浏览器窗口最大化
   'NAME':7,查看浏览器的名字
   'GET_COOKIES':8,返回当前会话中的cookies
   'GET_WINDOW_SIZE':9,获取当前窗口的坐标
   'SWITH_TO_PARENT_CONTENT':10,返回上一级表单
   'SWITH_TO_DEFAULT_CONTENT':11,返回最外层表单
   'TITLE':12,获取当前page的title
   'FOWARD':13,前进
   'REFRESH':14,刷新
   
   
'''
Driver_Operate_Event={
    'CURRENT_URL': 1,
    'CLOSE':2,
    'QUITE': 3,
    'BACK': 4,
    'CLEAR': 5,
    'MAXIMIZE_WINDOW': 6,
    'NAME': 7,
    'GET_COOKIES': 8,
    'GET_WINDOW_SIZE': 9,
    'SWITH_TO_PARENT_CONTENT': 10,
    'SWITH_TO_DEFAULT_CONTENT': 11,
    'TITLE': 12,
    'FOWARD': 13,
    'REFRESH': 14
}