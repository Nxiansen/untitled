if __name__ == '__main__':
    while True:
        print("开始？0/1")
        c=input()
        if c==0:
            break
        else:
            s = input("请输入字符串，我帮你看看哪个重复了：")
            d = set()
            for i in s:
                d.add(i)
            for i in d:
                num = s.count(i)
                if num >= 2:
                    print("重复的是{0},重复的次数为：{1}".format(i, num))

    #第二题

