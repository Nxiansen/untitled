import day444.qust1.my1 as q1
import day444.qust1.my2 as q2
import day444.qust1.my3 as q3
import day444.qust1.my4 as q4

if __name__ == '__main__':
    mdict={
        1:"[1]输入用户姓名及性别，然后给出下列的提示",
        2:"[2]随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
        3:"[3]注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息",
        4:"[4]从键盘输入一行字符串，判断是否是回文数",
        5:"[5]退出"
    }

    while True:
        for v in mdict.values():
            print(v)
        print("请选择功能：",end="")
        i=int(input())
        if i==1:
            print("输入性别时请输入，男/女")
            name = input("请输入姓名：")
            sex = input("请输入性别：")
            q1.chosex(name, sex)
            print()
        elif i==2:
            q2.suiji()
            print()
            print()
        elif i==3:
            q3.Email()
            print()
            print()
        elif i==4:
            q4.huiWen()
            print()
            print()
        elif i==5:
            print("下次再见。")
            break
