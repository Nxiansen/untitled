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
    # 新版
    a = [i.strip() for i in klist]#去空格
    b = {i for i in a}  # 去重
    c = {n:n for n in b}#添加入字典
    print(type(c))#打印类型
    print(c)#输出

