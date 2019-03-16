#把下面的klist作为字典的键
#同时作为字典的值
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
    newlist=[i.strip() for i in klist]
    newset={i for i in newlist}
    newdict={n:n for n in newset}
    print("字典的键和值为：{mydic}".format(mydic=newdict))
