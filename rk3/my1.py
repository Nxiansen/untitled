import random
if __name__ == '__main__':
    #.随机生成一个序列，再次生成一个整数，查看这个整数有没有在序列中（50分）
    b=[]
    for i in range(0,10):
        a = random.choice(range(1, 11))
        b.append(a)
    print(b)
    c=random.choice(range(1,11))
    print(c)
    if b.index(c):
        print("存在")
    else:
        print("不存在")