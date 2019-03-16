if __name__ == '__main__':
    klist=input("输入字符串，查看重复的字母")
    # 去空格
    a = [i.strip() for i in klist]
    r = {i: a.count(i) for i in a}
    print(r)