if __name__ == '__main__':
    print("年")
    a=int(input())
    print("月")
    b=int(input())
    print("日")
    c=int(input())
    num=0
    list={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:31,10:31,11:30,12:31}
    if (a%4==0 and a%100!=0)or a%400==0:
        for i in list.keys():
            if list.keys()==b:
                num+=i
        print("这是{0}年的第{1}".format(a,num+c))
    else:
        if int(str(b)+str(c))>218:
            for i in list.keys():
                num+=i
            print("这是{0}年的第{1}".format(a,num+c-1))
        else:
            for i in list.keys():
                num += i
            print("这是{0}年的第{1}".format(a, num + c))
