#随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集

import random
# 并集就是把两个列表相加去重

def suiji():
    nlist = [random.randint(1, 21) for i in range(0, 15)]
    mlist = [random.randint(1, 31) for i in range(0, 10)]
    slist = mlist + nlist
    ulist = {i for i in slist}
    print("第一个随机列表为：{0}".format(nlist))
    print("第二个随机列表为：{0}".format(mlist))
    print("两列表的并集为：{0}".format(ulist))

'''交集：intersection。
差集：difference。
并集：union。
子集校验：issubset。
父集校验：issupperset。注意！只适用于set集合
'''