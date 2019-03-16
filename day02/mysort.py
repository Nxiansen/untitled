#排序\
import random
if __name__ == '__main__':
    s=[5,9,1,6,3,7]
    reversed(s)
    s.sort(reverse=True)#reverse=? 队列表进行降序,默认为True,False则为正序
    print(s)
    random.shuffle(s)
    print(s)