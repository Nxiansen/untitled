if __name__ == '__main__':
    #a="20150505"
    a=input("请输入日期")
    a1=a[0:4]
    print(a1)
    a2=a[4:6]
    print(a2)
    if int(a2)>=1:
        a3=a[6:]
        print(a3)
        if int(a3) <= 31 and int(a3) >= 1:
            print("这是{0}年的第{1}天".format(a1, int(a3)+31*(int(a2)-1)))
        else:
            print("您输入的日期有误")
    else:
        print("您输入的月份有问题")
