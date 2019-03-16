if __name__ == '__main__':
    mlist=[] #or mlist=list()
    print(type(mlist))
    mlist.append("张三") #在列表末尾追加
    mlist.insert(0,"李四")#在列表指定位置添加
    mlist.insert(1,"王五")
    mlist.insert(1,"赵六")

    mlist.pop(1)#默认删除列表最后一个
    print(mlist)
    del mlist#删除列表，删除后mlist不存在，所以报错
    print(mlist)

    mlist.remove("赵六")#删除指定元素
    print(mlist)
    print(mlist.pop(0))