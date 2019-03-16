if __name__ == '__main__':
    s = input("输入数字:")
    mli = [i for i in s]
    nli = mli[:]
    print(nli)
    mli.reverse()
    print(mli)
    if nli == mli:
        print("是回文数")
    else:
        print("不是回文数")
        # reverse是用于列表等不是字符串