import random

if __name__ == '__main__':
    b=[]
    for i in range(0,10):
       b.append(random.choice(range(1, 11)))
    b.sort()
    print(b)
    print(2000==2000.0)#打印结果为True