import random
if __name__ == '__main__':
    a=[1,2,23,4,5,6,7]
    c=[o for o in a if o % 2 == 0]
    print(c.count(2))
    a=[random.randint(0,100) for i in range(0,10) if i%2==0]
    print(a)
    a={"o":1,"o1":1,"o2":1,"o3":1,"o4":1}
    for i,j in a.items():
        print(i,":",j,end=" ")
    print()
    print(a["o"])
    print(type(a))