import pymysql
from Common import ParsePropertyMethod
import sys
class PyMySQL(object):
    def __init__(self):
        fileName = sys.path[6] + '\\' + 'Config' + '\\' + 'config_property'
        # fileName='E:\\项目汇集\测试项目\\python-mydemo\\venv\\Config\\config_property'
        print('结果值--》》'+fileName)
        p = ParsePropertyMethod.ParsePropertyMethod(fileName)
        properties = p.getProperties()
        if( properties['db.m.type'].__eq__('mysql')  ):
            print('进入mysql中')
            self.host=properties['db.m.host']
            self.port=int(properties['db.m.port'])
            print('port的type类型：',type(self.port))
            self.user=properties['db.m.user']
            self.passwd=properties['db.m.passwd']
            self.databasename=properties['db.m.databasename']
            self.charset=properties['db.m.charset']
        else:
            print('没有合适的数据库')
        print("port------->>>>>>>>>>>>>>>",self.port)
        self.conn=pymysql.Connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.databasename,charset=self.charset)
        if(self.conn != None):
          print('成功连接')
        else:
            print('尚未成功连接')

    def close_conn(self):
        if(self.conn !=None):
           self.conn.close()
        else:
            print('数据库易价关闭')

    def insertMethod(self,sql):
        print('插入数据')
        return None
    '''
    sql 执行语句
    **kwargs有key值
    '''
    def updateMethod(self,sql,**kwargs):
        print('插入数据')
        return None

    def selectMethod(self,sql,**kwargs):
        print('插入数据')
        return None

    def selectMethod(self,sql,**kwargs):
        print('插入数据')
        return None

if __name__ == '__main__':
    # mysql=PyMySQL('54.222.177.176',3306,'tamc','Tamc@2018!','tamc_longan_test','utf8')
    mysql = PyMySQL()
    mysql.close_conn()
    print('end')