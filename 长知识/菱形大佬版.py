if __name__ == '__main__':
    numinput = input("请输入菱形的行数")
    sum=int(numinput)
    i=1
    #控制列数
    while i<=sum:
        j=0
        #上半三角的每行空格数
        while j<sum-i:
            print(" ",end="")#输出前面的空格
            j+=1    #控制变量自增
        j=0 #初始化j为下面循环使用
        #上半三角的每行*数量
        while j<2*i-1:
            print("*",end="")#输出*不换行
            j+=1    #输出星号的次数自增
        i+=1        #行数自增
        print()     #一行结束后换行语句



    i=sum-1
    while i>0:
        j=sum-i
        while j>0:
            print(" ",end="")
            j-=1
        j=i*2-1
        while j>0:
            print("*",end="")
            j-=1
        i-=1
        print()