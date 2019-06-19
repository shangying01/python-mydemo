import pymongo
class MongoDBInit(object):
    def __init__(self, db_name, col_name):
        # 1 创建连接对象
        self.conn = pymongo.MongoClient(host="localhost", port=27017)
        # 2 获取数据库,
        # 如果这个数据库不存在，就在内存中虚拟创建
        # 当在库里创建集合的时候，就会在物理真实创建这个数据库
        #指定数据库
        self.db_name = self.conn[db_name]
        #指定集合
        self.col_name = self.db_name[col_name]

    def insert(self, data):
        print('打印一下data的类型',type(data))
        if isinstance(data, list):
            #插入多条数据
          self.col_name.insert_many(data)
        elif isinstance(data, dict):
            #插入一条数据
          self.col_name.insert_one(data)

    def delete(self, query, _all=False):
        if _all:
            #删除多条数据
          self.col_name.delete_many(query)
        else:
            #删除一条数据
          self.col_name.delete_one(query)

    def update(self, query, data):
        if isinstance(data, list):
            # 修改多条数据
          self.col_name.update_many(query, data)
        elif isinstance(data, dict):
            #修改一条
          self.col_name.update_one(query,data)

    def find(self, query, _all=False):
        if _all:
            #查找多条
          return self.col_name.find(query)
        else:
            #查找一条
          return self.col_name.find_one(query)
#
# if __name__ == '__main__':
#
#     m = MongoDBInit("databasetest", "tabletest")
#     m.insert([{"_id": 6, "name": "gkl"}, {"_id": 7, "name": "rfy"}])
#     # m.update({"name": "rfy"}, {"$set": {"name": "郭康伦"}})
#     for i in m.find({}, _all=True):
#        print(i)
