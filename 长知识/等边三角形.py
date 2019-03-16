if __name__ == '__main__':
    num=int(input("请输入三角列数"))+1
    for i in range(1,num):
        for j in range(1,i+1):
            sum=1
            summ=0
            for jj in range(1,j+1):
                if jj==1:
                    sum*=1
                else:
                    sum*=2
                summ+=sum
            print(summ,"\t",end="")
        print()







        if __name__ == '__main__':
            num = int(input("请输入三角列数")) + 1
            def triangles():
                n = [1]
                while True:
                    yield n
                    n = [x + y for x, y in zip([0] + n, n + [0])]
            n = 0
            for t in triangles():
                print(t)
                n = n + 1
                if n == num:
                    break
