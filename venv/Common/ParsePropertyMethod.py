import re
import os
import tempfile
import e
import sys
import json

class ParsePropertyMethod(object):

    def __init__(self, fileName):
        self.fileName = fileName

    def getProperties(self):
        try:
            print('fileName地址的值-->>>',self.fileName)
            pro_file = open(self.fileName, 'r')
            properties = {}
            for line in pro_file:
                line = line.strip()
                if (line.find('=') > 0 and not line.startswith('#')):
                    strs = line.replace('\n','').split('=')
                    properties[strs[0].strip()] = strs[1].strip()
                else:
                    fopen.close()

        except Exception:
            raise
        return properties

if __name__ == '__main__':
    # fileName = sys.path[0] + '\\'+ 'system.properties'
    fileName=sys.path[6]+'\\'+'Config'+'\\'+'config_property'
    # fileName='E:\\项目汇集\测试项目\\python-mydemo\\venv\\Config\\config_property'
    p = ParsePropertyMethod(fileName)
    properties = p.getProperties()
    print('打印属性值：', properties)
    print('打印属性值：', properties['db.m.type'])
    # dict={'name':'shangying','age':9}
    # print('dict的值：',dict)
    # print(type(dict))
    # print(dict['age'])