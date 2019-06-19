a=1
def getREslut(a):

    if(a>2):
        print(a)
        print('获取b的真实结果：',a)
        result=getSelect(a)
        print('打印结果reslut'+result)
    else:
        a+=1
        print('每次的a的值',a)
        getREslut(a)

def getSelect(b):
    if(b == 1):
        print('ONE')
        return 'ONE'
    elif(b == 2):
        print('TWO')
        return 'TWO'
    elif(b == 3):
        print('THREE')
        return 'THREE'
    else:
        print('i don’/ no')
        return 'NONE'


if __name__ == '__main__':
  getREslut(a)