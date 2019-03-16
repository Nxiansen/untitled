if __name__ == '__main__':
# 老版
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
    j=[]
    for i in klist:
       j.append(i.strip())
    k=set()
    for i in j:
        k.add(i)
    l=dict()
    for n in k:
        l.setdefault(n)#l[n]=n
    print(l)