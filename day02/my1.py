if __name__ == '__main__':
    s = ["s", "s", "d", "j", "f", "h", "g", "s", "d", "f", "h", "j", "k", "j", "s", "d", "f", "a", "u", "i"]
    d = set()
    for i in s:
        d.add(i)
    for i in d:
        num = s.count(i)
        if num >= 2:
            print("重复的是{0},重复的次数为：{1}".format(i, num))
            #列表实现