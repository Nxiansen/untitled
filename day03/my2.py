if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    d=dict()
    a=[]#创建空列表
    for i in klist:#遍历klist列表
        a.append(i.strip())#将去除空格后的字符串装进新的空列表或i.split(" ")也能去除空格
    b=set()#创建空set集合
    # for i in a:#遍历a列表
    #     b.add(i)#将去除空格后的字符串添加进set集合中去重
    print("列表生产式")
    b={i for i in a}
    print(type(b))
    for i in b:#遍历集合
        num=a.count(i)#求出重复的词频
        if num>=2:
            d.setdefault(i,num)#放入字典
    print(d)