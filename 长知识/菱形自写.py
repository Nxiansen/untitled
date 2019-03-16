if __name__ == '__main__':
    for i in range(1,10):
        for j in range(1,10-i):
            print(end=" ")
        for a in range(1,i+1):
            print("*",end=" ")
        print()
    for b in range(2,10):
        for c in range(2,b+1):
            print(end=" ")
        for d in range(b,10):
            print("*",end=" ")
        print()