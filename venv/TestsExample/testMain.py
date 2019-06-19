from TestsExample import setGetMethod
from BaseHttp import HttpRuestBase,HttpRequestBean
import json
# per=setGetMethod.Person()
#
# per.set_name('shangying')
#
# print(type(per.get_name()))
#
url='http://www.baidu.com'
# url='http://httpbin.org/get'
json1={'a':'1'}
# cookies=HttpRuestBase.http
# Cookies(url)
# print('打印COOKIE的值',type(cookies))
# print('打印COOKIE的值',cookies)
# print('json1的类型',type(json1))
# json2=json.dumps(json1)
# print('json2的类型',type(json2))
# print(isinstance(json,dict))
num=['1','2','3']
print('num的类型',type(num))
# str1= ''.join(str(i) for i in num)
str1=json.loads(''.join(str(i) for i in num))
print('num的类型',type(str1))
print(str1)

list1=['a','b']
str2=','.join(list1)
print('打印str2的类型',str2)
# num1=json.loads(list.__dict__)
# print('num1的类型',num1)
# bean=HttpRuestBase.httpRequestGetJson(url)
# # # reslut=HttpRuestBase.httpRequestGet(url)
# print('打印COOKIE的值')
# print('打印COOKIE的值',bean.get_cookies())
# print('打印reslut.text得知',bean.get_responseJson())


