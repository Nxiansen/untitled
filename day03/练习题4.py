if __name__ == '__main__':
     # 把下面的klist作为字典的键
    # 并统计每个单词的词频
     klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
     ]
     newlist=[i.strip() for i in klist]#去空格 调用了strip()这个方法
     newset={i for i in newlist}#利用set集合的特性 去除重复
     newdict={}#新建一个字典类型的newdict
     for i in newset:
         num=newlist.count(i)#查看重复次数
         if num>=2:#如果大于的于2 就代表重复
             newdict[i]=num#or newdict.setdefault(i,num) 将键值存入字典
     print(newdict)#打印结果