def sj(num):
    for i in range(1,num+1):
        for j in range(1,num+1):
            print("*",end=" ")
            if j==i:
                print()
                break



if __name__ == '__main__':
    num=input("请输入三角形的边")
    sj(int(num))
