if __name__ == '__main__':


    meml = input("请输入一个邮箱:")
    mnum = meml.find("@")
    mdel = meml.find(".")

    if mnum == -1 and mdel == -1 :
        print("请输入正确的邮箱")
    elif mnum < 6 :
        print("长度不能少于6位")
    elif mdel >6 and mdel+1 != len(meml):
        print("邮箱输入正确")
    else :
        print("请输入正确邮箱")