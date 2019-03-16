if __name__ == '__main__':
    i=range(101)
    print(type(i))
    for j in i:
        print(str(j).rjust(3," "),end="")
        if j % 10 == 9:
            print()
