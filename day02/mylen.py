if __name__ == '__main__':
    s=[1,2,3,4,5]
    q=s.__len__()
    print(q)
    q=len(s)
    print(q)
    for l in s:
        print("下标为{1}[{0}]".format(l.__index__()-1,l))