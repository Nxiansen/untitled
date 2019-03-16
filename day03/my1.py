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

    a=klist.__len__()
    b={i for i in klist}
    b.discard("up")
    print(b)
    c=b.__len__()
    if a-c>0:
        print("有重复")
    else:
        print("无重复")