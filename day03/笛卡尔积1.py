if __name__ == '__main__':
    if __name__ == '__main__':
        a = [1, 2, 3, 4]
        b = ["q", "w", "e", "r"]
        c = [str(m) + n for m in a for n in b]
        print(c)

        j = [1, 2, 3, 4]
        k = ["q", "w", "e", "r"]
        l = [str(m) + n for m in j if m % 2 != 0 for n in k]
        print("奇数笛卡尔积=", l)  # \是换行实现