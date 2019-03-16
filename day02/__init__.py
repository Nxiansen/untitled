
if __name__ == '__main__':
    s="sadkljfkljhasdjkfhas"
    q=set()
    for i in s:
        q.add(i)
    print(s.__len__()-q.__len__())
    #第一题