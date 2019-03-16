import random

if __name__ == '__main__':
    a=input("输入一个整数，随机生成一个数字，比较这两个数字的大小")
    v=random.randrange(100)
    if int(a)>v:
        print("你赢了",a,">",v)
    else:
        print("你输了",a,"<",v)