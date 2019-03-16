
if __name__ == '__main__':
    for i in 1,2,3,4:
        for j in 1,2,3,4:
            print("*",end="")
            if i==j:
                print()
                break
    for i in 3,2,1:
        for j in 1,2,3:
            print("*",end="")
            if i==j:
                print()
                break
    for i in 3,2,1:
        for j in 1,2,3:
            if j==3:
                print(" ",end="")
            else:
                print("*",end="")
            if i==j:
                print()
                break