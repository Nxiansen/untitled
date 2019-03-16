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
    #去空格
    a=[i.strip() for i in klist]
    r={i:a.count(i) for i in a }
    print(r)
    print("究极缩写")







    # for i in b:
    #     num=a.count(i)
    #     d.setdefault(i,num)#存入字典
    # d[i]=num#与上功能相同