if __name__ == '__main__':
    print("判断字符串是否重复")
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
    print("klist中字符串有空格，先去除空格")
    newlist=[i.strip() for i in klist]
    print("利用集合的特点，去重")
    newset={i for i in klist}
    print("分别求出去重之前和之后的中长度")
    num1=newlist.__len__()
    print("没去除重复之前的长度为：{newlistkey}".format(newlistkey=num1))
    num2=newset.__len__()
    print("除重复之前的长度为：{newsetkey}".format(newsetkey=num2))
    print("如果长度不等，则字符串有重复")
    print(num1-num2)
