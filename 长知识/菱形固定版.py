if __name__ == '__main__':
    i=1
    sum=7
    while i<=sum:
        j=0
        while j<sum-i:
            print(" ",end="")
            j+=1
        j=0
        while j<2*i-1:
            print("*",end="")
            j+=1
        i+=1
        print()
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


