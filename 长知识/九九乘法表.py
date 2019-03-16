import random
if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    for i in arr:
        for j in arr:
            s=str(j*i)
            t=str(s).rjust(2," ")
            print(j,"*",i,"=",t,end="  ")
            if i==j:
                print()
                break
#                 99乘法口诀