if __name__ == '__main__':
    #列表生成式
    a=[i for i in range(1,101)]
    print("1-100={0}".format(a))
    b=[i for i in range(1,101) if i%2==0]
    print("1-100为偶数={0}".format(b))
    c=[i for i in range(1,101) if i%2==1]
    print("1-100为奇数={0}".format(c))