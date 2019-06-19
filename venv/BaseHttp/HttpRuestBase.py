import requests
import json
from BaseHttp import HttpRequestBean
bean = HttpRequestBean.HttpRequestBean()
reslut = None
cookies = None
def httpRequestGetJson(url):
    reslut = httpRequestGet(url,None,None)
    return bean

def httpRequestGetWithHeaderJson(url,header):
    reslut = httpRequestGet(url, header, None)
    return bean

def httpRequestGetWithHeaderParaJson(url,header,paramer):
    reslut = httpRequestGet(url, header, paramer)
    return bean

def httpRequestGetReslut(url):
    reslut= httpRequestGetReslut(url,None,None)
    return reslut

def httpRequestGetWithHeaderReslut(url,header):
    reslut = httpRequestGetReslut(url,header,None)
    return bean

def httpRequestGetWithHeaderReslut(url,header,paramer):
     return bean


def httpRequestGet(url,header,paramer):
    reslut = requests.get(url, header, paramer)
    if (isinstance(reslut.text, dict)):
        bean.set_responseJson(json.load(reslut.text))
        bean.set_responseString(json.dump(reslut.text))
    elif (isinstance(reslut.text, list)):
        str1=','.join(reslut.text)
        print("reslut是list类型，请确认")
        bean.set_responseJson(json.load(str1))
        bean.set_responseString(str1)
    else:
        bean.set_responseString(reslut.text)
        bean.set_responseJson(reslut.text)
        print('不是正常json、数组、字符串')
    print("cookies的类型", cookies)
    bean.set_cookies(reslut.cookies)
    return bean

def httpRequestGetReslut(url,header,paramer):
    reslut = requests.get(url, header, paramer)
    return reslut

def httpRequestPostJson(url):
    requests.post(url)
    print()

def httpRequestPostWithHeader(url,header):
    print(url,header)

def httpRequestPostWithHeaderPara(url,header,paramer):
    print(url,header)

def httpRequestPost(url,data,json,paramer):
    reslut = requests.post(url,data,json,paramer)
    if (isinstance(reslut.text, dict)):
        bean.set_responseJson(json.load(reslut.text))
        bean.set_responseString(json.dump(reslut.text))
    elif (isinstance(reslut.text, list)):
        print("reslut是list类型，请确认")
    else:
        bean.set_responseString(reslut.text)
        bean.set_responseJson(reslut.text)
        print('不是正常json、数组、字符串')
    print("cookies的类型", cookies)
    bean.set_cookies(reslut.cookies)
    return bean

def httpRequestPostReslut(url):
    requests.post(url)
    print()

def httpRequestPostWithHeaderReslut(url,header):
    print(url,header)

def httpRequestPostWithHeaderParaReslut(url,header,paramer):
    print(url,header)

def httpRequestPost(url,data,json,paramer):
    reslut = requests.post(url,data,json,paramer)
    return reslut