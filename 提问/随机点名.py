import random
if __name__ == '__main__':
    i=0
    p=[]
    while i<=100:
        i+=1
        name = ["李广军", "王志鹏", "靳中伟", "叶瑞金", "史欣阳",\
                "左孟龙", "孙浩宇", "史盼盼", "李墉", "王越", "王春旺", \
                "高山", "曹二方", "任海峰", "刘赛",\
                "宋成安", "周浩", "陈毅", "李新宇",\
                "董方龙", "莫乙洲", "杨鸿源", "赵昱", \
                "姜鑫悦", "梁一晗", "高碧云", "赵鹏浩",\
                "宁小健", "贾梦瑶", "赵政", \
                "赵柏淞", "赵澳", "王昊", "徐飞", "王雅哲", \
                "仝渊涛", "柴孟浩", "刘佳伟", "韩刚", \
                "张国斌", "高博", "伦宇"]
        b = random.choice(name)
        p.append(b)
    a = [i.strip() for i in p]
    r = {i: a.count(i) for i in a}
    print("点名100次随机出现名字的次数：",r)