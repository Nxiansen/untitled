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
    print("编写Python程序打印输出字符串中重复的所有字符")
    newlist=[i.strip() for i in klist]
    newset={i for i in newlist}
    for i in newset:
        num=newlist.count(i)
        if num>=2:
            print("重复的单词为：{mya},重复的次数为：{mynum}".format(mya=i,mynum=num))